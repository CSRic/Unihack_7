from flask_wtf import FlaskForm, Form
from wtforms import TextAreaField, PasswordField, SubmitField, BooleanField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, Email

class AnswerForm(FlaskForm):
    question1 = TextAreaField('你最害怕什么？', validators=[DataRequired()])
    question2 = TextAreaField('你如何定义成功', validators=[DataRequired()])
    question3 = TextAreaField('什么事情能够让你喜极而泣？', validators=[DataRequired()])
    question4 = TextAreaField('你如何看待特朗普？', validators=[DataRequired()])
    question5 = TextAreaField('你如何看待疫情？', validators=[DataRequired()])
    question6 = TextAreaField('你如何看待吴亦凡？', validators=[DataRequired()])
    submit = SubmitField('Submit')

class IdForm(Form):
    id = IntegerField('Form ID: ', validators=[DataRequired()])

class GuessForm(FlaskForm):
    question1 = TextAreaField('你最害怕什么？', validators=[DataRequired()])
    question2 = TextAreaField('你如何定义成功', validators=[DataRequired()])
    question3 = TextAreaField('什么事情能够让你喜极而泣？', validators=[DataRequired()])
    question4 = TextAreaField('你如何看待特朗普？', validators=[DataRequired()])
    question5 = TextAreaField('你如何看待疫情？', validators=[DataRequired()])
    question6 = TextAreaField('你如何看待吴亦凡？', validators=[DataRequired()])
    submit = SubmitField('Submit')