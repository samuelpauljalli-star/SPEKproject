# Wilson Health Care - Firebase Integration

## 🔥 Firebase Services Integrated

This project now includes the following Firebase services:

1. **Firebase Analytics** - Track user behavior and page visits
2. **Firebase Authentication** - Secure Google Sign-In for admin access
3. **Firebase Firestore** - NoSQL database for storing orders and user data

## 🚀 Setup Instructions

### Prerequisites
- Node.js installed (v24.13.1 or later)
- Firebase project created at [Firebase Console](https://console.firebase.google.com/)

### Firebase Configuration

Your Firebase configuration is already set up in `firebase-config.js` with:
- Project ID: `wilson-health-care`
- Auth Domain: `wilson-health-care.firebaseapp.com`

### Enable Services in Firebase Console

**Important:** You need to enable these services in your Firebase Console:

#### 1. Enable Google Authentication
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: `wilson-health-care`
3. Navigate to **Authentication** → **Sign-in method**
4. Click **Add new provider**
5. Select **Google**
6. Enable it and click **Save**

#### 2. Enable Firestore Database
1. In Firebase Console, go to **Firestore Database**
2. Click **Create database**
3. Choose **Start in production mode** (or test mode for development)
4. Select your preferred region (e.g., `asia-south1` for India)
5. Click **Enable**

#### 3. Set Up Firestore Security Rules
In Firestore → **Rules**, add:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow authenticated admins to read/write
    match /{document=**} {
      allow read, write: if request.auth != null && 
        (request.auth.token.email == 'samuelpauljalli@gmail.com' ||
         request.auth.token.email == 'wilsonhealthcare7@gmail.com');
    }
  }
}
```

#### 4. Add Authorized Domains
1. Go to **Authentication** → **Settings** → **Authorized domains**
2. Add your domain (e.g., `localhost` for testing, your production domain later)

## 📁 File Structure

```
wilson_health_care/
├── firebase-config.js          # Firebase initialization & exports
├── index.html                  # Main website (includes Analytics)
├── peter.html                  # Admin dashboard (includes Auth)
├── data.js                     # Product data
├── package.json                # Dependencies
└── README_FIREBASE.md          # This file
```

## 🔐 Admin Authentication

### How It Works
- Admin page (`peter.html`) uses **Firebase Google Authentication**
- Only authorized emails can access the dashboard:
  - `samuelpauljalli@gmail.com`
  - `wilsonhealthcare7@gmail.com`
  - Any email containing "admin"

### Testing Locally
1. Open `peter.html` in a browser
2. Click "Authenticate with Gmail"
3. Sign in with an authorized Google account
4. Access granted!

## 📊 Using Firestore Database

### Example: Save Order to Firestore

```javascript
import { db, collection, addDoc, serverTimestamp } from './firebase-config.js';

async function saveOrder(orderData) {
    try {
        const docRef = await addDoc(collection(db, "orders"), {
            ...orderData,
            timestamp: serverTimestamp()
        });
        console.log("Order saved with ID:", docRef.id);
    } catch (error) {
        console.error("Error adding order:", error);
    }
}
```

### Example: Fetch Orders

```javascript
import { db, collection, getDocs, query, orderBy } from './firebase-config.js';

async function getOrders() {
    const q = query(collection(db, "orders"), orderBy("timestamp", "desc"));
    const querySnapshot = await getDocs(q);
    
    const orders = [];
    querySnapshot.forEach((doc) => {
        orders.push({ id: doc.id, ...doc.data() });
    });
    
    return orders;
}
```

## 🎯 Next Steps

1. **Enable Firebase Services** (see above)
2. **Test Authentication** - Try logging into `peter.html`
3. **Migrate Data** - Move from localStorage to Firestore
4. **Add Firestore Rules** - Secure your database
5. **Deploy** - Host on Firebase Hosting or your preferred platform

## 🛠️ Development

### Install Dependencies (Optional)
If you want to use build tools:
```bash
npm install
```

### Current Setup
- Uses **CDN imports** - No build step required!
- Works directly in the browser
- ES6 modules supported

## 📝 Support

For Firebase documentation:
- [Firebase Auth Docs](https://firebase.google.com/docs/auth)
- [Firestore Docs](https://firebase.google.com/docs/firestore)
- [Firebase Console](https://console.firebase.google.com/)

## ✅ Checklist

- [x] Firebase config file created
- [x] Authentication integrated
- [x] Firestore SDK added
- [ ] Enable Authentication in Firebase Console
- [ ] Enable Firestore in Firebase Console
- [ ] Set up Firestore security rules
- [ ] Test admin login
- [ ] Migrate data to Firestore

---

**Created for Wilson Health Care** 🏥
