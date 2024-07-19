import pymysql

def connect():
    db = pymysql.connect(host='localhost', user='root', password='18921190757ytk', database='zion')
    return db