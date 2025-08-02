from flask import Flask, render_template, request
from utils.integrate import compute_integral
from sympy import latex

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        expr = request.form.get('expression')
        lower_limit = request.form.get('lower_limit')
        upper_limit = request.form.get('upper_limit')

        lower = float(lower_limit) if lower_limit else None
        upper = float(upper_limit) if upper_limit else None

        try:
            result = compute_integral(expr, lower, upper)
        except Exception as e:
            result = f"Error: {str(e)}"
    
    return render_template('index.html', result=None)

@app.route('/result', methods = ['POST', 'GET'])
def result_page():
    if request.method == 'POST':
        expr = request.form['expression']
        lower_limit = request.form.get('lower_limit')
        upper_limit = request.form.get('upper_limit')

        lower = float(lower_limit) if lower_limit else None
        upper = float(upper_limit) if upper_limit else None

        try:
            computed = compute_integral(expr,lower, upper)
            result = latex(computed)
        except Exception as e:
            result = f"Error:{str(e)}"
        
        return render_template('result.html', result=result)
    
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug = True)