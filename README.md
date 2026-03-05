# Yeab Pharmaceuticals One Member PLC - Company Profile Website

A professional, modern company profile website for Yeab Pharmaceuticals One Member PLC, built with Django and featuring a medical-corporate theme with advanced animations and responsive design.

## 🚀 Features

### Core Features
- **5 Complete Pages**: Home, About Us, Services, Blog (Dynamic), Contact Us
- **Modern Design**: Medical-corporate theme with professional aesthetics
- **Responsive Design**: Mobile-first approach, optimized for all devices
- **Advanced Animations**: AOS (Animate On Scroll), GSAP-style effects, parallax scrolling
- **Dynamic Blog System**: Full Django ORM integration with admin panel
- **Contact Form**: Functional with validation and email notifications
- **SEO Optimized**: Meta tags, semantic HTML5, clean URLs

### Design Elements
- **Color Scheme**: Deep Medical Blue (#0A1F44), Emerald Green (#0F9D58)
- **Typography**: Google Fonts (Poppins)
- **Animations**: Fade-in, slide-up, hover effects, parallax scrolling
- **Components**: Glassmorphism cards, smooth transitions, micro-interactions
- **Layout**: Clean spacing, premium feel, international standard

### Technical Features
- **Backend**: Django 4.2.7 with Python
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Framework**: Bootstrap 5 for responsive grid
- **Animations**: AOS library, custom CSS animations
- **Database**: SQLite (development ready)
- **Admin Panel**: Full CRUD operations for blog and contact messages

## 📁 Project Structure

```
yeab/
├── manage.py
├── requirements.txt
├── README.md
├── yeab_pharma/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── core/
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── services.html
│   │   └── contact.html
│   └── blog/
│       ├── blog_list.html
│       └── post_detail.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── (placeholder images)
└── media/
    └── (user uploads)
```

## 🛠 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone and Setup Environment
```bash
# Navigate to project directory
cd yeab

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Django Settings
1. Open `yeab_pharma/settings.py`
2. Update the following settings:
   ```python
   SECRET_KEY = 'your-unique-secret-key-here'
   DEBUG = False  # Set to False in production
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   
   # Email configuration (for contact form)
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'  # Your email provider
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
   ADMIN_EMAIL = 'admin@yourdomain.com'
   ```

### Step 4: Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Step 5: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the website.

## 📝 Usage Guide

### Admin Panel Access
1. Navigate to `/admin/`
2. Login with superuser credentials
3. Manage blog posts, categories, and contact messages

### Blog Management
1. **Create Categories**: Add blog categories in admin panel
2. **Write Posts**: Create and publish blog posts with rich content
3. **Upload Images**: Add featured images to blog posts
4. **SEO Optimization**: Add meta descriptions and keywords

### Contact Form
- Messages are saved to database
- Email notifications sent to admin (if configured)
- Form validation on both client and server side

### Customization
- **Colors**: Modify CSS variables in `static/css/style.css`
- **Fonts**: Update Google Fonts import in base template
- **Content**: Edit HTML templates for text changes
- **Images**: Replace placeholder images in `static/images/`

## 🎨 Design Customization

### Color Scheme
Update CSS variables in `style.css`:
```css
:root {
    --primary-color: #0A1F44;    /* Deep Medical Blue */
    --secondary-color: #0F9D58;   /* Emerald Green */
    --accent-color: #ffffff;     /* White */
}
```

### Typography
Google Fonts (Poppins) can be changed in `base.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Animations
- AOS settings in `main.js`
- Custom CSS animations in `style.css`
- Animation delays controlled via data attributes

## 📱 Responsive Design

The website is fully responsive with breakpoints:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: < 768px

### Mobile Features
- Hamburger navigation menu
- Touch-friendly buttons and links
- Optimized image sizes
- Smooth mobile animations

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Set up production database (PostgreSQL recommended)
4. Configure static files serving
5. Set up email backend
6. Enable HTTPS

### Static Files
```bash
# For production
python manage.py collectstatic --noinput
```

### Environment Variables
Use environment variables for sensitive data:
```bash
export SECRET_KEY='your-secret-key'
export DATABASE_URL='your-database-url'
export EMAIL_HOST='your-email-host'
```

## 🔧 Maintenance

### Regular Tasks
- Update Django and dependencies
- Backup database regularly
- Monitor contact form submissions
- Update blog content
- Check for security updates

### Performance Optimization
- Enable browser caching
- Compress images
- Minify CSS/JS
- Use CDN for static assets
- Enable Gzip compression

## 📞 Support

For technical support or questions:
- Email: info@yeabpharma.com
- Phone: +251 911 234 567

## 📄 License

This project is proprietary to Yeab Pharmaceuticals One Member PLC.

## 🌟 Features Highlight

### Homepage
- Cinematic hero section with parallax effects
- Service preview cards with hover animations
- Latest blog posts integration
- Company statistics with counter animations
- Call-to-action sections

### About Page
- Company timeline with animated milestones
- Mission and vision sections
- Core values with icon cards
- Director message section
- Company statistics

### Services Page
- Detailed service descriptions
- Process workflow visualization
- Product categories showcase
- Quality assurance section

### Blog System
- Dynamic blog post management
- Category filtering
- Search functionality
- Pagination
- Social sharing integration
- Related posts suggestions

### Contact Page
- Interactive contact form
- Google Maps integration
- FAQ accordion section
- Multiple contact methods
- Social media links

## 🎯 SEO Features

- Semantic HTML5 structure
- Meta tags optimization
- Open Graph tags
- Twitter Card support
- XML sitemap ready
- Robots.txt configuration
- Clean URL structure
- Image alt tags
- Heading hierarchy

## 🔒 Security Features

- CSRF protection
- XSS protection
- SQL injection prevention
- Secure form handling
- Admin panel protection
- Environment variable usage
- HTTPS ready

---

**Built with ❤️ for Yeab Pharmaceuticals One Member PLC**
