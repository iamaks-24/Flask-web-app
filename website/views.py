# saves the standard routes ,to whuch user navigates to

from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from .models import Note
from website import db
import json
# blueprint setup for flask app
# views is variable that can b changed
views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required # u cant goto home page unless u r login
def home():
    if request.method=='POST':
        note=request.form.get('note')
        if len(note)<1:
            flash('Note is too short!',category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!',category='success')
    return render_template("home.html",user=current_user)

@views.route("/delete-note",methods=['POST'])
def delete_note():
    note=json.loads(request.data)#v r loading using json coz data recieved in form of string not form element so json is used to convert to python dict format
    noteId=note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})#empty response
