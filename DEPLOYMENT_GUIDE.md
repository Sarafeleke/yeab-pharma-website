# 🚀 Deployment Guide - Yeab Pharmaceuticals Website

This guide will help you deploy the Yeab Pharmaceuticals website using **Render** for the Django backend and **Vercel** for the static frontend.

## 📋 Prerequisites

- GitHub account with the project repository
- Render account (free tier available)
- Vercel account (free tier available)
- Email credentials for contact form (optional)

---

## 🎯 Deployment Strategy

### Backend (Render)
- **Platform**: Render Web Service
- **Database**: PostgreSQL (Render's free tier)
- **Framework**: Django 4.2.7
- **URL**: `https://yeab-pharma-backend.onrender.com`

### Frontend (Vercel)
- **Platform**: Vercel Static Site
- **Purpose**: Serve static files and proxy API requests
- **URL**: `https://yeab-pharma-frontend.vercel.app`

---

## 🔧 Step 1: Deploy Backend on Render

### 1.1 Prepare Repository
Ensure your repository is pushed to GitHub with all the deployment files:
- `render.yaml` - Render configuration
- `Procfile` - Process configuration
- `requirements.txt` - Python dependencies

### 1.2 Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Verify your email

### 1.3 Deploy Web Service
1. Click **"New +"** → **"Web Service"**
2. Select your GitHub repository
3. Configure the service:
   - **Name**: `yeab-pharma-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python manage.py runserver 0.0.0.0:$PORT`
   - **Instance Type**: `Free`

### 1.4 Configure Environment Variables
Add these environment variables in Render dashboard:

```bash
DEBUG=False
SECRET_KEY=your-generated-secret-key
DATABASE_URL=postgresql://username:password@host:port/database
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
ADMIN_EMAIL=admin@yeabpharma.com
```

### 1.5 Create Database
1. Go to **"New +"** → **"PostgreSQL"**
2. **Name**: `yeab-pharma-db`
3. **Database Name**: `yeab_pharma`
4. **User**: `yeab_user`
5. **Plan**: Free

### 1.6 Run Migrations
After deployment, access your service and run:
```bash
# Connect to service shell and run:
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

## 🎨 Step 2: Deploy Frontend on Vercel

### 2.1 Create Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Verify your email

### 2.2 Import Project
1. Click **"Add New..."** → **"Project"**
2. Select your GitHub repository
3. Configure settings:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Build Command**: `npm run build`
   - **Output Directory**: `static`

### 2.3 Configure Environment Variables
Add these environment variables:
```bash
BACKEND_URL=https://yeab-pharma-backend.onrender.com
```

### 2.4 Update vercel.json (if needed)
The `vercel.json` file is already configured to:
- Serve static files from `/static/`
- Proxy API requests to Render backend
- Handle media files through backend
- Route all requests to Django backend

---

## 🔗 Step 3: Connect Frontend and Backend

### 3.1 Update Django Settings
The `settings.py` is already configured to:
- Accept requests from Vercel frontend
- Handle CORS properly
- Use environment variables

### 3.2 Test Connection
1. Visit your Vercel URL
2. Test all pages and functionality
3. Submit contact form to test email
4. Access admin panel: `/django-admin/`

---

## 📧 Step 4: Configure Email (Optional)

### 4.1 Gmail Setup
1. Enable 2-factor authentication on Gmail
2. Generate App Password:
   - Go to Google Account → Security
   - Enable 2-Step Verification
   - Generate App Password
   - Use this password in `EMAIL_HOST_PASSWORD`

### 4.2 Update Environment Variables
In Render dashboard, update:
```bash
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-16-digit-app-password
DEFAULT_FROM_EMAIL=your-gmail@gmail.com
```

---

## 🔄 Step 5: Post-Deployment Tasks

### 5.1 Create Superuser
Access your Render service shell and run:
```bash
python manage.py createsuperuser
```

### 5.2 Load Initial Data
1. Access admin panel: `https://yeab-pharma-backend.onrender.com/django-admin/`
2. Create blog categories
3. Add sample blog posts
4. Add products
5. Configure site information

### 5.3 Test All Features
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Blog system functions
- [ ] Contact form sends emails
- [ ] Admin panel accessible
- [ ] Images upload correctly
- [ ] Mobile responsive design

---

## 🛠️ Troubleshooting

### Common Issues

#### 1. Database Connection Error
```bash
# Check DATABASE_URL format
postgresql://username:password@host:port/database
```

#### 2. CSRF Token Error
Ensure your domains are in `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`.

#### 3. Static Files Not Loading
Run `collectstatic` command:
```bash
python manage.py collectstatic --noinput
```

#### 4. Email Not Sending
- Check email credentials
- Verify App Password for Gmail
- Check spam folder

#### 5. CORS Issues
Ensure frontend URL is in `CSRF_TRUSTED_ORIGINS`.

### Debug Mode
To enable debug mode temporarily:
```bash
DEBUG=True
```

---

## 📊 Monitoring

### Render Dashboard
- Monitor web service logs
- Check database performance
- View deployment history

### Vercel Dashboard
- Monitor static file serving
- View build logs
- Check analytics

---

## 💰 Cost Breakdown (Free Tier)

### Render (Free)
- Web Service: 750 hours/month
- PostgreSQL: 256MB RAM, 90GB storage
- Bandwidth: 100GB/month

### Vercel (Free)
- Static hosting: Unlimited bandwidth
- Build time: 6,000 minutes/month
- Functions: 100GB bandwidth/month

---

## 🔒 Security Considerations

1. **Environment Variables**: Never commit secrets to Git
2. **HTTPS**: Both platforms provide SSL certificates
3. **Database**: Use strong password for PostgreSQL
4. **Admin Panel**: Use strong superuser credentials
5. **Email**: Use App Passwords, not regular passwords

---

## 🚀 Going Live

### Custom Domains
1. **Render**: Add custom domain in service settings
2. **Vercel**: Add custom domain in project settings
3. Update DNS records as instructed

### Performance Optimization
1. Enable caching on Vercel
2. Optimize images before upload
3. Use CDN for static assets
4. Monitor database queries

---

## 📞 Support

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Django Documentation**: [docs.djangoproject.com](https://docs.djangoproject.com)

---

**🎉 Congratulations! Your Yeab Pharmaceuticals website is now live!**
