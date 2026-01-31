# 🥦 Vegetables Store (All-in-One)

A **Django-based web application** for managing and selling vegetables online.
Beginner-friendly CRUD project with **responsive UI**, image upload, and basic currency conversion.

---

## 📌 Project Overview

**Vegetables Store** lets users view, add, update, and delete vegetables.
Built for learning Django fundamentals: models, views, templates, static files, media handling, and responsiveness.

---

## ✨ Features

* 🥕 View list of vegetables
* ➕ Add / ✏️ Update / ❌ Delete vegetables (CRUD)
* 🖼️ Image upload using `ImageField`
* 💱 Currency conversion (details below)
* 📱 Fully responsive UI (mobile / tablet / desktop)
* ⚙️ Django backend with SQLite

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, SCSS, JavaScript, Bootstrap 5
* **Database:** SQLite (default)

---

## 📂 Project Structure

```
Vegetables-store/
│
├── shop/                 # Django app
├── static/               # CSS, JS, images
├── templates/            # HTML templates
├── manage.py             # Django manager
├── requirements.txt      # Dependencies
├── CURRENCY_CONVERSION.md
└── README.md
```

---

## ⚙️ Installation & Setup (ONE-PAGE COMMAND LIST)

> **Windows (PowerShell / VS Code Terminal)**

```powershell
# 1. Go to project folder
cd D:\Cybotronics\Vegetables-store

# 2. Check Python
python --version

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
venv\Scripts\activate

# 5. Ensure pip + upgrade
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# 6. Install dependencies
python -m pip install -r requirements.txt

# 7. Install Pillow (required for ImageField)
python -m pip install Pillow

# 8. Make migrations
python manage.py makemigrations

# 9. Apply migrations
python manage.py migrate

# 10. Create admin user (optional)
python manage.py createsuperuser

# 11. Run server
python manage.py runserver
```

🌐 Open in browser:

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
```

---

## 📱 Responsive Design (All-in-One)

### ✅ Bootstrap (add once in `base.html`)

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

### ✅ Responsive Navbar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-success">
  <div class="container">
    <a class="navbar-brand" href="#">Vegetables Store</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navMenu">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Shop</a></li>
      </ul>
    </div>
  </div>
</nav>
```

### ✅ Responsive Grid (Products)

```html
<div class="container">
  <div class="row">
    <div class="col-lg-4 col-md-6 col-sm-12 mb-4">
      <!-- Product Card -->
    </div>
  </div>
</div>
```

### ✅ Responsive Images

```html
<img src="{{ product.photo.url }}" class="img-fluid rounded" alt="product">
```

### ✅ Responsive Forms

```html
<div class="container">
  <div class="row justify-content-center">
    <div class="col-md-6 col-sm-12">
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button class="btn btn-success w-100">Submit</button>
      </form>
    </div>
  </div>
</div>
```

### ✅ Media Queries (optional)

```css
@media (max-width: 768px) {
  h1 { font-size: 24px; }
  .product-card { margin-bottom: 20px; }
}
```

---

## 💱 Currency Conversion

See detailed logic in:

```
CURRENCY_CONVERSION.md
```

---

## 🎯 Use Case

* Academic / College project
* Django learning (CRUD + media + responsive UI)
* Beginner-friendly

---

## 👩‍💻 Author

**Utkarsha Desai**

---

## 📜 License

Educational and learning purposes only.

---

## ⭐ Future Improvements

* User authentication
* Cart & checkout
* Payment gateway
* Cloud deployment
* More responsive polish
