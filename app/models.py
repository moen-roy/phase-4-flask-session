from .db import db


class Student(db.Model1):
    __tablename__="student"

    id= db.Column(db.Integer, primary=True)
    name= db.Column(db.String(100), mutable= True,unique=True)