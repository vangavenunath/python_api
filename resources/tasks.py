from flask import Response, request
from flask_restful import Resource
from database.db_interactions import runInsert, runQuery

class UserTimeLogOpsApi(Resource):

    def post(self):
        print("POST Method is called")
        check_query = "select 1 from v_user_log where username = '" + \
                request.json['username'] + "' AND create_date = '" + request.json['create_date'] + "'"
        out = runQuery(check_query)
        if not(out == '[[1]]') :
            query = "INSERT INTO v_user_log(id, username, create_date, start_time, end_time, comment, last_updated) VALUES (%(id)s, '" + \
                request.json['username'] + "', '" + request.json['create_date'] + "', '" + request.json[
                    'start_time'] + "', '" + request.json['end_time'] + "', '" + request.json[
                    'comment'] + "', %(last_updated)s )"
            print(query)
            out = runInsert(query)
        return out, 200

    def delete(self):
        print("DELETE method is called")
        print(request.json)
        return 'Success', 201

class AdminTimeLogApi(Resource):
    def post(self):
        print("UserTimeLogApi POST method is called")
        print(request.json)
        if str(request.json['username']) == '[]':
            query = "SELECT username, create_date, start_time, end_time, comment FROM v_user_log where create_date >= '" + \
                    request.json['from_date'] + "' AND create_date <= '" + request.json['to_date'] + "'"
        else:
            query =  "SELECT username, create_date, start_time, end_time, comment FROM v_user_log where create_date >= '"+request.json['from_date']+"' AND create_date <= '"+request.json['to_date']+"' AND username IN " + str(request.json['username'])
        query = query.replace('[', '(').replace(']', ')')
        print(query)
        out = runQuery(query)
        return out, 200

class LeavesApi(Resource):
    def post(self):
        print("LeavesApi POST method is called")
        print(request.json)
        query =  "select username, leave_date, last_updated from v_user_leaves where leave_status = 'pending'"
        print(query)
        out = runQuery(query)
        return out, 200
    def put(self):
        print("LeavesApi PUT method is called")
        print(request.json)
        query =  "UPDATE v_user_leaves SET leave_status = '" + request.json['status'] + "' WHERE username = '" + \
                 request.json['username'] +"' and leave_date = '" + request.json['leave_date'] +"'"
        print(query)
        out = runQuery(query)
        return out, 200

class UserTimeLogApi(Resource):
    def post(self):
        print("UserTimeLogApi POST method is called")
        print(request.json)
        query =  "SELECT username, create_date, start_time, end_time, comment FROM v_user_log where username IN " + str(request.json['username'])
        query = query.replace('[', '(').replace(']', ')')
        print(query)
        out = runQuery(query)
        return out, 200

class UsersApi(Resource):
    def get(self):
        print("UsersApi GET method is called")
        query =  "SELECT DISTINCT username FROM v_user_login WHERE username != 'admin'"
        print(query)
        out = runQuery(query)
        return out