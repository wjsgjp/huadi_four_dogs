#连接mysql数据库
#连接mysql数据库
import pymysql
db = pymysql.connect(host='localhost', user='root', password='18921190757ytk', database='zion')


def select_videos(bid=None, title=None, pubdate_start=None, pubdate_end=None, duration_min=None, duration_max=None,
                  view=None, like=None, coin=None, share=None, danmaku=None, reply=None, favorite=None,
                  uname=None, tags=None):
    cursor = db.cursor()
    query = "SELECT title,view FROM up_video_info WHERE 1=1"
    # Add conditions based on the input parameters
    if bid:
        query += f" AND bid = '{bid}'"
    if title:
        query += f" AND title LIKE '%{title}%'"
    if pubdate_start and pubdate_end:
        query += f" AND pubdate BETWEEN '{pubdate_start}' AND '{pubdate_end}'"
    if duration_min:
        query += f" AND duration >= {duration_min}"
    if duration_max:
        query += f" AND duration <= {duration_max}"
    if uname:
        query += f" AND uname LIKE '%{uname}%'"
    if tags:
        query += f" AND tags LIKE '%{tags}%'"

    # Add sorting conditions
    if view:
        query += " ORDER BY view DESC"
    elif like:
        query += " ORDER BY like DESC"
    elif coin:
        query += " ORDER BY coin DESC"
    elif share:
        query += " ORDER BY share DESC"
    elif favorite:
        query += " ORDER BY favorite DESC"

    cursor.execute(query)
    result = cursor.fetchall()
    return result