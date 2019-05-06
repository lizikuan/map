import json

import pymysql
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def map():
    return render_template("map.html")

@app.route('/getdata')
def getdata():
    db = pymysql.connect("localhost", "root", "123456", "test")
    print("----------数据库连接成功----------")
    cursor = db.cursor()
    sql = """select * from map"""
    cursor.execute(sql)
    value = cursor.fetchall()
    result = {}
    for i in value:
        result[i[0]] = i[1]
    #jsonstr = json.dumps(result, ensure_ascii=False)
    db.commit()
    db.close()
    data = []
    for i in value:
        data.append({"name":i[0],"value":i[1]})
    print(data)
    jsonstr = json.dumps(data, ensure_ascii=False)
    return jsonstr
if __name__=='__main__':
    app.run()