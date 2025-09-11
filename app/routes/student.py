from flask import Blueprint,jsonify,request

# create student blueprint

student_bp=Blueprint("student",__name__,url_prefix="/student")

@student_bp.route("/",methods=["GET","POST,PUT"])
def home():
    return "welcome to our API"

# routes and controller
@student_bp.route("/add/json",methods=["POST"])
def add_student_json ():
    data=request.get_json()
    print ("Add user using a json was hit")
    print(data)
    return "Adding user via json"

@student_bp.route("/add/form",methods=["POST"])
def add_student_form ():
    print ("Add user using a form was hit")
    return "Adding user via form"

@student_bp.route("/edit",methods=["PUT"])
def eddit_user ():
    print ("Edditing user was hit")
    return "Edditing user"

@student_bp.route("/list",methods=["GET"])
def list_users():
    print ("List Student ")
    users= [{"name":"Roy"}]
    return ( "Listing all students")