// SPOKE Tech Superstore - Firebase Service Layer
// Cleanly encapsulates Firebase Authentication and Cloud Firestore operations

import {
    auth,
    db,
    provider,
    signInWithPopup,
    signOut,
    signInWithEmailAndPassword,
    createUserWithEmailAndPassword,
    onAuthStateChanged,
    updateProfile,
    collection,
    doc,
    setDoc,
    getDoc,
    getDocs,
    addDoc,
    updateDoc,
    query,
    where,
    orderBy,
    serverTimestamp,
    limit
} from './firebase-config.js';

// ==========================================
// 1. AUTHENTICATION SERVICE
// ==========================================
export const AuthService = {
    /**
     * Sign in with Google Popup
     */
    async loginWithGoogle() {
        try {
            if (!auth || !provider) {
                throw new Error("Firebase Auth is not initialized.");
            }
            const result = await signInWithPopup(auth, provider);
            const user = result.user;
            
            const profileData = {
                uid: user.uid,
                name: user.displayName || 'SPOKE Customer',
                email: user.email,
                photoURL: user.photoURL || '',
                phone: user.phoneNumber || '',
                lastLogin: new Date().toISOString()
            };

            // Write/Merge User Profile in Firestore
            await UserProfileService.saveUserProfile(user.uid, profileData);
            
            // Persist session to localStorage
            localStorage.setItem('SPOKE-user', JSON.stringify(profileData));
            return { success: true, user: profileData };
        } catch (error) {
            console.warn("AuthService.loginWithGoogle error:", error);
            return { success: false, error: error.message };
        }
    },

    /**
     * Register a new user with Email and Password
     */
    async registerWithEmail(email, password, fullName = '') {
        try {
            if (!auth) throw new Error("Firebase Auth is not initialized.");
            
            const userCredential = await createUserWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;

            if (fullName && auth.currentUser) {
                await updateProfile(auth.currentUser, { displayName: fullName });
            }

            const profileData = {
                uid: user.uid,
                name: fullName || email.split('@')[0],
                email: user.email,
                phone: user.phoneNumber || '',
                photoURL: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=120&q=80',
                createdAt: new Date().toISOString()
            };

            // Save to Firestore
            await UserProfileService.saveUserProfile(user.uid, profileData);
            localStorage.setItem('SPOKE-user', JSON.stringify(profileData));
            return { success: true, user: profileData };
        } catch (error) {
            console.error("AuthService.registerWithEmail error:", error);
            return { success: false, error: error.message };
        }
    },

    /**
     * Sign in existing user with Email and Password
     */
    async loginWithEmail(email, password) {
        try {
            if (!auth) throw new Error("Firebase Auth is not initialized.");
            
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;

            // Retrieve existing profile from Firestore
            let profile = await UserProfileService.getUserProfile(user.uid);
            if (!profile) {
                profile = {
                    uid: user.uid,
                    name: user.displayName || email.split('@')[0],
                    email: user.email,
                    photoURL: user.photoURL || '',
                    phone: user.phoneNumber || ''
                };
                await UserProfileService.saveUserProfile(user.uid, profile);
            }

            localStorage.setItem('SPOKE-user', JSON.stringify(profile));
            return { success: true, user: profile };
        } catch (error) {
            console.error("AuthService.loginWithEmail error:", error);
            return { success: false, error: error.message };
        }
    },

    /**
     * Sign out current user
     */
    async logout() {
        try {
            if (auth) await signOut(auth);
            localStorage.removeItem('SPOKE-user'); localStorage.removeItem('SPEK-user');
            return { success: true };
        } catch (error) {
            console.error("AuthService.logout error:", error);
            localStorage.removeItem('SPOKE-user'); localStorage.removeItem('SPEK-user');
            return { success: true };
        }
    },

    /**
     * Subscribe to auth state changes
     */
    onAuthStateChanged(callback) {
        if (!auth) return () => {};
        return onAuthStateChanged(auth, async (user) => {
            if (user) {
                const profile = await UserProfileService.getUserProfile(user.uid) || {
                    uid: user.uid,
                    name: user.displayName || 'Customer',
                    email: user.email,
                    photoURL: user.photoURL || ''
                };
                localStorage.setItem('SPOKE-user', JSON.stringify(profile));
                callback(profile);
            } else {
                callback(null);
            }
        });
    },

    /**
     * Get local cached user
     */
    getCurrentUser() {
        try {
            return JSON.parse(localStorage.getItem('SPOKE-user') || localStorage.getItem('SPEK-user')) || null;
        } catch (e) {
            return null;
        }
    }
};

