from app.db import db
from datetime import datetime,timezone


class Student(db.Model):
    __tablename__="student"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(500),nullable=False,unique=True)
    created_at=db.Column(db.DateTime,default=datetime.now(timezone.utc),nullable=False)