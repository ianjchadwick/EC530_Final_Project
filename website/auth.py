from flask import Blueprint, render_template, request, flash, redirect, url_for
from.models import User, Role, Contact
from werkzeug.security import generate_password_hash, check_password_hash
from. import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category="error")
        else:
            flash('Email does not exist.', category="error")

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register',  methods=['GET', 'POST'])
def register():
    # Get the info from the sign-up form
    if request.method == 'POST':
        # Get info for user table
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        DOB = request.form.get('DOB')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # Get role table information
        patient = request.form.get('role1')
        doctor = request.form.get('role2')
        admin = request.form.get('role3')
        # Get contact table information
        phone = request.form.get('phone')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        zip = request.form.get('zip')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category="error")
        elif len(first_name) < 2:
            flash('Name must be greater than 1 character.', category="error")
        elif password1 != password2:
            flash('Passwords don\'t match.', category="error")
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category="error")
        elif not (admin or doctor or patient):
            flash('You must select at least one role.', category="error")
        else:
            # add user to database
            new_user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            DOB=DOB,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # Log the user in so we can get their newly assigned id
            login_user(new_user, remember=True)
            # Assign user roles
            new_user_roles = Role(doctor=doctor,
                                  admin=admin,
                                  patient=patient,
                                  user_id=current_user.id)
            db.session.add(new_user_roles)
            # Add new user contact information
            new_user_contact = Contact(phone=phone,
                                       street=street,
                                       city=city,
                                       state=state,
                                       zip=zip,
                                       user_id=current_user.id)
            db.session.add(new_user_contact)
            db.session.commit()
            flash('Account created!', category="success")
            return redirect(url_for('views.home'))

    return render_template("reg.html", user=current_user)
