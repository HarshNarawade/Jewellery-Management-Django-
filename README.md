# 🛠️ Jewelry Customization Platform

A powerful Django-based web application supporting customizable jewelry orders with role-based permissions.

---

## 🚀 Project Overview

This project is designed to handle jewelry customization workflows,
from customers placing orders to store managers and factory managers overseeing production.
The platform ensures smooth user management, order tracking, and role-specific permissions.

---

## 📦 Setup Instructions

### 🛠️ Prerequisites

Ensure you have the following installed:

- **Python 3.10+**
- **MySQL**

---

### 💻 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install project dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   ```bash
   cp .env.example .env
   # Fill in the following details:
   ```

   **Example .env file:**

   ```env
   DB_NAME=DB_NAME
   DB_USER=DB_USER
   DB_PASSWORD=DB_PASSWORD
   DB_HOST=localhost
   DB_PORT=3306
   ```

   Replace this in ur settings.py 
   ```bash
     DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.mysql",
          "NAME": env("DB_NAME"),
          "USER": env("DB_USER"),
          "PASSWORD": env("DB_PASSWORD"),
          "HOST": env("DB_HOST", default="localhost"),
          "PORT": env("DB_PORT", default="3306"),
          "OPTIONS": {
              "charset": "utf8mb4",
          },
      }
    }
   ```

5. **Set up MySQL database:**

   ```bash
   mysql -u root -p
   CREATE DATABASE jewels;
   GRANT ALL PRIVILEGES ON jewels.* TO 'harsh'@'localhost' IDENTIFIED BY 'harsh';
   FLUSH PRIVILEGES;
   EXIT;
   ```

6. **Apply database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a Django superuser:**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run predefined group setup script:**

   ```bash
   python manage.py configure_groups
   ```

9. **Collect static files:**

   ```bash
   python manage.py collectstatic
   ```

10. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

---

## 🔥 Functionality Overview

### 🧑‍💼 User Roles

- **Customer:**

  - View past orders.
  - Customize jewelry.
  - View bills.

- **Store Manager:**

  - Add, view, update, and delete users.
  - Manage customer orders.
  - Monitor customizations and track production costs.

- **Factory Manager:**

  - View and update assigned orders.
  - Access production details and cost breakdowns

---

### 📌 Key Features

- **Custom User Model:** Supports three distinct user roles with different permission sets.
- 
- **Role-Based Permissions:** Each user role has predefined access control managed via `configure_groups`.
- 
- **Order Management:** Users can view, add, update, or delete orders based on permissions.
- 
- **MySQL Integration:** Fully compatible with MySQL databases.
- 
- **Environment Configuration:** `.env` file to easily manage database credentials and sensitive data.
- 
- **Admin Panel:** Supports full management of users, orders, and permissions.
- 
- **Static File Management:** Collect and serve static files seamlessly.
- 
- **Django Tables2 Integration:**
  - View orders in a clean, sortable, paginated table.
  - Search orders by customer, date, or customization details.
  - Export orders to Excel, CSV, or other formats.
  - Import orders from pre-formatted files.
  - Download a sample file template for easier importing.

- **PDF Generation:**
  - Generate PDFs of jewelry order details.
  - Export order invoices and bills in a printable format.

---


**✨ Setup complete! Happy building! ✨**

