# database models

#from current package(website directory) we are importing database object(db)
#flask_login module helps to log users in
#func provides the date n time

from . import db 
from flask_login import UserMixin 
from sqlalchemy.sql import func 
# database software vl gvunique id's for each object incremented to the database

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())#daten time vt the timezone vl b appended  when the notes is created
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))  #user.id references to the User class((for foreign key lower case) in sql User class vl b referred as user only) #user who created the particular note

# one to may relationship | one user multiple notes
# Foriegn key(column of one table references to the column of another table) relation ship
# has to b Implemented coz,every user vl its set of notes

# user object vl b imported from usermixin

#  vl define schema
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email= db.Column(db.String(150),unique=True)#for string datatype v hv to declare the length
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note') #(capital for relationship) Note->class #stores all the notes id created by the respective user