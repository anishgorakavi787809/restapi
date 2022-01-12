from logging import error
from flask import *
import requests
from requests.auth import HTTPBasicAuth
import psycopg2
from werkzeug.security import *

app = Flask(__name__)
app.secret_key = "dheidljejkelfj9oou390iojrly9"
db = psycopg2.connect(
    host="localhost", #Usually that
    user="postgres",
    password="Checkred",
    database="checkred_practice",
    )
    
cur = db.cursor()
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if 'username' in session and 'password' in session:
            return redirect(url_for('portal'))
        else:
            return render_template("index.html")

    else:
        username = request.form["username"]
        password = request.form["password"]
        cur.execute(f"select * from user_login where email='{username}'")
        test = cur.fetchone()
        print(test)
        if test == None:
            return render_template("index.html",error="Error:wrong username")
        
        else:
            validpassword = check_password_hash(test[1],password)
            if validpassword == True:
                session['username'] = username
                session['password'] = password
                return redirect(url_for('portal'))
            else:
                return render_template("index.html",error="Error:wrong password")

@app.route('/portal')
def portal():
    if 'username' in session and 'password' in session:
        return render_template("portal.html")
    else:
        return redirect(url_for('index'))
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'GET':
        if 'username' in session and 'password' in session:
            return render_template("search.html")   
        else:
            return redirect(url_for('index'))
        
    else:
        query = request.form["query"]
        req = requests.get(f"http://192.168.1.180:5000/api/search/{query}",auth=HTTPBasicAuth(session['username'],session['password']))
        jsoned = req.text
        jsoned = jsoned.split()
        return render_template("search.html",url1=jsoned[0],url2=jsoned[1],url3=jsoned[2],url4=jsoned[3],url5=jsoned[4],url6=jsoned[5],url7=jsoned[6],url8=jsoned[7],url9=jsoned[8],url10=jsoned[9])
@app.route('/signout')
def signout():
    if 'username' in session and 'password' in session:
        session.pop('username',None)
        session.pop('password',None)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/operation',methods=['POST','GET'])
def operater():
    if request.method == 'GET':
         if 'username' in session and 'password' in session:
             return render_template("operation.html")
    else:
        firstnum = request.form['firstnum']
        secondnum = request.form['secondnum']
        operator = request.form['operator']

        nums = {
            "arg1":firstnum,
            "arg2":secondnum
        }
        print(operator)
        if operator == "add":
            req = requests.post(f'http://192.168.1.180:5000/api/operation/add',json=nums,auth=HTTPBasicAuth(session['username'],session['password']))
        elif operator == "sub":
            req = requests.post(f'http://192.168.1.180:5000/api/operation/sub',json=nums,auth=HTTPBasicAuth(session['username'],session['password']))
        elif operator == "mul":
            req = requests.post(f'http://192.168.1.180:5000/api/operation/mul',json=nums,auth=HTTPBasicAuth(session['username'],session['password']))
        elif operator == "div":
            req = requests.post(f'http://192.168.1.180:5000/api/operation/div',json=nums,auth=HTTPBasicAuth(session['username'],session['password']))
        else:
            req = requests.post(f'http://192.168.1.180:5000/api/operation/mod',json=nums,auth=HTTPBasicAuth(session['username'],session['password']))
        jsoned = req.json()
        print(jsoned)
        return render_template("operation.html",result=jsoned["result"])
@app.route('/signup',methods=['GET','POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        req = requests.post('http://192.168.1.180:5000/api/signup',auth=HTTPBasicAuth(username,password))
        return render_template("index.html",success="success: your account has now been created!")
@app.route('/forgot_password',methods=['GET','POST'])
def forgot_password():
    if request.method == "GET":
        return render_template("forgotpassword.html")
    else:
        username = request.form["username"]
        email = request.form["email"]
        cur.execute(f"select * from user_login where email='{username}'")
        verify = cur.fetchone()

        if verify == None:
            return render_template("forgotpassword.html",error="error:wrong username!")
        else:
            jsoned_email = {
                "email":email
            }
            req = requests.post("http://192.168.1.180:5000/api/forgotpassword",json=jsoned_email,auth=HTTPBasicAuth(username,"FIller"))
            return render_template("index.html",success="success: Sent an email to your email! Check your inbox and fill the form in the email!")
@app.route('/recover_password_form')
def recover_password():
    return redirect('http://192.168.1.180:5000/recover_password_form')
app.run(host="0.0.0.0",port=80,)