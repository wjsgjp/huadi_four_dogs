#连接mysql数据库
import pymysql
import pandas as pd
from database_connect import connect
db=connect()

def recommend_video(partition):
    cursor = db.cursor()
    #写一个sql语句
    if partition=="all":
        sql = "select * from videos_rank order by `rank` limit 100"
    else:
        sql = f"select * from videos_rank where `par`='{partition}' order by `rank` limit 100"
    cursor.execute(sql)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Convert result to DataFrame
    df = pd.DataFrame(result, columns=columns)
        #去除profile里的空格与回车
    df = df.drop_duplicates(subset=['bid'], keep='first')
    result_json = df.to_json(orient='records', force_ascii=False)
    return result_json