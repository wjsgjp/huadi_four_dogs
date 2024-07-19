#连接mysql数据库
#连接mysql数据库
import pymysql
from database_connect import connect
db=connect()

import pandas as pd
import datetime

#筛选视频信息
def select_videos(bid=None, title=None, pubdate_start=None, pubdate_end=None, duration_min=None, duration_max=None,
                  view=None, like=None, coin=None, share=None, danmaku=None, reply=None, favorite=None,
                  uname=None, tags=None,date_order_desc=None,date_order_asc=None):
    cursor = db.cursor()
    query = "SELECT * FROM up_video_info WHERE 1=1"
    # Add conditions based on the input parameters
    if bid:
        query += f" AND bid = '{bid}'"
    if title:
        query += f" AND title LIKE '%{title}%'"
    if pubdate_start:
        if not pubdate_end:
            pubdate_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
    elif date_order_desc:
        query += "ORDER BY pubdate DESC "
    elif date_order_asc:
        query += "ORDER BY pubdate asc "
    elif like:
        query += " ORDER BY like DESC"
    elif coin:
        query += " ORDER BY coin DESC"
    elif share:
        query += " ORDER BY share DESC"
    elif favorite:
        query += " ORDER BY favorite DESC"
    elif danmaku:
        query += " ORDER BY danmaku DESC"
    elif reply:
        query += " ORDER BY reply DESC"
    else:
        query += " ORDER BY view DESC"

    cursor.execute(query)
    print(query)
    result = cursor.fetchall()
    # 转换为dataframe
    columns = [desc[0] for desc in cursor.description]

    # Convert result to DataFrame
    df = pd.DataFrame(result, columns=columns)
    #去除df中bid重复的，保留第一个
    df = df.drop_duplicates(subset=['bid'], keep='first')
    result_json = df.to_json(orient='records', force_ascii=False)

    return result_json


