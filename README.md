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
2. **Run the Django development server:**:
    ```bash
    ./manage.py runserver
**Note:** Django 4.2.5, hot-reloading upon file changes is built-in, so there's no need for additional setup for this feature.

## 🐳 Run with Docker 
**Requirements**

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

**To start** Docker container, run the following command:

```sh
docker-compose up
```

Open [http://localhost:8000](http://localhost:8000) in a web browser

## 🧪 Running Tests
In your local Python environment:

    ./manage.py test

Inside Docker container:

    docker-compose run django python manage.py test

## 🤝 Contribution

This project is solely for the internship purpose. However, feedback and suggestions are always welcome.
