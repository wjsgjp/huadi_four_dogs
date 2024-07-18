from PIL import Image
import numpy as np
import jieba
import pandas as pd
import wordcloud
import matplotlib.pyplot as plt
# 指定形状图片的路径
def wordcloud_bv(content,bv):

    #将content转为字符串
    content = ' '.join(content)
    # 使用 jieba 分词
    text = content
    text = ' '.join(jieba.cut(text))
    # 去掉停用词
    stopwords = pd.read_csv('D:\\bili\\video_analys\\stopwords.txt', encoding='utf-8')
    stopwords_list = list(stopwords['stopwords'])  # 将停用词转换为列表

    text = ' '.join([word for word in text.split() if word not in stopwords_list])
    # 读取背景图片
    background_image = np.array(Image.open('D:\\bili\\video_analys\\img.png'))

    # 生成词云
    wc = wordcloud.WordCloud(font_path='simsun.ttc', background_color='white', width=1000, height=800, margin=2, mask=background_image)
    wc.generate(text)
    # 显示词
    #保存词云
    wc.to_file(f"D:\\bili\\static\\danmaku_wordcloud\\{bv}.png")
    img_url=f"D:\\bili\\static\\danmaku_wordcloud\\{bv}.png"
    return img_url