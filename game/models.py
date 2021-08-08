from game import db
from datetime import datetime


class AnsweredForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question1 = db.Column(db.Text, nullable=False)
    question2 = db.Column(db.Text, nullable=False)
    question3 = db.Column(db.Text, nullable=False)
    question4 = db.Column(db.Text, nullable=False)
    question5 = db.Column(db.Text, nullable=False)
    question6 = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f"AnsweredForm('{self.id}', '{self.question1}', '{self.question2}', '{self.question3}', '{self.question4}', '{self.question5}', '{self.question6}')"

