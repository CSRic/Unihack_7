import random
from flask import Flask, request

app = Flask(__name__)



questionsPool = ['what is your name', 'how old are you', 'where do you come from', 'what are your hobbies', 'do you like python programming', 'what is the best programming language in the world', 'are you willing to be a web developer in the future', 'can you use flask', 'talk about randomization algorithm']
database = {}
id = 1

def listToStr(data):
    ret = ""
    i = 0
    while(i < len(data)-1):
        ret = ret + data[i] + ';'
        i += 1
    ret += data[-1]
    return ret

@app.route('/')
def home():
    with open("index.html") as f:
        html = f.read()

    return html

@app.route('/enterid')
def enterid():
    with open("enterid.html") as f:
        html = f.read()

    return html

@app.route('/form', methods=['GET','POST'])
def form():
    with open("form.html") as f:
        html = f.read()
    action = request.args["action"]
    if(action == 'create'):
        questions = random.sample(questionsPool, 6)
        formCode = ''
        for i in range(1,7):
            formCode = formCode + '<input type="hidden" id="q' + str(i) + '" name="q' + str(i) + '" value="' + questions[i-1] + '">\n<label for="a' + str(i) + '">' + str(i) + '.' + questions[i-1] + '</label><br>\n<input type="text" id="a' + str(i) + '" name="a' + str(i) + '"><br>\n'
        html = html.format("getData", formCode) 
        return html
    if(action == 'play'):
        global database
        formid = int(request.form["formid"])
        if(not (formid in database)):
            return "Error: form not found. Please enter a correct ID number"
        questions = database[formid][0]
        formCode = '<input type="hidden" id="formid" name="formid" value="' + str(formid) + '">\n' 
        for i in range(1,7):
            formCode = formCode + '<input type="hidden" id="q' + str(i) + '" name="q' + str(i) + '" value="' + questions[i-1] + '">\n<label for="a' + str(i) + '">' + str(i) + '.' + questions[i-1] + '</label><br>\n<input type="text" id="a' + str(i) + '" name="a' + str(i) + '"><br>\n'
        html = html.format("result", formCode) 
        return html

@app.route('/getData', methods=['POST'])
def getData():
    questions = []
    answers = []
    for i in range(1,7):
        questionID = 'q' + str(i)
        answerID = 'a' + str(i)
        question = request.form[questionID]
        answer = request.form[answerID]
        questions.append(question)
        answers.append(answer)
    global id
    global database
    oldID = id
    database[id] = [questions, answers]
    id += 1
    info = 'Your answers are successfully submitted! Your answers are:<br><br>'
    for i in range(1,7):
        info = info + "Question " + str(i) + '. ' + questions[i-1] + '<br>' + "Answer: " + answers[i-1] + "<br><br>"
    info += "The ID of your questionaire is " + str(oldID)
    return info

@app.route('/result', methods=['POST'])
def result():
    global database
    yourAnswers = []
    formid = 0
    formid = int(request.form["formid"])
    questions = database[formid][0]
    originalAnswers = database[formid][1]
    for i in range(1,7):
        answerID = 'a' + str(i)
        answer = request.form[answerID]
        yourAnswers.append(answer)
    info = 'Your answers are successfully submitted!<br><br>'
    for i in range(1,7):
        info = info + "Question " + str(i) + '. ' + questions[i-1] + '<br>' + "Original Answer: " + originalAnswers[i-1] + '<br>'+ "Your Answer: " + yourAnswers[i-1]  + "<br><br>"
    info = info + "TODO: After the algorithm is completed, the similarity rate will be displayed here."
    return info

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!

# NOTE: app.run never returns (it runs for ever, unless you kill the process)
# Thus, don't define any functions after the app.run call, because it will
# never get that far.
