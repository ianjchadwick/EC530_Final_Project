#  EC530 Final Project - Healthcare Doctor and Patient Portal

## Overview
This is a web app built using Flask and SQLAlchemy in Python and SQLite. The objective is to provide a patient and doctor portal where patients can upload the readings from their devices and doctors can monitor the information for their patients. There are two main roles, Doctor and Patient, with plans to add a third Administrator role in a future version of the app.

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
The app utilizes Flask requests and SQLAlchemy for the database API. Each of the endpoints are described below. Note, some of the pages require the user to be logged in to access (utlizing Flask-Login). This is to ensure the data is associated with the correct user:

### Authentication
These endpoints allow the user to create a new account and log into an existing account.

#### /register
- Registers a new user. Adds user to database and contact information to contact table. All fields are required.
- Methods: GET, POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/171964198-67e07bd9-b13c-4727-82c1-c3f054a1eab0.png)

#### /logout
- Logs user out using Flask-login if they are already logged in.
- (login required)
- Methods: GET

#### /login
- Logs a user in if the account exists, otherwise flashes an error if the password is incorrect or the the email is not in the database.
- Methods: GET, POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/171971102-127274b6-a012-46b9-8606-7506f54030b9.png)

### Measurements
These endpoints allow a user with the "patient" role to enter in measurements and readings for height and weight, temperature, blood pressure and blood glucose.

#### /measurement
- The main measurement page that displays the user's most recent measurements for each of the different types (height and weight, temperature, etc.). This page also has the links to the other pages for recording measurements and readings.
- Methods: GET
- (login required)

#### /weight
- Allows users to enter in a height and weight. Also displays weight measurements by date in descending order.
- (login required)
- Methods: GET, POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172021682-b2074355-7e2b-43f0-9f71-1de05a0b6313.png)

#### /delete-weight
- Allows a user to delete a previously entered height and weight measurement.
- (login required)
- Methods: POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172021753-78948d95-254e-4929-88c2-30c17792f762.png)

#### /temp
- Allows users to enter in a temperature reading. Also displays temperature readings by date in descending order.
- (login required)
- Methods: GET, POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172021792-d2c4ffe9-ef5a-406e-a56c-301708b558b3.png)

#### /delete-temp
- Allows a user to delete a previously entered temperature measurement.
- (login required)
- Methods: POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172021812-dcc595f1-81ed-40a1-977f-8ed113b32546.png)

#### /bp
- Allows users to enter in a blood pressure reading. Also displays blood pressure readings by date in descending order.
- (login required)
- Methods: GET, POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172022071-980b149d-bb5f-4526-a0c7-7edbc0373cc6.png)

#### /delete-bp
- Allows a user to delete a previously entered blood pressure measurement.
- (login required)
- Methods: POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172022112-2c0f477a-9dd2-4add-8b55-dbb49528c30e.png)

#### /glucose
- Allows users to enter in a blood glucose reading. Also displays blood glucose readings by date in descending order.
- (login required)
- Methods: GET, POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172022150-434f0dac-9617-4d2e-b29c-42aa9a9e476a.png)

#### /delete-glucose
- Allows a user to delete a previously entered blood glucose measurement.
- (login required)
- Methods: POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172022159-4764cc37-32cc-45ca-bbc4-3818820319f7.png)

### Patient Management
These endpoints allow the users with the "doctor" role to manage their patients and to view their latest measurements and readings.

#### /doctor
- Shows a list of the current patients with the latest measurements/readings for each of the categories in alphabetical order by last name. If they do not have a measurement/reading for a particular type then it will display "No Measurement" for that type. Also has a link to the patient management endpoint where doctors can add or remove patients.
- (login as "doctor" required)
- Methods: GET

#### /patient
- This will display a page which has the current list of patients, as well as a list of all the users with the "patient" role in alphabetical order by last name. Doctors are able to add and remove patients on this page with  calls to the /add-patient and /remove-patient endpoints respectively.
- (login as "doctor" required)
- Methods: GET

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172022159-4764cc37-32cc-45ca-bbc4-3818820319f7.png)

#### /add-patient
- This endpoint adds a patient to the doctor's list of current patients and redirects to the /patient endpoint.
- (login as "doctor" required)
- Methods: POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172023014-f3c0df24-dae6-4826-9eed-81e830cca8be.png)

#### /remove-patient
- This endpoint removes a patient from the doctor's list of current patients and redirects to the /patient endpoint.
- (login as "doctor" required)
- Methods: POST

- POST expected input format:

![image](https://user-images.githubusercontent.com/13345034/172023014-f3c0df24-dae6-4826-9eed-81e830cca8be.png)
