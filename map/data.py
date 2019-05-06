import pandas
import pymysql
import json


def getdata():
    db = pymysql.connect("localhost","root","123456","test" )

    print("----------数据库连接成功----------")

    cursor = db.cursor()
    sql="""select * from map"""
    cursor.execute(sql)
    value = cursor.fetchall()
    result = {}
    for i in value:
        result[i[0]]=i[1]
    print(result)
    jsonstr = json.dumps(result,ensure_ascii=False)
    db.commit()
    db.close()
    return jsonstr