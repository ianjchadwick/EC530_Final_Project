from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    DOB = db.Column(db.String(8))
    roles = db.relationship('Role')
    notes = db.relationship('Note')
    contact = db.relationship('Contact')


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


