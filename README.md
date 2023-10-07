# Meduzzen Internship Project

Welcome to the Meduzzen Internship Project repository. This project is a part of the internship process at Meduzzen, aiming to demonstrate proficiency in web development using specific technologies.

## 🛠 Technologies Used

- **Backend**: 
  - ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white)
  - ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=Django&logoColor=white)
  
- **Frontend**: 
  - ![Vue.js](https://img.shields.io/badge/-Vue.js-4FC08D?style=flat-square&logo=Vue.js&logoColor=white)

## 📖 Project Overview

This project is designed to showcase the ability to build a full-stack application using Django for the backend and Vue.js for the frontend. As a part of the Meduzzen internship, this project will cover various aspects of web development, from setting up the environment to deploying the final application.

## 🚀 Running the Application

1. **Install the required packages:**:
   ```bash
   pip install -r requirements.txt

2. **Copy `.env.example` to `.env`:**
   ```bash
   cp .env.example .env
Or rename, if you prefer.

3. **Run the Django development server:**:
    ```bash
    ./manage.py runserver
**Note:** Django hot-reloading upon file changes is built-in, so there's no need for additional setup for this feature.

## 🐳 Run with Docker 
**Requirements**

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

**To start** Docker container, run the following command:

```sh
docker-compose up
```

Open [http://localhost:8000](http://localhost:8000) in a web browser

**Note:** The `start.sh` script is executed within the Docker container. This script is responsible for applying any pending db **migrations** and starting the Django application.

## 🗃 Database Migrations

### Local:
1. **Create Migrations:**
   ```bash
   ./manage.py makemigrations
2. **Apply Migrations:**
    ```bash
    ./manage.py migrate
### Docker:
1. **Create Migrations:**
    ```bash
    docker-compose exec django ./manage.py makemigrations
2. **Apply Migrations:**
    ```bash
    docker-compose exec django ./manage.py migrate
## 🧪 Running Tests
In your local Python environment:

    ./manage.py test

Inside Docker container:

    docker-compose run django python manage.py test

## 🗄 Logging

Logging is set up to output messages to the console, with a logging level of `DEBUG` for development purposes. Please refer to the `settings.py` for detailed logging configurations.

**NOTE:** Messages of `WARNING` level and above are additionally recorded to `warning.log` located in the `/logs/` directory.

## 🔑 Auth0 Login / Registration

Log in or register http://localhost:8000/auth/login/auth0/ You can use existing credentials or create a new account, with the option to use **Google** or **Facebook** for login.

## ℹ️ API Usage

### 🧑‍💻 User Registration

To register a new user, use the following `curl` command:

```sh
curl -X POST http://localhost:8000/api/users/ \
-H "Content-Type: application/json" \
-d '{"username": "new_user", "password": "new_password", "email": "new_user@example.com"}'
```
### 🔒 User Login
To login a user and receive an authentication token, use the following curl command:
```sh 
curl -X POST http://localhost:8000/auth/token/login/ \
-H "Content-Type: application/json" \
-d '{"username": "exampleuser", "password": "examplepassword"}'
```

### 🚪 User Logout
To logout a user and invalidate the user's token, use the following curl command:
```sh 
curl -X POST http://localhost:8000/auth/token/logout/ \
-H "Content-Type: application/json" \
-H "Authorization: Token YOUR_TOKEN"
```
Replace YOUR_TOKEN with the actual token of the user you want to log out.

### 🔄 Password and Username Reset
To reset a user's password, use the following curl command:
```sh
curl -X POST http://localhost:8000/auth/users/reset_password/ \
-H "Content-Type: application/json" \
-d '{"email": "example@email.com"}'
```
To reset a user's username, use the following curl command:
```sh
curl -X POST http://localhost:8000/auth/users/reset_username/ \
-H "Content-Type: application/json" \
-d '{"email": "example@email.com"}'

```

### 📧 Email Activation
To activate a user, use the following curl command:
```sh
curl -X POST http://localhost:8000/auth/users/activation/ \
-H "Content-Type: application/json" \
-d '{"uid": "UID", "token": "TOKEN"}'
```
Replace UID with the user's UID and TOKEN with the actual token received in the email.
## 🤝 Contribution

This project is solely for the internship purpose. However, feedback and suggestions are always welcome.
