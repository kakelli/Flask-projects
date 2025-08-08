from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('quiz'))
    return render_template('login.html')

@app.route('/quiz', methods = ['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        answers = {'q1': 'B',
                   'q2': 'C',
                   'q3': 'D',
                   'q4': 'A',
                   'q5': 'A', 
                   'q6': 'C', 
                   'q7': 'D', 
                   'q8': 'B', 
                   'q9':'C', 
                   'q10': 'A'}
        questions = []
        for key, correct in answers.items():
            user_answer = request.form.get(key)
            if user_answer is None:
                score += 0 #Missed question
            elif user_answer ==  correct:
                score += 3
            else:
                score += -1         
        session['score'] = score
        session['username'] = session.get('username', 'Guest')
        session['questions'] = questions
        return redirect(url_for('result'))
    return render_template('quiz.html')

@app.route('/result')
def result():
    username = session.get('username', 'Guest')
    score =  session.get('score', 0)
    questions = session.get('questions', [])
    return render_template('result.html', username=username, score=score, questions=questions)

if __name__ == '__main__':
    app.run(debug=True) 