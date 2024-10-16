# Django Blog Application

This is a simple blog application built with Django, featuring user authentication, post management, and profile management. Users can create, read, update, and delete blog posts, manage their profiles, and browse posts made by other users.

## Features
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

## Requirements

Python 3.x
Django 4.x (or the version you are using)
PostgreSQL or MySQL (if applicable, otherwise SQLite)
Docker (optional, if using Docker for setup)


## Cloning the Repository

git clone https://github.com/Abhicodes4/Blog_app.git

cd Blog_app

## Setting up a Virtual Environment

python -m venv venv
venv\Scripts\activate

## Installing Dependencies

pip install -r requirements.txt

## Database Setup
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

## Migrating the Database

python manage.py migrate

## Creating a Superuser

python manage.py createsuperuser

## Running the Development Server

python manage.py runserver

## Docker Setup (Optional)

docker-compose up --build

## API Documentation (if applicable)

python manage.py test




