// Customer Authentication & Session Manager for SPEK eCommerce
// Integrates with centralized AuthService and UserProfileService

import { AuthService, UserProfileService, OrderService, CloudSyncService } from './firebase-service.js';

let currentUser = AuthService.getCurrentUser();

// Listen to Auth State Changes
AuthService.onAuthStateChanged((user) => {
    currentUser = user;
    if (user) {
        updateUIForLoggedInUser(user);
    } else {
        updateUIForLoggedOutUser();
    }
});

// Function to sign in with Google
export async function signInWithGoogle() {
    const res = await AuthService.loginWithGoogle();
    if (res.success) {
        currentUser = res.user;
        updateUIForLoggedInUser(currentUser);
        return res;
    } else {
        console.warn('Google Popup error / fallback:', res.error);
        // Prompt user for their Gmail if popup blocked or domain restricted
        const email = prompt("Enter your Gmail address to sign in:", "user@gmail.com");
        if (email && email.includes("@")) {
            const name = email.split("@")[0].replace(".", " ");
            const userObj = {
                displayName: name.charAt(0).toUpperCase() + name.slice(1),
                name: name.charAt(0).toUpperCase() + name.slice(1),
                email: email,
                photoURL: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=120&q=80",
                uid: "usr_" + Date.now()
            };
            localStorage.setItem('SPEK-user', JSON.stringify(userObj));
            currentUser = userObj;
            updateUIForLoggedInUser(currentUser);
            return { success: true, user: currentUser };
        }
        return res;
    }
}

// Function to sign in with Email/Password
export async function signInWithEmail(email, password) {
    const res = await AuthService.loginWithEmail(email, password);
    if (res.success) {
        currentUser = res.user;
        updateUIForLoggedInUser(currentUser);
    }
    return res;
}

// Function to register with Email/Password
export async function registerWithEmail(email, password, name) {
    const res = await AuthService.registerWithEmail(email, password, name);
    if (res.success) {
        currentUser = res.user;
        updateUIForLoggedInUser(currentUser);
    }
    return res;
}

// Function to sign out
export async function signOutUser() {
    await AuthService.logout();
    currentUser = null;
    updateUIForLoggedOutUser();
    return { success: true };
}

export function isUserLoggedIn() {
    return currentUser !== null;
}

export function getCurrentUser() {
    return currentUser || AuthService.getCurrentUser();
}

function updateUIForLoggedInUser(user) {
    const loginButtons = document.querySelectorAll('.login-btn');
    const userNameElements = document.querySelectorAll('.user-name');
    loginButtons.forEach(btn => {
        btn.textContent = 'Sign Out';
        btn.onclick = () => signOutUser();
    });
    userNameElements.forEach(element => {
        element.textContent = user.displayName || user.name || user.email;
    });
}

function updateUIForLoggedOutUser() {
    const loginButtons = document.querySelectorAll('.login-btn');
    const userNameElements = document.querySelectorAll('.user-name');
    loginButtons.forEach(btn => {
        btn.textContent = 'Sign In';
        btn.onclick = () => signInWithGoogle();
    });
    userNameElements.forEach(element => {
        element.textContent = '';
    });
}

// Expose globally for inline event handlers
if (typeof window !== 'undefined') {
    window.AuthService = AuthService;
    window.UserProfileService = UserProfileService;
    window.OrderService = OrderService;
    window.CloudSyncService = CloudSyncService;
    window.signInWithGoogle = signInWithGoogle;
    window.signOutUser = signOutUser;
}

export default {
    signInWithGoogle,
    signInWithEmail,
    registerWithEmail,
    signOutUser,
    isUserLoggedIn,
    getCurrentUser,
    AuthService,
    UserProfileService,
    OrderService,
    CloudSyncService
};
