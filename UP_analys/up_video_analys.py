#连接mysql数据库
#连接mysql数据库
import pymysql
db = pymysql.connect(host='localhost', user='root', password='18921190757ytk', database='zion')
def select_user_name(username):
    cursor = db.cursor()
    sql = f"SELECT title,pic FROM up_video_info WHERE uname like '%{username}%'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result