from flask import Blueprint, render_template, request, flash, redirect, url_for
from.models import User, Role, Contact, HeightWeight, Temperature, BloodPressure, Glucose
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
        if not height_ft:
            flash('Please enter height in feet.', category='error')
        elif not height_in:
            flash('Please enter height in inches.', category='error')
        elif not weight:
            flash('Please enter a weight measurement.', category='error')
        else:
            new_measurement = HeightWeight(height_ft=height_ft,
                                       height_in=height_in,
                                       weight=weight,
                                       user_id=current_user.id)
            db.session.add(new_measurement)
            db.session.commit()
            flash('Measurement added!', category='success')
    return render_template('weight.html', user=current_user)


@measurement.route('/temp', methods=['GET', 'POST'])
@login_required
def temperature():
    if request.method == 'POST':
        temp = request.form.get('temperature')
        if not temp:
            flash('Please enter a temperature.', category='error')
        else:
            new_temp = Temperature(temperature=temp,
                                   user_id=current_user.id)
            db.session.add(new_temp)
            db.session.commit()
            flash('Measurement added!', category='success')
    return render_template('temp.html', user=current_user)


@measurement.route('/bp', methods=['GET', 'POST'])
@login_required
def bp_measurement():
    if request.method == 'POST':
        systolic = request.form.get('systolic')
        diastolic = request.form.get('diastolic')
        if not systolic:
            flash('Please enter a systolic pressure.', category='error')
        elif not diastolic:
            flash('Please enter a diastolic pressure.', category='error')
        else:
            new_bp = BloodPressure(systolic=systolic,
                                   diastolic=diastolic,
                                   user_id=current_user.id)
            db.session.add(new_bp)
            db.session.commit()
            flash('Measurement added!', category='success')
    return render_template('bp.html', user=current_user)


@measurement.route('/glucose', methods=['GET', 'POST'])
@login_required
def glucose_reading():
    if request.method == 'POST':
        glucose = request.form.get('glucose')
        if not glucose:
            flash('Please enter blood glucose measurement.', category='error')
        else:
            new_glucose = Glucose(glucose=glucose,
                                   user_id=current_user.id)
            db.session.add(new_glucose)
            db.session.commit()
            flash('Measurement added!', category='success')
    return render_template('glucose.html', user=current_user)