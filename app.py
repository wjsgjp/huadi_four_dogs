import time

from flask import Flask, request, render_template, url_for, jsonify
from UP_analys.up_video_analys  import select_videos
from UP_analys.up_info_analys import select_up_info
from markupsafe import escape
from user_analys.distribution import get_user_img_url,get_user_heat_map_url
from scrapers.getDanmaku import  getDanmaku
from video_analys.wordcloud import wordcloud_bv
from recommend.video_recommend import recommend_video
from recommend.up_recommend import recommend_up_inter,recommend_up_like
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/up/videos', methods=['GET'])
def select_video():
    bid = request.args.get('bid')
    title = request.args.get('title')
    pubdate_start = request.args.get('pubdate_start')
    pubdate_end = request.args.get('pubdate_end')
    duration_min = request.args.get('duration_min')
    duration_max = request.args.get('duration_max')
    view = request.args.get('view')
    like = request.args.get('like')
    coin = request.args.get('coin')
    share = request.args.get('share')
    danmaku = request.args.get('danmaku')
    reply = request.args.get('reply')
    favorite = request.args.get('favorite')
    uname = request.args.get('uname')
    tags = request.args.get('tags')
    date_order_desc=request.args.get('date_order_desc')
    date_order_asc=request.args.get('date_order_asc')
    result_json=select_videos(bid, title, pubdate_start, pubdate_end, duration_min, duration_max,view, like, coin, share, danmaku, reply, favorite,uname, tags,date_order_desc,date_order_asc)
    return result_json


@app.route('/up',methods=['GET'])
def select_up():
    # 获取参数
    #按照up主名字搜索
    name=request.args.get('name')
    # 按照up主简介搜索
    profile=request.args.get('profile')
    # 按照up主uid搜索
    uid = request.args.get('uid')
    # 按照粉丝数搜索（下界）
    fans_limit=request.args.get('fans_limit')
    # 按照up主点赞数降序
    likes=request.args.get('likes')
    # 按照up主播放数降序
    plays=request.args.get('plays')
    result_json=select_up_info(name,profile,fans_limit,likes,plays,uid)
    return result_json


@app.route('/user_analys',methods=['GET'])
def user_analys():
    user_png=get_user_img_url()
    img_urls=[ ]
    for filename in user_png:
        img_urls.append(url_for('static', filename=filename))
    return jsonify({'image_url': img_urls})
@app.route('/video_analys',methods=['GET'])
def video_analys():
    #获取想要展示的分区名字
    partition_nanme=request.args.get('partition_name')
    return "123"

@app.route('/recommend_videos',methods=['GET'])
def recommend_videos():
    partition=request.args.get('partition')
    result=recommend_video(partition)
    return result

@app.route('/recommend_ups',methods=['GET'])
def recommend_ups():
    partition=request.args.get('partition')
    order=request.args.get('order')
    if order=='like':
        return recommend_up_like(partition)
    if order=='inter':
        return recommend_up_inter(partition)

@app.route('/danmu_wordcloud',methods=['GET'])
def danmu_wordcloud():
    bv=request.args.get('bv')
    date=request.args.get('date')
    start_time=time.time()
    danmakulist=getDanmaku(bv,date)
    print(time.time()-start_time)
    print("="*50)
    start_time=time.time()
    img_url=wordcloud_bv(danmakulist,bv)
    print(time.time()-start_time)
    print("="*50)
    return jsonify({'image_url': img_url})

if __name__ == '__main__':
    app.run()