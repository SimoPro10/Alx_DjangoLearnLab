# E-commerce Product API

This is a Django-based RESTful API for managing products in an e-commerce platform. The API provides endpoints for creating, reading, updating, and deleting product data, and integrates user authentication.

## Features

- CRUD operations for products
- User authentication using custom user model
- Token-based authentication for API security
- Database integration using SQLite or MySQL

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10+
- pip (Python package installer)
- MySQL server (if using MySQL for database)
- Git (optional, for version control)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd e-commerce_product_api
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database:**
   - If using MySQL, update the `DATABASES` setting in `settings.py` with your database credentials.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': '<database_name>',
           'USER': '<username>',
           'PASSWORD': '<password>',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

## Usage

### Endpoints

#### Authentication
- **POST /api/token/** - Obtain authentication tokens
- **POST /api/token/refresh/** - Refresh authentication tokens

#### Products
- **GET /api/products/** - List all products
- **POST /api/products/** - Create a new product (Admin only)
- **GET /api/products/<id>/** - Retrieve a single product
- **PUT /api/products/<id>/** - Update a product (Admin only)
- **DELETE /api/products/<id>/** - Delete a product (Admin only)

## Environment Variables

Set the following environment variables in a `.env` file or in your environment:

```env
SECRET_KEY=<your_django_secret_key>
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_NAME=<database_name>
DATABASE_USER=<database_user>
DATABASE_PASSWORD=<database_password>
```

## Deployment

1. Configure `ALLOWED_HOSTS` in `settings.py`.
2. Use a production-ready web server like Gunicorn with Nginx.
3. Set up a production database and update the `DATABASES` setting accordingly.
4. Use HTTPS for secure connections.