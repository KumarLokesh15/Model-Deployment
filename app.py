from flask import Flask, render_template, request
import salary

app = Flask(__name__)

@app.route("/hi", methods=['GET','POST'])

def hello():
    if request.method == 'POST':
        exp = request.form['exp']
        salary_pred = salary.salary_exp_pred(exp) 
        sl = salary_pred
    return render_template('index.html', sl = sl)

#@app.route('/sub', methods = ['POST'])
#def submit(salary_pred):
    # html -> py
    #if request.method=='POST':
     #   name = request.form["exp"]

    # py -> html
    #return render_template('sub.html', n = name)

if __name__ == "__main__":
    app.run(debug=True)
