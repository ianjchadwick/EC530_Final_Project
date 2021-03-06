from flask_login import login_required, current_user
from flask import Blueprint, render_template, request
from.models import User
from . import db
import json

doctor = Blueprint('doctor', __name__)


@doctor.route('/doctor', methods=['GET'])
@login_required
def doctor_main():
    if current_user.roles[0].doctor:
        patient_list = []
        for patient in current_user.patients:
            user = User.query.get(patient.patient_id)
            patient_list.append(user)
        return render_template('doctor.html', patients=patient_list, user=current_user)
    else:
        return render_template('home.html', user=current_user)


@doctor.route('/patient')
@login_required
def patient_mgmt():
    if current_user.roles[0].doctor:
        users = db.session.query(User)
        return render_template('addpatient.html', all_users=users, user=current_user)
    else:
        return render_template('home.html', user=current_user)

