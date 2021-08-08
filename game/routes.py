from flask import render_template, url_for, flash, redirect, request
from game import app, db
from game import app
from game.forms import AnswerForm, IdForm
from game.models import AnsweredForm
from sentence_comparison import *

questions = [
    'what is your name', 
    'how old are you', 
    'where do you come from', 
    'what are your hobbies', 
    'do you like python programming', 
    'what is the best programming language in the world', 
    'are you willing to be a web developer in the future', 
    'can you use flask', 
    'talk about randomization algorithm'
]

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

wanted_id = 0

@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/answer", methods=['GET', 'POST'])
def answer():
    form = AnswerForm()
    if form.validate_on_submit():
        af = AnsweredForm(question1=form.question1.data, question2=form.question2.data, question3=form.question3.data, question4=form.question4.data, question5=form.question5.data, question6=form.question6.data)
        db.session.add(af)
        db.session.commit()
        flash('Your answer has been submitted! Here is your answer!', 'success')
        return redirect(url_for('youranswer'))
    return render_template('answer.html', title='Give Your Answers', form=form)

@app.route("/youranswer", methods=['GET', 'POST'])
def youranswer():
    af = AnsweredForm.query.order_by(-AnsweredForm.id).first()
    
    return render_template('youranswer.html', title='Your Answer', af=af)

@app.route("/enterid", methods=['GET', 'POST'])
def enterid():
    form = IdForm()
    if request.method == 'POST' and form.validate():
        global wanted_id
        wanted_id = int(request.form['id'])
        exists = bool(AnsweredForm.query.filter_by(id=wanted_id).first())
        if exists:
            flash('Start guessing!', 'success')
            return redirect(url_for('guess'))
        else:
            flash('ID does not exist. Please check again.', 'danger')
    return render_template('enterid.html', title='Enter A Form ID', form=form)


@app.route("/guess", methods=['GET', 'POST'])
def guess():
    form = AnswerForm()
    if form.validate_on_submit():
        af = AnsweredForm(question1=form.question1.data, question2=form.question2.data, question3=form.question3.data, question4=form.question4.data, question5=form.question5.data, question6=form.question6.data)
        db.session.add(af)
        db.session.commit()
        flash("Your answer has been submitted! Here are your guess and your friend's original answer!", 'success')
        return redirect(url_for('yourresult'))
    return render_template('guess.html', title='Have a Guess', form=form)



@app.route("/yourresult", methods=['GET', 'POST'])
def yourresult():
    af1 = AnsweredForm.query.filter_by(id=wanted_id).first()
    af2 = AnsweredForm.query.order_by(-AnsweredForm.id).first()
    score1 = scom(af1.question1, af2.question1, difficulty = 3)
    score2 = scom(af1.question2, af2.question2, difficulty = 3)
    score3 = scom(af1.question3, af2.question3, difficulty = 3)
    score4 = scom(af1.question4, af2.question4, difficulty = 3)
    score5 = scom(af1.question5, af2.question5, difficulty = 3)
    score6 = scom(af1.question6, af2.question6, difficulty = 3)
    score = (score1 + score2 + score3 + score4 +score5 + score6) / 6
    
    return render_template('yourresult.html', title='Your Result', af1=af1, af2=af2, wanted_id=wanted_id, score = score)