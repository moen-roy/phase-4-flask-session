from flask import Blueprint,jsonify

# create student blueprint

student_bp=Blueprint("student",__name__,url_prefix="/student")

@student_bp.route("/",methods=["GET"])
def home():
    return "welcome to our API"

# routes and controller
@student_bp.route("/add",methods=["POST"])
def add_student ():
    print ("Add user was hit")
    return "Adding user"

@student_bp.route("/edit",methods=["PUT"])
def eddit_user ():
    print ("Edditing user was hit")
    return "Edditing user"

@student_bp.route("/list",methods=["GET"])
def list_users():
    print ("List Student ")
    users= [{"name":"Roy"}]
    return ( "Listing all students")