# EmailJS Setup Instructions for Maxx Fitness Contact Form

Your contact form has been updated to send emails to **maxxfitnesswebsite@gmail.com**. To complete the setup, you need to configure EmailJS (a free email service for websites).

## Step 1: Create EmailJS Account

1. Go to [https://www.emailjs.com](https://www.emailjs.com)
2. Sign up for a free account
3. Verify your email address

## Step 2: Connect Your Gmail Account

1. In your EmailJS dashboard, go to "Email Services"
2. Click "Add New Service"
3. Select "Gmail" 
4. Connect your **maxxfitnesswebsite@gmail.com** account
5. Note down the **Service ID** (something like "service_xxxxxxx")

## Step 3: Create Email Template

1. Go to "Email Templates" in your EmailJS dashboard
2. Click "Create New Template"
3. Use this template:

**Template Name:** Contact Form
**Subject:** New Contact Form Submission - Maxx Fitness
**Content:**
```
Hello Maxx Fitness Team,

You have received a new contact form submission from your website.

Name: {{from_name}}
Email: {{from_email}}

Message:
{{message}}

---
This message was sent from the Maxx Fitness website contact form.
Please reply to: {{reply_to}}
```

4. Save the template and note down the **Template ID** (something like "template_xxxxxxx")

## Step 4: Get Your Public Key

1. Go to "Account" > "General" in your EmailJS dashboard
2. Find your **Public Key** (something like "xxxxxxxxxxxxxx")

## Step 5: Update Your Website Code

Open your `script.js` file and replace these placeholders:

1. Replace `YOUR_EMAILJS_USER_ID` with your **Public Key**
2. Replace `YOUR_SERVICE_ID` with your **Service ID** 
3. Replace `YOUR_TEMPLATE_ID` with your **Template ID**

Example:
```javascript
emailjs.init("abcd1234efgh5678"); // Your Public Key
emailjs.send('service_abc123', 'template_xyz789', templateParams) // Your Service ID and Template ID
```

## Step 6: Test the Contact Form

1. Open your website
2. Go to the contact section
3. Fill out the form and submit
4. Check if you receive the email at maxxfitnesswebsite@gmail.com

## Backup Feature

If EmailJS fails for any reason, the form will automatically fall back to opening the user's email client with a pre-filled email to **maxxfitnesswebsite@gmail.com**.

## Free Plan Limits

EmailJS free plan includes:
- 200 emails per month
- Basic email templates
- Standard support

This should be sufficient for most gym contact forms. If you need more emails, you can upgrade to a paid plan.

## Security Note

Your email address and EmailJS credentials are only used for sending contact form submissions. No sensitive information is exposed.