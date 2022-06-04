#  EC530 Final Project - Healthcare Doctor and Patient Portal

## Overview
This is a Web app built using Flask in Python and SQLite. The objective is to provide a patient and doctor portal where patients can upload the readings from their devices and doctors can monitor the information for their patients. There are two main roles, Doctor and Patient, with plans to add a third Administrator role in a future version of the app.

## User Stories

### Patient
Patients are able to add and delete measurements for:
- Height and Weight
- Temperature
- Blood Pressure
- Glucose
Patients can view their measurements on the respective pages and the most recent measurements on the main measurements page.

### Doctor
Doctors will be able to:
- view a list of all their current patients
- add and remove patients (from a list of all users with the "patient" role)
- see current patients' latest measurements for each category (Height and weight, blood pressure, etc.)

### Database Model
The database was managed using SQLite and SQLAlchemy. The database model for the application which can be seen in models.py is:
![image](https://user-images.githubusercontent.com/13345034/171961362-c91463ac-ac6b-474b-abc1-17fab8d0fcc6.png)


## Database API
The app utilizes Flask and SQLAlchemy for the database API. Each of the endpoints are described below:

### Authentication

#### /register
- Registers a new user. Adds user to database and contact information to contact table. All fields are required.
- Methods: GET, POST

- POST JSON input format:

![image](https://user-images.githubusercontent.com/13345034/171964198-67e07bd9-b13c-4727-82c1-c3f054a1eab0.png)

#### /logout
- Logs a user out if they are logged in.
- (login required)
- Methods: GET

Logs user out using Flask-login

#### /login
- Logs a user in if the account exists, otherwise flashes an error if the password is incorrect or the the email is not in the database.
- Methods: GET, POST

- POST JSON input format:

![image](https://user-images.githubusercontent.com/13345034/171971102-127274b6-a012-46b9-8606-7506f54030b9.png)

### Measurements

#### /weight
- Allows users to enter in a height and weight. Also displays weight measurements by date in descending order.
- Methods: GET, POST

- POST JSON input format:

