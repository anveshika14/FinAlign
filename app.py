from flask import Flask
from flask import render_template,redirect,request,Response

app = Flask(__name__) 

#login page
@app.route("/")
def login():
     return render_template("login.html")

#registration page
@app.route("/registration")
def register():
     return render_template("Registration.html")

#dashboard page
@app.route("/dashboard")
def dashboard():
     return render_template("dashboard.html")


if __name__ == '__main__':
     app.run()