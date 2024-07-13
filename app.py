from flask import Flask, request
from UP_analys.up_video_analys  import select_videos
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/videos', methods=['GET'])
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
    result_json=select_videos(bid, title, pubdate_start, pubdate_end, duration_min, duration_max,view, like, coin, share, danmaku, reply, favorite,uname, tags)
    return result_json
if __name__ == '__main__':
    app.run()