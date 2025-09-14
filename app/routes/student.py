from flask import Blueprint,jsonify,request
from app.models import Student
from app.db import db
import re  

# create student blueprint

student_bp=Blueprint("student",__name__,url_prefix="/student")

@student_bp.route("/",methods=["GET","POST,PUT"])
def home():
    return "welcome to our API"

# routes and controller
@student_bp.route("/add/json",methods=["POST"])
def add_student_json ():

    print ("Add user using a json was hit")
    data=request.get_json()
    # checking name
    name= data.get("name")
    email=data.get("email")

    if not name:
        return jsonify({"error":"Name is invalid"}),400
    if not email:
        return jsonify({"error":"Email invalid"}),400
    email_regex= r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex,email):
        return jsonify({"error":"Incorect email format"})

    exists= Student.query.filter_by(email=email).first()
    if exists:
        return jsonify({"error":"Email in use"}),400
    
    new_student=Student(name=name,email=email)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({
        "message":"Student added",
        "name":new_student.name,
        "email":new_student.email,
        "created_at":new_student.created_at

    })



    

    print(data)
    return "Adding user via json",200

@student_bp.route("/add/form",methods=["POST"])
def add_student_form ():
    print ("Add user using a form was hit")
    return "Adding user via form",200

@student_bp.route("/edit",methods=["PUT"])
def eddit_user ():
    print ("Edditing user was hit")
    return "Edditing user"

@student_bp.route("/list",methods=["GET"])
def list_users():
    print ("List Student ")
    users= [{"name":"Roy"}]
    return ( "Listing all students")