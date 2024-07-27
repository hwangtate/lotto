import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1025',
    db='lotto'
)

cursor = connection.cursor()

