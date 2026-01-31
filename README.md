![Django E-commerce](https://res.cloudinary.com/practicaldev/image/fetch/s--sq_zyTgt--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/igudmgdrvenbhmf5n6wl.png)

![Built with Love](https://forthebadge.com/images/badges/built-with-love.svg) 
![HTML](https://forthebadge.com/images/badges/uses-html.svg) 
![CSS](https://forthebadge.com/images/badges/uses-css.svg) 
![Git](https://forthebadge.com/images/badges/uses-git.svg) 
![JavaScript](https://forthebadge.com/images/badges/uses-js.svg) 
![Python](https://forthebadge.com/images/badges/made-with-python.svg)  
![Built by Developers](https://forthebadge.com/images/badges/built-by-developers.svg)

# 🥬 VegeFoods - Django E-commerce Website

A full-featured e-commerce platform for selling fresh vegetables and organic products, built with Django and modern web technologies.

## 📋 Table of Contents

- [About Django](#about-django)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Linux/MacOS Setup](#linuxmacos-setup)
  - [Windows Setup](#windows-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## 🐍 About Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source.

## ✨ Features

- 🛒 **Shopping Cart** - Add, update, and remove products
- ❤️ **Wishlist** - Save favorite products for later
- 🔍 **Product Search & Filter** - Easy product discovery
- 👤 **User Authentication** - Register, login, and profile management
- 💳 **Checkout Process** - Secure order placement
- 📱 **Responsive Design** - Works on all devices
- 🎨 **Modern UI** - Clean and intuitive interface
- 📊 **Admin Dashboard** - Manage products, orders, and users
- 📧 **Email Notifications** - Order confirmations and updates
- 💰 **Payment Integration** - Secure payment processing

## 🛠️ Tech Stack

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Authentication:** Django Authentication System
- **Static Files:** Django Static Files
- **Media Storage:** Local/Cloudinary

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Linux/MacOS Setup

1. **Clone the repository**
```bash
   cd Vege-Foods-Store
```

2. **Create and activate virtual environment**
```bash
   python3 -m venv env
   source env/bin/activate
```

3. **Install required packages**
```bash
   pip install -r requirements.txt
```

4. **Configure environment variables** (Optional)
```bash
   cp .env.example .env
   # Edit .env file with your configurations
```

5. **Run database migrations**
```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
```

6. **Create superuser account**
```bash
   python3 manage.py createsuperuser
```

7. **Collect static files**
```bash
   python3 manage.py collectstatic
```

8. **Load sample data** (Optional)
```bash
   python3 manage.py loaddata fixtures/sample_data.json
```

9. **Run the development server**
```bash
   python3 manage.py runserver
```

10. **Access the application**
    - Website: http://127.0.0.1:8000/
    - Admin Panel: http://127.0.0.1:8000/admin/

### Windows Setup

1. **Clone the repository**
```cmd
   cd Vege-Foods-Store
```

2. **Create and activate virtual environment**
```cmd
   python -m venv env
   env\Scripts\activate
```

3. **Install required packages**
```cmd
   pip install -r requirements.txt
```

4. **Run migrations**
```cmd
   python manage.py makemigrations
   python manage.py migrate
```

5. **Create superuser**
```cmd
   python manage.py createsuperuser
```

6. **Run the server**
```cmd
   python manage.py runserver
```

## 🚀 Usage

### For Customers

1. Browse products on the home page
2. Add products to cart or wishlist
3. Register/Login to your account
4. Proceed to checkout
5. Complete your order

### For Administrators

1. Access the admin panel at `/admin`
2. Login with superuser credentials
3. Manage products, categories, orders, and users
4. View sales reports and analytics

## 📁 Project Structure
```
Vege-Foods-Store/
├── core/                   # Main app
├── products/              # Products app
├── cart/                  # Shopping cart app
├── orders/                # Orders management
├── users/                 # User authentication
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
├── templates/             # HTML templates
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 📸 Screenshots

<!-- Add your screenshots here -->
*Coming soon...*

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Smartvegnet**

- Email: Smartvegnet@gmail.com

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- All contributors who helped improve this project

## 📞 Support

If you encounter any issues or have questions, please:

1. Create a new issue if your problem isn't already listed
2. Contact the author via email

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ by Smartvegnet