# GYM MEMBER REGISTRATION FORM - Google Forms Setup Instructions

## Files in this folder:
- `updated_with_logo.pdf` - Original PDF form
- `logo_0_0.png` - Extracted gym logo (from page 1)
- `logo_2_0.png` - Extracted logo (from page 3)
- `create_google_form.js` - Google Apps Script to create the form

---

## Step-by-Step Instructions

### Step 1: Create the Google Form

1. Go to **[Google Apps Script](https://script.google.com/)** (script.google.com)
2. Click **"New Project"**
3. Delete any existing code in the editor
4. Copy the entire content of `create_google_form.js` and paste it
5. Click the **floppy disk icon** or press `Ctrl+S` to save
6. Name the project (e.g., "Gym Registration Form Creator")

### Step 2: Run the Script

1. In the toolbar, select **`main`** from the function dropdown
2. Click the **▶️ Run** button
3. A dialog will appear asking for authorization - click **"Review Permissions"**
4. Select your Google account
5. Click **"Advanced"** → **"Go to [Project Name] (unsafe)"**
6. Click **"Allow"** to grant permissions

### Step 3: Get the Form URL

1. After the script runs, click **"Execution log"** at the bottom
2. You'll see:
   - **Published URL**: Share this with gym members to fill out the form
   - **Edit URL**: Use this to customize the form

### Step 4: Add the Logo to the Form

1. Open the **Edit URL** in your browser
2. Click on the **header area** at the top of the form
3. Click **"Choose image"**
4. Select **"Upload"** tab
5. Upload the `logo_0_0.png` file from this folder
6. Position and resize as needed

### Step 5: Customize the Form Theme (Optional)

1. In the form editor, click the **palette icon** 🎨 (Customize theme)
2. Choose a **color theme** that matches your gym branding
3. Select a **background color**
4. Choose a **font style**

---

## Form Structure Created

The script creates the following sections:

1. **Personal Information**
   - Full Name, Date of Birth, Address, City, State, Pin Code
   - Phone Number (10-digit validation)
   - Email Address (email validation)

2. **Emergency Contact Information**
   - Full Name, Phone Number, Relationship

3. **Health & Fitness Information**
   - Medical conditions (Yes/No + explanation)
   - Fitness Goals (multiple choice)

4. **Membership Options**
   - Monthly / Quarterly / Annual / Other

5. **Payment Options**
   - Cash / Paytm / PhonePe / Google Pay
   - Payment authorization consent

6. **Consent and Waivers**
   - Exercise risk acknowledgement
   - Marketing consent
   - Image/video consent
   - Data protection acknowledgement

7. **Final Acknowledgement**
   - Terms acceptance
   - Digital signature (name)
   - Date

---

## Collecting Responses

1. In the form editor, click the **"Responses"** tab
2. Click the **Google Sheets icon** to create a linked spreadsheet
3. All form submissions will be automatically saved to the spreadsheet

---

## Need Help?

If you encounter any issues:
1. Make sure you're signed into a Google account
2. Ensure you have permission to create Google Forms
3. Check that pop-ups are enabled in your browser
