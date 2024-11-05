from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

#This is an entity representing a table
#id is automatically generated for every new record
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer,default=0)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route("/",methods=["POST","GET"])
def index() -> str:
    if request.method == 'POST':
        task = request.form["content"]
        new_task = Todo(content=task)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your task"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html",tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting that task"

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]

        try:
            db.session.commit() #Just a commit will do, since we have modified content attribute
            return redirect("/")
        except:
            return "There was a problem updating that task"
    else:
        return render_template("update.html", task=task)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #create database tables

    app.run(port=5001,debug=True)
