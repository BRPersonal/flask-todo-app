from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer,default=0)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route("/hello")
def index() -> str:
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #create database tables

    app.run(debug=True)
