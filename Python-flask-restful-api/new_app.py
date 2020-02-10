import pymysql
from flask import Flask, jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class IOT(Resource):
    def get(self):
        db = pymysql.connect("localhost","root","","sensor")
        cursor = db.cursor()
        query = """select * from tb_ldr"""
        cursor.execute(query)
        data = cursor.fetchall()
        payload = []
        content = {}
        for row in data:
            print(row)
            content = {'ldrid':row[0], 'ldrdata':row[1]}
            payload.append(content)

        db.close()
        return jsonify(payload)


    def post(self):
        some_json = request.get_json()
        db = pymysql.connect("localhost","root","","sensor")
        cursor = db.cursor()
        query = """insert into tb_ldr VALUES({},{})""".format(some_json["ldrid"],some_json["ldrdata"])
        cursor.execute(query)
        db.commit()
        db.close()

        return{'response': 'inserted successfully'},201

    
class IOT2(Resource):
    def get(self):
        db = pymysql.connect("localhost","root","","sensor")
        cursor = db.cursor()
        query = """select * from tb_temp"""
        cursor.execute(query)
        data=cursor.fetchall()
        payload = []
        content = {}
        for row in data:
            print(row)
            content = {'tempid': row[0], 'tempdata': row[1]}
            payload.append(content)
            
        db.close()
    
        return jsonify(payload)

    
    def post(self):
        some_json = request.get_json()
        db = pymysql.connect("localhost","root","","sensor")
        cursor = db.cursor()
        query = """insert into tb_temp VALUES({},{})""".format(some_json["tempid"],some_json["tempdata"])
        cursor.execute(query)
        db.commit()
        db.close()

        return{'response': 'inserted successfully'},201


    

api.add_resource(IOT,'/ldr')
api.add_resource(IOT2,'/temp')

if __name__ == "__main__":
    app.run(debug=True)
        
