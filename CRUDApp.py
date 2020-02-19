import flask
from flask import Flask
from flask import request
from flask import render_template

import os
os.chdir("/Users/danielnixa/projects/flask-crud-app")

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "CRUDApp.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Stock(db.Model):
    co_name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Company Name: {}>".format(self.co_name)



@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)