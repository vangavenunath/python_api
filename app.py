from flask import Flask, request
app = Flask(__name__)
from database.db_interactions import *
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/',methods = ['GET'])
def hello():
    out = runQuery("SELECT username, password FROM v_user_login")
    return out

@app.route('/',methods = ['POST'])
def check_login():
    print(request.json)
    out = runQuery("SELECT 112 FROM v_user_login where username = '" + request.json['username'] + "' AND password = '"+request.json['password']+"'" )
    return out

if __name__ == '__main__':
    app.run()