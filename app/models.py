from .db import db


class Student(db.Model):
    __tablename__="student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    phone=db.Column(db.Integer,nullable=False, unique= True)
