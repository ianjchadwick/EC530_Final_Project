from flask import Blueprint, render_template, request, flash, redirect, url_for
from.models import User, Role, Contact, HeightWeight, Temperature
from werkzeug.security import generate_password_hash, check_password_hash
from. import db
from flask_login import login_user, login_required, logout_user, current_user

measurement = Blueprint('measurements', __name__)


@measurement.route('/measurement', methods=['GET'])
@login_required
def measure_main():
    return render_template('measurements.html', user=current_user)


@measurement.route('/weight', methods=['GET', 'POST'])
@login_required
def height_weight():
    if request.method =='POST':
        height_ft = request.form.get('height_ft')
        height_in = request.form.get('height_in')
        weight = request.form.get('weight')
        new_measurement = HeightWeight(height_ft=height_ft,
                                       height_in=height_in,
                                       weight=weight,
                                       user_id=current_user.id)
        db.session.add(new_measurement)
        db.session.commit()
    return render_template('weight.html', user=current_user)


@measurement.route('/temp', methods=['GET', 'POST'])
@login_required
def temperature():
    if request.method == 'POST':
        temp = request.form.get('temperature')
        new_temp = Temperature(temperature=temp,
                               user_id=current_user.id)
        db.session.add(new_temp)
        db.session.commit()
    return render_template('temp.html', user=current_user)