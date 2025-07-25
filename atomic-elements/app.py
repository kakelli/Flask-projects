from flask import Flask, render_template
import json

app = Flask(__name__)

#Load element from Json
with open('elements.json') as f:
    element_data = json.load(f)['elements']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/periodic_table')
def show_periodic_table():
    with open('elements.json') as f:
        element_data = json.load(f)['elements']
    return render_template('periodic_table.html', elements=element_data, element_data=element_data)

@app.route('/element/<symbol>')
def element_detail(symbol):
    element = next((el for el in element_data if el['symbol'].lower() == symbol.lower()), None)
    if element:
        return render_template('element.html', element=element)
    else:
        return f"Element with symbol '{symbol}' not found", 404
    
if __name__ == '__main__':
    app.run(debug=True)

