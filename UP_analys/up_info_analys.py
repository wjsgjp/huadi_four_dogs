#连接mysql数据库
#连接mysql数据库
import pymysql
db = pymysql.connect(host='localhost', user='root', password='18921190757ytk', database='zion')
import pandas as pd

import datetime
#计算UP主的视频总播放量
def calculate_up_viewcount(userid):
    cursor = db.cursor()
    #计算同一个uid的所有播放量
    sql=f" select sum(view) from up_video_info where uid={userid}"
    cursor.execute(sql)
    result=cursor.fetchall()
    result_df=pd.DataFrame(result)
    return result_df

#计算UP主视频总点赞量
def calculate_up_likecount(userid):
    cursor = db.cursor()
    #计算同一个uid的所有播放量
    sql=f" select sum(`like`) from up_video_info where uid={userid}"
    cursor.execute(sql)
    result=cursor.fetchall()
    result_df=pd.DataFrame(result)
    return result_df