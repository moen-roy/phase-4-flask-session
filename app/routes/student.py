from flask import Blueprint,jsonify

# create student blueprint

student_bp=Blueprint("student",__name__)

# routes and controller
@student_bp.routes("student/add",method=["POST"])
def add_user ():
    print ("Add user was hit")
    return "Adding user"

@student_bp.routes("/students",method=["GET"])
def list_users():
    print ("List Student ")
    return "Listing all students"