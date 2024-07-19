from PIL import Image
import numpy as np
import jieba
import pandas as pd
import wordcloud
import pymysql
from database_connect import connect
db=connect()
import matplotlib.pyplot as plt
# 指定形状图片的路径
def wordcloud_bv(content,bv):

    #将content转为字符串
    content = ' '.join(content)
    # 使用 jieba 分词
    text = content
    text = ' '.join(jieba.cut(text))
    # 去掉停用词
    stopwords = pd.read_csv('video_analys/stopwords.txt', encoding='utf-8')
    stopwords_list = list(stopwords['stopwords'])  # 将停用词转换为列表

    text = ' '.join([word for word in text.split() if word not in stopwords_list])
    print(text)
    # 读取背景图片
    background_image = np.array(Image.open('video_analys/img.png'))

    # 生成词云
    wc = wordcloud.WordCloud(font_path='simsun.ttc', background_color='white', width=1000, height=800, margin=2, mask=background_image)
    wc.generate(text)
    # 显示词
    #保存词云
    wc.to_file(f"static/danmaku_wordcloud/{bv}.png")
    img_url=f"static/danmaku_wordcloud/{bv}.png"
    return img_url


def get_pubdate(bv):
    cursor=db.cursor()
    sql=f"select pubdate from up_video_info where bid='{bv}'"
    cursor.execute(sql)
    result=cursor.fetchall()
    #转换为dataframe
    result=pd.DataFrame(result)
    print("result")
    print(result)
    # 将pubdate转换为字符串
    pubdate=result[0][0]
    print("pubdate")
    print(pubdate)
    #pubdate只保留年月日
    pubdate=pubdate.strftime('%Y-%m-%d')

    print(pubdate)
    #转换为字符串
    pubdate=str(pubdate)
    print(pubdate)
    return pubdate