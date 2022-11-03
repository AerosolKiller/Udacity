from flask import Flask
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

#FLASK_APP=app.py FLASK_DEBUG=true flask run

app = Flask(__name__)



URI = 'postgresql://lpwer@localhost:5432/eg'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.drop_all()
db.create_all()

@app.route('/')


@app.route('/')
def index():
    return 'Hello World!!'
 
if __name__ == '__main__':
    app.run(debug=True) 
