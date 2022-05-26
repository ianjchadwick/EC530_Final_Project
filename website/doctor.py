from flask_login import login_required, current_user
from flask import Blueprint, render_template
from.models import User
from . import db

doctor = Blueprint('doctor', __name__)


@doctor.route('/doctor')
@login_required
def doctor_main():
    if current_user.roles[0].doctor:
        return render_template('doctor.html', user=current_user)
    else:
        return render_template('home.html', user=current_user)


@doctor.route('/patient')
@login_required
def patient_mgmt():
    if current_user.roles[0].doctor:
        users = db.session.query(User)
        return render_template('addpatient.html', all_users=users, user=current_user)
    else:
        return render_template('addpatient.html', user=current_user)
