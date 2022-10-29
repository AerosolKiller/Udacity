#import flask class from flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#instantiate app
app = Flask(__name__)

# connect app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lpwer@localhost:5432/eg'

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable = False)

#create tables based on db.model that was configured with the associate table
db.create_all()   

#python decorator
#tell Flask app which endpoint to listen to for connections. 
@app.route('/')

# name the route handler as "index" (root route)
def index():
    return 'Hello World!!'
