#Django Blog Application
This is a simple blog application built with Django, featuring user authentication, post management, and profile management. Users can create, read, update, and delete blog posts, manage their profiles, and browse posts made by other users.

##Features
User registration and authentication (login/logout)
Create, edit, delete blog posts
Profile management (including profile pictures)
Responsive design with Tailwind CSS
RESTful API endpoints (if applicable)
Dockerized environment for easy setup
Requirements
Python 3.x
Django 4.x (or the version you are using)
PostgreSQL or MySQL (if applicable, otherwise SQLite)
Docker (optional, if using Docker for setup)

##Requirements

Python 3.x
Django 4.x (or the version you are using)
PostgreSQL or MySQL (if applicable, otherwise SQLite)
Docker (optional, if using Docker for setup)

project6/
│
├── blogapp/
│   ├── models.py        # Defines models for the blog and user profiles
│   ├── views.py         # Contains the views for displaying and managing posts
│   ├── urls.py          # Routes for the blog app
│   └── forms.py         # Forms for user input
├── project6/
│   ├── settings.py      # Django settings file
│   ├── urls.py          # Main project URL configuration
│   └── wsgi.py          # WSGI application entry point
├── manage.py            # Django management command line utility
├── requirements.txt     # Project dependencies
├── Dockerfile           # Docker setup (if applicable)
├── docker-compose.yml   # Docker Compose configuration (if applicable)
├── .gitignore           # Git ignore file
└── db.sqlite3           # Database file (ignored in .gitignore if using SQLite)

##Cloning the Repository

git clone https://github.com/Abhicodes4/Blog_app.git
cd Blog_app

##Setting up a Virtual Environment

python -m venv venv
venv\Scripts\activate

##Installing Dependencies

pip install -r requirements.txt

##Database Setup
SQLite: By default, this project uses SQLite, so no additional setup is required.

PostgreSQL/MySQL: If using PostgreSQL or MySQL, update the DATABASES setting in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'your-db-name',
        'USER': 'your-db-user',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': '5432',  # or 3306 for MySQL
    }
}

##Migrating the Database

python manage.py migrate

##Creating a Superuser

python manage.py createsuperuser

##Running the Development Server

python manage.py runserver

Docker Setup (Optional)

docker-compose up --build

##API Documentation (if applicable)

python manage.py test




