from flask import Blueprint,jsonify

# create student blueprint

student_bp=Blueprint("student",__name__)
@student_bp.route("/",methods=["GET"])
def home():
    return "welcome to our API"

# routes and controller
@student_bp.route("/student/add",methods=["POST"])
def add_user ():
    print ("Add user was hit")
    return "Adding user"

@student_bp.route("/students",methods=["GET"])
def list_users():
    print ("List Student ")
    users= [{"name":"Roy"}]
    return (jsonify (users), "Listing all students")