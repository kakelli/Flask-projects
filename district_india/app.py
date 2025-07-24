from flask import Flask, request, render_template
import json

app = Flask(__name__)

#Loading the data from JSON file
with open('i_data.json') as f:
    data = json.load(f)

@app.route('/', methods = ['GET', 'POST'])
def index():
    state_info = None
    state_name = None

    if request.method == 'POST':
        state_name = request.form['state_name'].strip()
        state_info = data.get(state_name)

    return render_template('index.html', state_info=state_info, state_name=state_name)

if __name__ == '__main__':
    app.run(debug=True)