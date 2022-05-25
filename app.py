import os

from flask import Flask,render_template,request,flash
from flask_jwt import JWT
from flask_restful import Api

from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)

uri = os.environ.get("DATABASE_URL","sqlite:///data.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI']=uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='Varun'
api = Api(app)

jwt = JWT(app,authenticate,identity)

# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route("/")
def index():
    flash("Please enter your login details!!!")
    return render_template("loginpage.html")

@app.route("/login",methods=["POST"])
def login():
    username = str(request.form['username_input'])
    password = str(request.form['password_input'])
    if authenticate(username,password):
        return render_template("index.html"),200
    else:
        return render_template("Error.html"),404

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=='POST':
        username = str(request.form['username_input'])
        email = str(request.form['email_input'])
        password = str(request.form['password_input'])
        if(username =="" or password==""):
            return render_template("MissingFields.html",title="MissingField")
        status=UserRegister.post(username,password,email)
        if status==400:
            return render_template("user_registerError.html")
        return render_template("RegistrationSucess.html")
    else:
        return render_template("Register.html"),200

if __name__=='__main__':
    from database import db  # we are importing this as a part of circular imports
    db.init_app(app)
    app.run(port=8080,debug=True)
