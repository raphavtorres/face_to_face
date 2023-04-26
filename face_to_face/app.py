from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
""" app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///face_to_face.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    tip_1 = db.Column(db.String(100), nullable=True)
    tip_2 = db.Column(db.String(100), nullable=True)
    tip_3 = db.Column(db.String(100), nullable=True)
    tip_4 = db.Column(db.String(100), nullable=True) """

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# https://stackoverflow.com/questions/45877080/how-to-create-dropdown-menu-from-python-list-using-flask-and-html