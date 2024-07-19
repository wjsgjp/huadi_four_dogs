#连接mysql数据库
#连接mysql数据库
import os
from functools import reduce
from hashlib import md5
import urllib.parse
import time
import requests
import pymysql
from database_connect import connect
db=connect()
import pandas as pd

import datetime

# 查询Up主
def select_bangumi(name=None, profile=None, fans_limit=None, score_limit=None,score_people=None, plays=None,tags=None,danmaku=None,start_time=None,end_time=None):
    cursor = db.cursor()
    query = "SELECT * FROM bangumi WHERE 1 = 1"
    if name:
        query += f" AND name LIKE '%{name}%'"
    if profile:
        query += f" AND profile LIKE '%{profile}%'"

    if fans_limit:
        # 按照粉丝数量排序
        query += f" AND fans>= {fans_limit}  "
    if score_limit:
        query += f" AND score>= {score_limit}  "
    if start_time:
        if not end_time:
            end_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query += f" AND start_time BETWEEN '{start_time}' AND '{end_time}'"
    if tags:
        query += f" AND tags LIKE '%{tags}%'"


    #排序
    if danmaku:
        # 按照点赞数量排序
        query += f" ORDER BY danmaku DESC"
    elif plays:
        # 按照播放数量排序
        query += f" ORDER BY plays DESC"
    elif score_people:
        query += f" ORDER BY score_people DESC"
    else:
        #先按照评分排序，评分相同按照fans排序
        query += f" ORDER BY score DESC,fans DESC"



    cursor.execute(query)
    print(query)
    result = cursor.fetchall()
    # 转换为dataframe
    columns = [desc[0] for desc in cursor.description]
    # Convert result to DataFrame
    df = pd.DataFrame(result, columns=columns)
    #去除profile里的空格与回车
    df['profile'] = df['profile'].apply(lambda x: x.replace('\n', '').replace(' ', ''))
    result_json = df.to_json(orient='records', force_ascii=False)
    return result_json
