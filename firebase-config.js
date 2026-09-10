// Central Firebase Configuration for SPEK Tech Superstore
// Uses Firebase modular JavaScript SDK with ES modules for direct browser integration
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
import { 
    getAuth, 
    GoogleAuthProvider, 
    signInWithPopup, 
    signOut, 
    signInWithEmailAndPassword, 
    createUserWithEmailAndPassword,
    onAuthStateChanged,
    updateProfile
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { 
    getFirestore, 
    collection, 
    doc, 
    setDoc, 
    getDoc, 
    getDocs, 
    addDoc, 
    updateDoc, 
    deleteDoc, 
    query, 
    where, 
    orderBy, 
    serverTimestamp,
    limit
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

// Web App Firebase Configuration
const firebaseConfig = {
    apiKey: "AIzaSyCh5w0Vljp-7dV_Ui_8gTXj_WKF5TyEToA",
    authDomain: "wilson-health-care.firebaseapp.com",
    projectId: "wilson-health-care",
    storageBucket: "wilson-health-care.firebasestorage.app",
    messagingSenderId: "60179173764",
    appId: "1:60179173764:web:adfda13ac51d1140a00dd1",
    measurementId: "G-KT8FX5KZEB"
};

// Initialize Firebase App & Services
let app = null;
let auth = null;
let db = null;
let analytics = null;
let provider = null;

try {
    app = initializeApp(firebaseConfig);
    try { 
        analytics = getAnalytics(app); 
    } catch (e) {
        // Analytics is optional in local development
    }
    auth = getAuth(app);
    db = getFirestore(app);
    provider = new GoogleAuthProvider();
    console.log("Firebase App, Auth, and Cloud Firestore initialized successfully.");
} catch (e) {
    console.warn("Firebase initialization notice:", e);
}

// Export central instances and modular methods
export { 
    app, 
    auth, 
    db, 
    analytics, 
    provider,
    GoogleAuthProvider, 
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
    deleteDoc, 
    query, 
    where, 
    orderBy, 
    serverTimestamp,
    limit
};
