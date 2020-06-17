from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('signup.html')
@app.route('/signup',methods=['POST'])
def signup():

    # read the posted values from the UI
    _name = request.form['Name']
    _name = request.form['Username']
    _email = request.form['Email']
    _password = request.form['Password']
    _password = request.form['Confirm Password']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
if __name__ == '__main__':
    app.run(debug=True)