
from flask import *
from flask_restful import *
import psycopg2
import random
from werkzeug.security import *
import traceback
import smtplib
from googlesearch import search
from flask_cors import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = psycopg2.connect(
    host="localhost", #Usually that
    user="postgres",
    password="Checkred",
    database="checkred_practice",
    )
cur = db.cursor()
server = smtplib.SMTP("xxxx.xxx.xxx",587)
server.starttls()
server.login("xxxxxxxx@xxx.com","3283829732923823982389")
def randomnums():
    firstdig = random.randint(0,9)
    seconddig = random.randint(0,9)
    thirddig = random.randint(0,9)
    all3dig = str(firstdig) + str(seconddig) + str(thirddig)
    return all3dig

class Operations(Resource):
    def get(self,name):
        return jsonify({'error':'NO GET ALLOWED!!!!!!!!'})
    def post(self,name):
        try:
            username = request.authorization["username"]
            password = request.authorization["password"]
            username = username.replace("'","")
            password = password.replace("'","")
            cur.execute(f"select * from user_login where email='{username}'")
            proceed = False
            isitondb = cur.fetchone()
            print(isitondb[1])
            if isitondb == None:
                return jsonify({"error":"Wrong username! If you have no account, use /signup!"})
            else:
                correctpassword = check_password_hash(isitondb[1],password)
                print(correctpassword)
                if correctpassword == True:
                    proceed = True
                    print(proceed)
                else:
                    return jsonify({"error":"Wrong password!"})
            if proceed == True:
                if name == "add":
                    lol = request.get_json()
                    #d = json.dumps(lol)
                    uuid = 0
                    while True:
                        uuid = randomnums()
                        cur.execute(f'select * from audit_history where UNID={uuid}')
                        sameuuid = cur.fetchone()
                        if sameuuid == None:
                            break
                        else:
                            print("Same!")
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) + int(secondvar)
                        }
                    print("Putting into database")
                   
                    cur.execute("insert into audit_history(UNID,URL,Request,Response) values(%s,'http://192.168.1.180:5000/api/operation/add',%s,%s)",(uuid,str(lol),str(result)))
                    db.commit()
                    return jsonify(result)

                if name == "sub":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        uuid = randomnums()
                        cur.execute(f'select * from audit_history where UNID={uuid}')
                        sameuuid = cur.fetchone()
                        if sameuuid == None:
                            break
                        else:
                            print("Same!")
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) - int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    cur.execute("insert into audit_history(UNID,URL,Request,Response) values(%s,'http://192.168.1.180:5000/api/operation/sub',%s,%s)",(uuid,str(lol),str(result)))
                    db.commit()
                    return jsonify(result)

                if name == "mul":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        uuid = randomnums()
                        cur.execute(f'select * from audit_history where UNID={uuid}')
                        sameuuid = cur.fetchone()
                        if sameuuid == None:
                            break
                        else:
                            print("Same!")
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) * int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    cur.execute("insert into audit_history(UNID,URL,Request,Response) values(%s,'http://192.168.1.180:5000/api/operation/mul',%s,%s)",(uuid,str(lol),str(result)))
                    db.commit()
                    return jsonify(result)

                if name == "mod":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        uuid = randomnums()
                        cur.execute(f'select * from audit_history where UNID={uuid}')
                        sameuuid = cur.fetchone()
                        if sameuuid == None:
                            break
                        else:
                            print("Same!")
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) % int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    cur.execute("insert into audit_history(UNID,URL,Request,Response) values(%s,'http://192.168.1.180:5000/api/operation/mod',%s,%s)",(uuid,str(lol),str(result)))
                    db.commit()
                    return jsonify(result)

                if name == "div":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        uuid = randomnums()
                        cur.execute(f'select * from audit_history where UNID={uuid}')
                        sameuuid = cur.fetchone()
                        if sameuuid == None:
                            break
                        else:
                            print("Same!")
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) / int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    cur.execute("insert into audit_history(UNID,URL,Request,Response) values(%s,'http://192.168.1.180:5000/api/operation/div',%s,%s)",(uuid,str(lol),str(result)))
                    db.commit()
                    return jsonify(result)
                else:
                    return jsonify({"error":"Wrong operator"})
        #Error if none is inputed
        except:
            traceback.print_exc()
            return jsonify({"error":"Wrong username;Wrong password! If you have no account, use /signup!"})

#This is to create accounts
class SignUp(Resource):
    def get(self):
        return jsonify({"error":"No GET!!!!!"})
    def post(self):
        username = request.authorization["username"]
        password = request.authorization["password"]
        username = username.replace("'","")
        password = password.replace("'","")
        password = generate_password_hash(password)
        cur.execute("insert into user_login(email,password) values(%s,%s)",(username,password))
        db.commit()
        return "Signed you up!"

