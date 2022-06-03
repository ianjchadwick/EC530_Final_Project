#  EC530 Final Project - Healthcare Doctor and Patient Portal

## Overview
This is a Web app built using Flask in Python and SQLite. The objective is to provide a patient and doctor portal where patients can upload the readings from their devices and doctors can monitor the information for their patients. There are two main roles, Doctor and Patient, with plans to add a third Administrator role in a future version of the app.

## User Stories

### Patient
Patients are able to add measurements for:
- Height and Weight
- Temperature
- Blood Pressure
- Glucose

### Doctor
Doctors will be able to:
- add and remove patients from a list of all users with the patient role
- see patients' latest measurements for each category (Height and weight, blood pressure, etc.)

### Database Model
The database was managed using SQLite and SQLAlchemy. The database model for the application which can be seen in models.py is:
![image](https://user-images.githubusercontent.com/13345034/171961362-c91463ac-ac6b-474b-abc1-17fab8d0fcc6.png)

