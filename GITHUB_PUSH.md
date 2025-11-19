# 🔑 GitHub Push Instructions

Your local code is ready! Now you need to authenticate and push to GitHub.

## Step-by-Step Instructions

### 1. Get Your Personal Access Token

Since GitHub no longer accepts passwords for HTTPS, you need a Personal Access Token:

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "Max Fitness Deploy"
4. Select these scopes:
   - ✅ repo (Full control of private repositories)
   - ✅ admin:repo_hook (Full control of hooks)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)

### 2. Push Code to GitHub

Run this command in terminal:

```bash
cd /home/jack/work/maxgym
git push -u origin main
```

### 3. Enter Credentials

When prompted:
- **Username**: `mohith182007` (your GitHub username)
- **Password**: Paste the token you copied (NOT your GitHub password)

### 4. Verify

After push completes, check: https://github.com/mohith182007/Max-Fitness

You should see all your files there!

---

## ⚠️ Common Issues

**Error: "repository not found"**
- Check repository URL is correct
- Verify you have access to the repo

**Error: "Authentication failed"**
- Make sure you're using Personal Access Token (not password)
- Token must have 'repo' scope

**Error: "Permission denied"**
- Check your GitHub account permissions
- Verify the repository is yours

---

## Quick Reference

```bash
# Current setup:
# Remote: https://github.com/mohith182007/Max-Fitness.git
# Branch: main
# Ready to push: YES

# Push command:
git push -u origin main

# After push, check on GitHub:
# https://github.com/mohith182007/Max-Fitness
```

---

**Once pushed successfully, you can deploy on Vercel immediately!**
