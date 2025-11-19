# 🚀 DEPLOYMENT GUIDE - MAX FITNESS

Your code is ready to push to GitHub and deploy on Vercel!

## 📋 Prerequisites

1. **GitHub Account** - https://github.com (create if you don't have)
2. **Vercel Account** - https://vercel.com (sign up with GitHub)

---

## 🔄 Step 1: Push to GitHub

### Option A: Using HTTPS (Easier)

```bash
cd /home/jack/work/maxgym

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/mohith182007/Max-Fitness.git

# Rename branch to main (Vercel prefers main)
git branch -M main

# Push to GitHub
git push -u origin main
```

**When prompted:**
- Username: `your-github-username`
- Password: Use a **Personal Access Token** (not your password)
  - Generate at: https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Select scopes: `repo`, `admin:repo_hook`
  - Copy and paste the token as password

---

## 🌐 Step 2: Deploy on Vercel

### Quick Deploy Method (Recommended)

1. Go to https://vercel.com
2. Click **"New Project"**
3. Click **"Import Git Repository"**
4. Paste: `https://github.com/mohith182007/Max-Fitness.git`
5. Click **"Import"**
6. Framework: Select **"Other"** (it's a static site)
7. Build Command: Leave empty
8. Output Directory: Leave empty
9. Click **"Deploy"**

### That's it! 🎉

Your site will be live at: `https://max-fitness.vercel.app` (or custom domain)

---

## 📂 Project Structure

```
max-fitness/
├── index.html          # Main HTML file
├── styles.css          # All styling (responsive)
├── script.js           # Interactive features
├── file.enc            # Gym image (background)
├── README.md           # Documentation
├── vercel.json         # Vercel config
├── .gitignore          # Git ignore rules
└── .git/               # Git repository
```

---

## ✨ Features Deployed

✅ Black & Red Professional Theme
✅ Fully Responsive Design
✅ Dynamic Hero Section with Background Image
✅ Facilities Showcase (Cardio, Strength, Personal Training, Nutrition)
✅ Location Information (Bengaluru)
✅ Contact Phone: +91 94825 07769
✅ Operating Hours: Mon-Sat 5AM-10PM, Sun 7AM-7PM
✅ Dual Membership Plans:
   - Cardio + Gym Access
   - Gym Access Only
✅ 4 Duration Options (1 Month, 3 Months, 6 Months, 1 Year)
✅ Smooth Animations & Interactive Elements
✅ Contact Form Ready for Email Integration
✅ Mobile-Friendly with Hamburger Menu

---

## 🔗 Environment Variables (Optional)

If you want to add email functionality, create a `.env` file:

```
FORMSPREE_ID=your_formspree_form_id
```

Then update the form in `index.html`:
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

---

## 🎯 Next Steps After Deployment

1. **Custom Domain** (Optional)
   - Vercel → Project Settings → Domains
   - Add your custom domain (e.g., maxfitness.com)

2. **Email Integration** (Optional)
   - Sign up at https://formspree.io
   - Update contact form with Formspree endpoint
   - Receive inquiries directly in your email

3. **Monitoring**
   - Vercel Dashboard shows analytics and errors
   - Custom domains can have SSL certificates

4. **Updates**
   ```bash
   # Make changes locally, then:
   git add .
   git commit -m "Description of changes"
   git push origin main
   # Vercel auto-deploys on push!
   ```

---

## 📞 Support Files

- **README.md** - Contains full project documentation
- **vercel.json** - Deployment configuration
- **.gitignore** - Files to exclude from git

---

## ✅ Checklist Before Pushing

- [x] All HTML files present
- [x] CSS files included
- [x] JavaScript files included
- [x] Image file (file.enc) included
- [x] README.md documentation
- [x] vercel.json configuration
- [x] .gitignore created
- [x] Git initialized and committed

---

**Ready to Deploy? Follow Step 1 and 2 above!** 🚀

For any issues: https://vercel.com/docs/platform/deployments
