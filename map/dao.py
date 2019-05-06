import pymysql

from spider import pachong

db = pymysql.connect("localhost","root","123456","test" )

print("----------数据库连接成功----------")

cursor = db.cursor()

data = pachong()
for i in data:
    sql="""INSERT INTO map(addressname,value) VALUES ({},{})""".format(repr(i),int(data[i]))
    cursor.execute(sql)
    print("{}人口数据插入成功".format(i))
    db.commit()
db.close()