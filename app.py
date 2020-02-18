from flask import Flask, request
app = Flask(__name__)
from database.db_interactions import runInsert, runQuery
import json
from flask_restful import Api
from resources.routes import initialize_routes

api = Api(app)

initialize_routes(api)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/',methods = ['GET'])
def hello():
    out = runQuery("SELECT username, password, last_updated FROM v_user_login WHERE username != 'admin'")
    return out

@app.route('/',methods = ['DELETE'])
def delete_user1():
    print(request.json)
    query = "DELETE FROM v_user_login where username IN " + str(request.json)
    query = query.replace('[', '(').replace(']', ')')
    print(query)
    out = runInsert(query)
    return out

@app.route('/',methods = ['PUT'])
def add_user_1():
    print(request.json)
    print("INSERT INTO v_user_login(id, username, password, last_updated) VALUES (2, '" + request.json['username'] + "', '"+request.json['password']+"', '2020-02-14 12:00:00')")
    out = runInsert("INSERT INTO v_user_login(id, username, password, last_updated) VALUES (%(id)s, '" + request.json['username'] + "', '"+request.json['password']+"', %(last_updated)s)" )
    # out = ''
    return out

@app.route('/',methods = ['POST'])
def check_login():
    out = runQuery("SELECT 1 FROM v_user_login where username = '" + request.json['username'] + "' AND password = '"+request.json['password']+"'" )
    return out

@app.route('/user',methods = ['GET'])
def get_users():
    # out = runQuery("SELECT username, password, last_updated FROM v_user_login WHERE username != 'admin'")
    # out = "Users does not exist" if out == '[]' else out
    # return out
    return "Test"

if __name__ == '__main__':
    app.run(debug=True)