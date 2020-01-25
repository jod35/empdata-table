from . import db


class Employee(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(40),nullable=False)
    age=db.Column(db.Integer(),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    salary=db.Column(db.Integer(),nullable=False)
    residence=db.Column(db.String(25),nullable=False)

    def __repr__(self):
        return "Employee {}".format(self.name)