class ForgotPassword(Resource):
    def get(self):
        return jsonify({"error":"No GET!!!!!"})
    def post(self):
        username = request.authorization["username"]
        username = username.replace("'","")
        cur.execute(f"select * from user_login where email='{username}'")
        isitondb = cur.fetchone()
        
        if isitondb == None:
            return jsonify({"error":"Wrong username! If you have no account, use /signup!"})
        else:
           
            email = request.get_json()
            message = "link is 192.168.1.180/recover_password_form"
            server.sendmail("anish.gorakavi@gmail.com",email["email"],message)
            return jsonify({"success":"Check your inbox!"})

class LogIn(Resource):
    def post(self):
        return jsonify({"error":"No POST!!!!!"})
    def get(self):
        username = request.authorization["username"]
        password = request.authorization["password"]
        username = username.replace("'","")
        print(username)
        print(password)
        cur.execute(f"select * from user_login where email='{username}'")
        isitondb = cur.fetchone()
        
        if isitondb == None:
            return jsonify({"error":"Wrong username! If you have no account, use signup!"})
        else:
            print("checkmate")
            passwordcheck = check_password_hash(isitondb[1],password)
            if passwordcheck == False:
                
               
                return jsonify({"error":"Wrong password!"})
            else:
                return jsonify({"success":"Logged in!"})
    def options(self):
        return jsonify({"success":"Logged in!"})
 #These are to route the classes
api.add_resource(Operations,'/api/operation/<string:name>') #localhost/api/operattion/add
api.add_resource(SignUp,'/api/signup')
api.add_resource(ForgotPassword,'/api/forgotpassword')
api.add_resource(LogIn,"/api//testlogin")

#Now, this is a help page
@app.route('/', methods=['GET','POST'])
def index():
    return """
        /api/operation/add - addition
        /api/operation/sub - subtraction
        /api/operation/mul - multiplication
        /api/operation/div - division
        /api/operation/mod - modulo
        /api/signup - create account!
        /api/search/ - search
        /api/forgotpassword - forgot password
        /api/testlogin - Test login!
        EVERY REQUEST HAS TO BE POST!!!!!!!! BUT /api/search has to be GET

        for math operations:
            body:
            {
                "arg1":number,
                "arg2":number
            }(IN JSON MODE!)
        for forgotpassword:
            body:
            {
                "email":"your email id"
            }
        for search:
            /api/search/<query>
        YOU NEED TO AUTHENTICATE!!!!!!
        
    """
@app.route("/recover_password_form")
def recoverpasswordform():
    return render_template("index.html")

@app.route("/recover_password",methods=['POST'])
def recoverpassword():
    username = request.form['username']
    password = request.form['password']
    username = username.replace("'","")
    password = password.replace("'","")
    cur.execute(f"select * from user_login where email='{username}'")
    isitondb = cur.fetchone()
    if isitondb == None:
        return jsonify({"error":"Wrong username! If you have no account, use /signup!"})
    else:
        password = generate_password_hash(password)
        cur.execute(f"update user_login set password = '{password}' where email = '{username}'")
        db.commit()
        return "Changed your password"
@app.route('/api/search/<string:query>')
def searchman(query):
    try:

            username = request.authorization["username"]
            password = request.authorization["password"]
            username = username.replace("'","")
            password = password.replace("'","")
            print(username)
            print(password)
            cur.execute(f"select * from user_login where email='{username}'")
            proceed = False
            isitondb = cur.fetchone()
            print(isitondb[1])

            if isitondb == None:
                return jsonify({"error":"Wrong username! If you have no account, use /signup!"})
            else:
                searchlist = []
                for i in search(query,num=10,stop=10):
                    searchlist.append(i)
                x = f"""
                {searchlist[0]}
                {searchlist[1]}
                {searchlist[2]}
                {searchlist[3]}
                {searchlist[4]}
                {searchlist[5]}
                {searchlist[6]}
                {searchlist[7]}
                {searchlist[8]}
                {searchlist[9]}
                """
                print(x)
                urls = {
                    "url1":searchlist[0],
                    "url2":searchlist[1],
                    "url3":searchlist[2],
                    "url4":searchlist[3],
                    "url5":searchlist[4],
                    "url6":searchlist[5],
                    "url7":searchlist[6],
                    "url8":searchlist[7],
                    "url9":searchlist[8],
                    "url10":searchlist[9]
                }
                return jsonify(urls)
    except:
        traceback.print_exc()
        return jsonify({"error":"Wrong username or password! If you have no account, use /signup!"})
   
if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')