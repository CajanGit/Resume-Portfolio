from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for('views.home')) #added so when adding note, page reloading first redirects to url views.home 
    notes = Note.query.all() #asks for data from database so that page can use the data
    return render_template("home.html", notes = notes)

@views.route('/resume', methods = ['GET','POST'])
def resume():
    return render_template("resume.html")

@views.route('/github', methods = ['GET','POST'])
def github():
    return render_template("github.html")

@views.route('/aboutme', methods = ['GET','POST'])
def aboutMe():
    return render_template("aboutMe.html")

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        db.session.delete(note)
        db.session.commit()

    return jsonify({})

