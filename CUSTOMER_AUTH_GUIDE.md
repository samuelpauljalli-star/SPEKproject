# Customer Authentication Implementation Guide

## Overview
This guide helps you implement mandatory Google Sign-In for customers when placing orders.

---

## Step 1: Add Customer Auth Script to index.html

Add this script tag in the `<head>` section of `index.html` (after the firebase-config.js script):

```html
<script type="module" src="customer-auth.js"></script>
```

---

## Step 2: Update Your Order/Checkout Flow

### Find the "Buy Now" or "Checkout" Button Handler

Look for the function that handles when a customer clicks "Buy Now" or "Checkout". 
Then add authentication check:

```javascript
import { isUserLoggedIn, getCurrentUser, signInWithGoogle } from './customer-auth.js';

async function handleOrderClick() {
    // Check if user is logged in
    if (!isUserLoggedIn()) {
        // Show login modal/prompt
        const result = await signInWithGoogle();
        
        if (!result.success) {
            alert('Please sign in to place an order');
            return;
        }
    }
    
    // Get current user details
    const user = getCurrentUser();
    
    // Continue with order placement
    proceedWithOrder(user);
}

function proceedWithOrder(user) {
    // Your existing order logic here
    // You now have access to:
    // - user.displayName
    // - user.email
    // - user.photoURL
    // - user.uid
    
    // Save order with user info
    const orderData = {
        orderId: generateOrderId(),
        customer: {
            name: user.displayName,
            email: user.email,
            // ... other customer info
        },
        // ... order items, total, etc.
    };
    
    // Save to localStorage or Firebase
    saveOrder(orderData);
}
```

---

## Step 3: Add Login UI to Your Website

### Option A: Add a Login Button in Navigation

Add this to your navigation bar in `index.html`:

```html
<nav>
    <!-- Your existing nav items -->
    <button class="login-btn" id="userLoginBtn">Sign In</button>
    <span class="user-name" id="userName"></span>
</nav>
```

Add some CSS:
```css
.login-btn {
    background: var(--primary);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
}

.user-name {
    color: var(--primary);
    font-weight: 600;
    margin-left: 10px;
}
```

### Option B: Show Modal Before Checkout

Create a login modal that appears when user tries to checkout without being logged in:

```html
<!-- Add this before closing </body> tag -->
<div id="loginModal" class="modal-overlay" style="display: none;">
    <div class="modal-content">
        <h2>Sign In Required</h2>
        <p>Please sign in to continue with your order</p>
        <button onclick="handleGoogleSignIn()" class="google-btn">
            <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/pwa_brand/google__72dp.png" 
                 style="width: 20px; margin-right: 10px;">
            Sign in with Google
        </button>
        <button onclick="closeLoginModal()" class="cancel-btn">Cancel</button>
    </div>
</div>

<script type="module">
    import { signInWithGoogle } from './customer-auth.js';
    
    window.handleGoogleSignIn = async function() {
        const result = await signInWithGoogle();
        if (result.success) {
            document.getElementById('loginModal').style.display = 'none';
            // Proceed with order
        }
    }
    
    window.closeLoginModal = function() {
        document.getElementById('loginModal').style.display = 'none';
    }
</script>
```

---

## Step 4: Make Login Mandatory for Orders

Update your existing order placement code to always check authentication:

```javascript
// Example: When user clicks "Add to Cart" or "Buy Now"
document.querySelectorAll('.buy-now-btn').forEach(button => {
    button.addEventListener('click', async function() {
        // Check login first
        if (!isUserLoggedIn()) {
            // Show login modal or redirect to sign in
            document.getElementById('loginModal').style.display = 'flex';
            return; // Stop here until user logs in
        }
        
        // User is logged in, continue with order
        const user = getCurrentUser();
        // ... your order logic
    });
});
```

---

## Step 5: Track User Data for Admin Dashboard

The customer authentication automatically saves user data to `localStorage` under the key `wilson-user-history`. This is displayed in your admin dashboard automatically.

---

## Testing

1. **Open your website** in a browser
2. **Try to place an order** without logging in
3. **You should be prompted** to sign in with Google
4. **After signing in**, the order should proceed
5. **Check the admin dashboard** (`peter.html`) to see the logged-in user in "Customer History"

---

## Important Notes

✅ **Admin access** is now restricted to only the two specified emails
✅ **Customer authentication helper** is ready to use
✅ **User tracking** is automatic

⚠️ **Next Steps You Need to Complete:**
1. **Integrate** `customer-auth.js` into your existing order flow
2. **Add UI** for login/logout buttons
3. **Test** the complete flow from sign-in to order placement

---

## Need Help?

If you need help finding where your order/checkout code is, search for:
- "add to cart"
- "buy now"
- "checkout"
- "place order"

in your `index.html` file and integrate the auth check there.
