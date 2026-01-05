# Deploy Django SGD Events to Render - Step by Step Guide

## Prerequisites
- GitHub account
- Render account (free tier available)
- Your project pushed to GitHub

---

## Step 1: Push Your Project to GitHub

### If you haven't initialized Git yet:
```bash
git init
git add .
git commit -m "Initial commit - ready for deployment"
```

### Create a new repository on GitHub:
1. Go to https://github.com/new
2. Create a repository named "Django-SGD" (or any name)
3. Don't initialize with README (your project already has files)

### Push your code:
```bash
git remote add origin https://github.com/YOUR_USERNAME/Django-SGD.git
git branch -M main
git push -u origin main
```

---

## Step 2: Sign Up for Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up using your GitHub account (recommended)
4. Authorize Render to access your GitHub repositories

---

## Step 3: Create a New Web Service

1. From Render Dashboard, click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Build and deploy from a Git repository"**
4. Click **"Connect"** next to your Django-SGD repository
   - If you don't see it, click "Configure account" to grant access

---

## Step 4: Configure Your Web Service

Fill in the following details:

### Basic Settings:
- **Name**: `sgd-events` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Runtime**: **Python 3**

### Build & Deploy Settings:
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn sgd_events.wsgi:application`

### Instance Type:
- Select **"Free"** (for prototypes)

---

## Step 5: Add Environment Variables

Scroll down to **"Environment Variables"** section and add:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | Click "Generate" or use a long random string |
| `DEBUG` | `False` |

---

## Step 6: Create PostgreSQL Database

1. Scroll down and click **"Advanced"**
2. Under "Add Database", click **"New Database"**
3. Configure:
   - **Name**: `sgd-events-db`
   - **Database Name**: `sgd_events`
   - **User**: `sgd_events_user`
   - **Region**: Same as your web service
   - **Instance Type**: Free

4. Click **"Create Database"**

---

## Step 7: Link Database to Web Service

Render will automatically:
- Create a `DATABASE_URL` environment variable
- Link it to your web service

---

## Step 8: Deploy!

1. Click **"Create Web Service"** button at the bottom
2. Render will start building your app (takes 5-10 minutes)
3. Watch the logs for any errors

### Build Process:
- ✅ Installing dependencies from requirements.txt
- ✅ Collecting static files
- ✅ Running database migrations
- ✅ Starting Gunicorn server

---

## Step 9: Access Your Website

Once deployment succeeds:
1. You'll see "Live" status with a green dot
2. Your URL will be: `https://sgd-events.onrender.com`
3. Click the URL to open your website!

---

## Troubleshooting

### If build fails:
- Check the logs in Render dashboard
- Ensure all files are pushed to GitHub
- Verify `build.sh` has execute permissions

### If website shows errors:
- Check environment variables are set correctly
- View logs: Dashboard → Your Service → Logs
- Ensure database migrations completed

### Database issues:
- Verify DATABASE_URL is set automatically
- Check PostgreSQL database is running

---

## Important Notes

### Free Tier Limitations:
- **Web service spins down after 15 minutes of inactivity**
- First request after downtime takes 30-60 seconds (cold start)
- 750 hours/month free (enough for 1 service)
- Database: 90 days free, then $7/month

### Keep Your App Alive (Optional):
- Use UptimeRobot (free) to ping your URL every 5 minutes
- Or upgrade to paid tier ($7/month) for always-on

---

## Updating Your App

After making changes:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

Render automatically redeploys when you push to GitHub! 🚀

---

## Next Steps

1. ✅ Custom domain (optional): Dashboard → Settings → Custom Domain
2. ✅ Enable HTTPS (automatic on Render)
3. ✅ Set up monitoring and alerts
4. ✅ Configure backups for production

---

## Support

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/

---

**Your Django app is now live on the internet! 🎉**
