from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    DOB = db.Column(db.String(8))
    roles = db.relationship('Role')
    contact = db.relationship('Contact')
    weight = db.relationship('HeightWeight', order_by="HeightWeight.date.desc()")
    temp = db.relationship('Temperature', order_by="Temperature.date.desc()")
    bp = db.relationship('BloodPressure', order_by="BloodPressure.date.desc()")
    glucose = db.relationship('Glucose', order_by="Glucose.date.desc()")
    patients = db.relationship('Patients', order_by="Patients.last_name")


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(10))
    patient = db.Column(db.String(10))
    admin = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10))
    street = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(5))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    device_type = db.Column(db.String(50))


class HeightWeight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weight = db.Column(db.Float)
    height_ft = db.Column(db.Integer)
    height_in = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    temperature = db.Column(db.Float)


class BloodPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    systolic = db.Column(db.Integer)
    diastolic = db.Column(db.Integer)


class Glucose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    glucose = db.Column(db.Integer)


class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patient_id = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))





