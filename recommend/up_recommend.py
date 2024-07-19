#连接mysql数据库
import pymysql
import pandas as pd
from database_connect import connect
db=connect()

def recommend_up_like(partition):
    cursor = db.cursor()

    # 写一个sql语句
    if partition == "all":
        sql = "select * from up_rank  limit 100"
    else:
        sql = f"select * from up_rank where `par`='{partition}'  limit 100"
    cursor.execute(sql)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Convert result to DataFrame
    df = pd.DataFrame(result, columns=columns)
    # 去除profile里的空格与回车
    result_json = df.to_json(orient='records', force_ascii=False)
    return result_json


def recommend_up_inter(partition):
    cursor = db.cursor()

    # 写一个sql语句
    if partition == "all":
        sql = "select * from up_rank_inter  limit 100"
    else:
        sql = f"select * from up_rank_inter where `par`='{partition}'  limit 100"
    cursor.execute(sql)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Convert result to DataFrame
    df = pd.DataFrame(result, columns=columns)
    # 去除profile里的空格与回车
    result_json = df.to_json(orient='records', force_ascii=False)
    return result_json