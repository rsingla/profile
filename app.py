import os

from flask import Flask
from person import GetJson
from flask import render_template 
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

@app.route('/person')
def get_person_data():
    return GetJson()

@app.route('/signup', methods=['GET', 'POST'])
def register():
     if(request.method == 'POST'):
         print(request.form['username'])
         print(request.form['input-password'])
         print(request.form['reconfirm-password'])
         return render_template('success.html')
     return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
     if(request.method == 'POST'):
         print(request.form['username'])
         print(request.form['password'])
         return render_template('success.html')
     return render_template('logins.html')
     

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