// ==========================================
// 2. USER PROFILE SERVICE (Cloud Firestore)
// ==========================================
export const UserProfileService = {
    /**
     * Save or merge user profile in `users/{uid}`
     */
    async saveUserProfile(uid, data) {
        if (!db || !uid) return null;
        try {
            const userRef = doc(db, 'users', uid);
            const payload = {
                ...data,
                updatedAt: serverTimestamp()
            };
            await setDoc(userRef, payload, { merge: true });
            return true;
        } catch (error) {
            console.warn("UserProfileService.saveUserProfile error:", error);
            return false;
        }
    },

    /**
     * Get user profile by UID
     */
    async getUserProfile(uid) {
        if (!db || !uid) return null;
        try {
            const userRef = doc(db, 'users', uid);
            const snapshot = await getDoc(userRef);
            if (snapshot.exists()) {
                return snapshot.data();
            }
            return null;
        } catch (error) {
            console.warn("UserProfileService.getUserProfile error:", error);
            return null;
        }
    }
};

// ==========================================
// 3. ORDER SERVICE (Cloud Firestore)
// ==========================================
export const OrderService = {
    /**
     * Save an order to Cloud Firestore `orders` collection
     */
    async createOrder(orderData) {
        try {
            // Also store locally for instant offline reliability
            const localOrders = JSON.parse(localStorage.getItem('SPOKE-orders') || localStorage.getItem('SPEK-orders')) || [];
            localOrders.unshift(orderData);
            localStorage.setItem('SPOKE-orders', JSON.stringify(localOrders));

            if (!db) return { success: true, orderId: orderData.orderId, source: 'local' };

            const ordersCollection = collection(db, 'orders');
            const docPayload = {
                ...orderData,
                serverCreatedAt: serverTimestamp()
            };

            const docRef = await addDoc(ordersCollection, docPayload);
            return { success: true, firestoreId: docRef.id, orderId: orderData.orderId, source: 'firestore' };
        } catch (error) {
            console.warn("OrderService.createOrder Firestore notice (fallback to local):", error);
            return { success: true, orderId: orderData.orderId, source: 'local_fallback' };
        }
    },

    /**
     * Retrieve orders for a specific user ID
     */
    async getUserOrders(userId) {
        try {
            const localOrders = JSON.parse(localStorage.getItem('SPOKE-orders') || localStorage.getItem('SPEK-orders')) || [];
            if (!db || !userId) return localOrders;

            const q = query(
                collection(db, 'orders'),
                where('userId', '==', userId),
                orderBy('serverCreatedAt', 'desc'),
                limit(50)
            );
            
            const querySnapshot = await getDocs(q);
            const firestoreOrders = [];
            querySnapshot.forEach((doc) => {
                firestoreOrders.push({ id: doc.id, ...doc.data() });
            });

            if (firestoreOrders.length > 0) {
                return firestoreOrders;
            }
            return localOrders;
        } catch (error) {
            console.warn("OrderService.getUserOrders error (using local):", error);
            return JSON.parse(localStorage.getItem('SPOKE-orders') || localStorage.getItem('SPEK-orders')) || [];
        }
    },

    /**
     * Cancel an order in Firestore and locally
     */
    async cancelOrder(orderId) {
        try {
            const localOrders = JSON.parse(localStorage.getItem('SPOKE-orders') || localStorage.getItem('SPEK-orders')) || [];
            const updated = localOrders.map(o => o.orderId === orderId ? { ...o, status: 'Cancelled' } : o);
            localStorage.setItem('SPOKE-orders', JSON.stringify(updated));

            if (db) {
                const q = query(collection(db, 'orders'), where('orderId', '==', orderId));
                const snapshot = await getDocs(q);
                snapshot.forEach(async (d) => {
                    await updateDoc(doc(db, 'orders', d.id), { status: 'Cancelled', cancelledAt: serverTimestamp() });
                });
            }
            return true;
        } catch (e) {
            console.warn("OrderService.cancelOrder error:", e);
            return false;
        }
    }
};

// ==========================================
// 4. CLOUD SYNC SERVICE (Cart & Wishlist)
// ==========================================
export const CloudSyncService = {
    /**
     * Save user wishlist to Cloud Firestore `wishlists/{userId}`
     */
    async syncWishlist(userId, wishlistItems) {
        if (!db || !userId) return;
        try {
            await setDoc(doc(db, 'wishlists', userId), {
                userId,
                items: wishlistItems,
                updatedAt: serverTimestamp()
            }, { merge: true });
        } catch (e) {
            console.warn("CloudSyncService.syncWishlist error:", e);
        }
    },

    /**
     * Retrieve user wishlist from Cloud Firestore
     */
    async getWishlist(userId) {
        if (!db || !userId) return null;
        try {
            const snapshot = await getDoc(doc(db, 'wishlists', userId));
            if (snapshot.exists()) {
                return snapshot.data().items || [];
            }
            return null;
        } catch (e) {
            console.warn("CloudSyncService.getWishlist error:", e);
            return null;
        }
    },

    /**
     * Save user cart to Cloud Firestore `carts/{userId}`
     */
    async syncCart(userId, cartItems) {
        if (!db || !userId) return;
        try {
            await setDoc(doc(db, 'carts', userId), {
                userId,
                items: cartItems,
                updatedAt: serverTimestamp()
            }, { merge: true });
        } catch (e) {
            console.warn("CloudSyncService.syncCart error:", e);
        }
    }
};

// Default export combining all services
export default {
    AuthService,
    UserProfileService,
    OrderService,
    CloudSyncService
};
