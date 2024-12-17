# flask-todo-app
A simple Flask app using python that demonstrates CRUD operations with a database

Learn Flask for python - Full tutorial
https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=WL&index=11

open a terminal
#Install virtual env
$ pip install virtualenv

#Open a terminal in project root directory and run this command
#This will Create virtual environment. This will create  env directory
$ virtualenv env

#activate virtual environment
$ source env/bin/activate

You will get into env prompt. Now you are inside virtual environment
Now after this, anything that you install is contained within this env
and will not install globally on your system. Your system is shielded from this env

To verify that you are indeed inside the virtual environment,
run the command
which python
You should get output that points to env folder of your project directory
$ which python
/Users/adiyen/poc/flask-todo-app/env/bin/python

Install the necessary dependencies in this virtual environment.
(env) is a prompt that indicates you are in virtual environment. It is
not part of the command
$ (env) pip install -r requirements.txt

To check what versions are installed in virtual environment run
$ pip list

You could also use pip freeze command to capture packages currently
installed in the environment and create requirements.txt
$ pip freeze > requirements.txt


Finally start the web server:
$ (env) python app.py

Note on sqlite
--------
path with 3 forward-slashes is relative path 
path with four forward-slashes is absolute path
database will be created in instance folder

