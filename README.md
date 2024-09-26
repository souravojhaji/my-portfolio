# My Portfolio

Welcome to my portfolio project! This application showcases my skills, projects, and experience. It is built with a Nuxt.js frontend and a Django backend, using PostgreSQL as the database.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Running the Project](#running-the-project)

## Features
- **Responsive Design:** Accessible on all devices.
- **Dynamic Content:** Fetches and displays projects, skills, and contact information from the backend.
- **User Authentication:** Secure access to certain features (if applicable).

## Technologies
- **Frontend:** Nuxt.js
- **Backend:** Django
- **Database:** PostgreSQL
- **Others:** Docker, Virtual Environment

## Setup
To set up the project, follow these steps: Clone the Repository: 
`git clone https://github.com/souravojhaji/my-portfolio.git` 

and navigate to the backend directory: `cd my-portfolio/backend`.

 Create a Virtual Environment: `python -m venv venv` 
 
 and activate it with `source venv/bin/activate` (use `venv\Scripts\activate` on Windows).

 Install Dependencies: `pip install -r requirements.txt`. 
 
 Set Up PostgreSQL by creating a database and user, and updating the `settings.py` file in your Django project with your database credentials. 
 
 Run Migrations with `python manage.py migrate`. Create a Superuser (optional) using `python manage.py createsuperuser`. 
 
 Finally, Run the Django Server with `python manage.py runserver`. 

For the Frontend Setup, navigate to the frontend directory with `cd ../frontend`. 

Install Dependencies using `npm install`, and Run the Nuxt.js Development Server with `npm run dev`.

## Running the Project
To run the project, start the Django Backend: make sure you're in the `backend` directory and the virtual environment is activated, then run `python manage.py runserver`. Next, start the Nuxt.js Frontend by navigating to the `frontend` directory with `cd frontend` and run `npm run dev`. Finally, open your browser and navigate to `http://localhost:3000` to view your portfolio.

