import json
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, jsonify
from.models import Note, HeightWeight, Temperature, BloodPressure, Glucose, User, Patients
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short.', category="error")
        else:
            flash("Created new note.", category="success")
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # get data from post request
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/delete-weight', methods=['POST'])
def delete_weight():
    weight = json.loads(request.data)  # get data from post request
    weightId = weight['weightId']
    weight = HeightWeight.query.get(weightId)
    if weight:
        if weight.user_id == current_user.id:
            db.session.delete(weight)
            db.session.commit()

    return jsonify({})

@views.route('/delete-temp', methods=['POST'])
def delete_temp():
    temp = json.loads(request.data)  # get data from post request
    tempId = temp['tempId']
    temp = Temperature.query.get(tempId)
    if temp:
        if temp.user_id == current_user.id:
            db.session.delete(temp)
            db.session.commit()

    return jsonify({})


@views.route('/delete-bp', methods=['POST'])
def delete_BP():
    bp = json.loads(request.data)  # get data from post request
    bpId = bp['bpId']
    bp = BloodPressure.query.get(bpId)
    if bp:
        if bp.user_id == current_user.id:
            db.session.delete(bp)
            db.session.commit()

    return jsonify({})


@views.route('/delete-glucose', methods=['POST'])
def delete_glucose():
    glucose = json.loads(request.data)  # get data from post request
    glucoseId = glucose['glucoseId']
    glucose = Glucose.query.get(glucoseId)
    print(glucose)
    if glucose:
        if glucose.user_id == current_user.id:
            db.session.delete(glucose)
            db.session.commit()

    return jsonify({})


@views.route('/add-patient', methods=['POST'])
def add_patient():
    patient = json.loads(request.data)  # get data from post request
    patientId = patient['patientId']
    patient = User.query.get(patientId)
    if patient:
        new_patient = Patients(doctor_id=current_user.id,
                               first_name=patient.first_name,
                               last_name=patient.last_name,
                               patient_id=patient.id)
        db.session.add(new_patient)
        db.session.commit()

    return jsonify({})


@views.route('/remove-patient', methods=['POST'])
def delete_patient():
    patient = json.loads(request.data)  # get data from post request
    patientId = patient['patientId']
    #patient = Patients.query.filter(Patients.patient_id == f'{patientId}')
    patient = Patients.query.get(patientId)
    print(patientId)
    print(patient)
    if patient:
        if patient.doctor_id == current_user.id:
            db.session.delete(patient)
            db.session.commit()

    return jsonify({})
