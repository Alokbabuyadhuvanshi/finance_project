# Finance Management System

A simple and clean **Finance Management Backend + UI** built using **Django**.
This project allows users to manage their income and expenses with basic analytics.

---

## 🚀 Features

### 🔐 Authentication

* User Registration
* User Login / Logout
* Session-based authentication

### 💵 Financial Records

* Add income and expense records
* Update records
* Delete records
* View all records

### 🔍 Filtering

* Filter by:

  * Type (Income / Expense)
  * Category
  * Date range

### 📊 Analytics Dashboard

* Total Income
* Total Expenses
* Current Balance
* Category-wise breakdown
* Monthly totals
* Recent activity

### 🛠 Admin Panel

* View all users
* View user-wise financial records (inline)
* Filters, search, and sorting enabled

---

## 🧱 Tech Stack

* Backend: **Django**
* Database: **SQLite (default)**
* Frontend: **Django Templates (HTML)**
* Authentication: **Django built-in auth system**

---

## 📁 Project Structure

```id="fullstruct"
finance_project/
│
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   
├── finance_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── form.html
│   ├── list.html
│
├── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd finance_project
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install django
```

### 4. Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```
python manage.py createsuperuser
```

### 6. Run Server

```
python manage.py runserver
```

---

## 🔒 Authentication Notes

* Uses Django’s built-in authentication
* Custom user model (`core.User`)
* Each user can only access their own records

---

## ✅ Validations

* Login:

  * Invalid credentials handling
* Registration:

  * Duplicate username check
  * Password validation
* Forms:

  * Invalid input handling with error messages

---

## 📊 Admin Features

* Inline records inside User view
* Filters:
  * Type
  * Category
  * Date
* Search functionality
* Sorted by latest records

---

## 🎯 Future Improvements

* Add charts (income vs expense)
* Export data (CSV/Excel)
* Budget tracking
* REST API support
* Better UI (Bootstrap)
* AI boot

---

## 👨‍💻 Author

**Alok Babu**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
