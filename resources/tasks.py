from flask import Response, request
from flask_restful import Resource
from database.db_interactions import runInsert, runQuery

class UserTimeLogOpsApi(Resource):

    def post(self):
        print("POST Method is called")
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

class UserTimeLogApi(Resource):
    def get(self, username):
        print("TasksApi GET method is called")
        query =  "SELECT username, create_date, start_time, end_time, comment FROM v_user_log where username IN ( '" + username + "' )"
        print(query)
        out = runQuery(query)
        return out