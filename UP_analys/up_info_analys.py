#连接mysql数据库
#连接mysql数据库
from functools import reduce
from hashlib import md5
import urllib.parse
import time
import requests
import pymysql
db = pymysql.connect(host='localhost', user='root', password='18921190757ytk', database='zion')
import pandas as pd

import datetime

# 查询Up主
def select_up_info(name=None, profile=None, fans_limit=None, likes=None, plays=None, uid=None):
    cursor = db.cursor()
    query = "SELECT * FROM up_info WHERE 1 = 1"
    if uid:
        query += f" AND uid = '{uid}'"
    if name:
        query += f" AND name LIKE '%{name}%'"
    if profile:
        query += f" AND profile LIKE '%{profile}%'"

    if fans_limit:
        # 按照粉丝数量排序
        query += f" AND fans>= '{fans_limit}  "

    if likes:
        # 按照点赞数量排序
        query += f" ORDER BY likes DESC"
    elif plays:
        # 按照播放数量排序
        query += f" ORDER BY plays DESC"
    else:
        query += f" ORDER BY fans DESC"


    cursor.execute(query)
    print(query)
    result = cursor.fetchall()
    # 转换为dataframe
    columns = [desc[0] for desc in cursor.description]
    # Convert result to DataFrame
    df = pd.DataFrame(result, columns=columns)
    result_json = df.to_json(orient='records', force_ascii=False)
    return result_json
#获取UP主头像
def get_img_url(mid):
    # Wbi签名相关函数
    mixinKeyEncTab = [
        46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
        33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
        61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
        36, 20, 34, 44, 52
    ]

    def getMixinKey(orig: str):
        '对 imgKey 和 subKey 进行字符顺序打乱编码'
        return reduce(lambda s, i: s + orig[i], mixinKeyEncTab, '')[:32]

    def encWbi(params: dict, img_key: str, sub_key: str):
        '为请求参数进行 wbi 签名'
        mixin_key = getMixinKey(img_key + sub_key)
        curr_time = round(time.time())
        params['wts'] = curr_time  # 添加 wts 字段
        params = dict(sorted(params.items()))  # 按照 key 重排参数
        # 过滤 value 中的 "!'()*" 字符
        params = {
            k: ''.join(filter(lambda chr: chr not in "!'()*", str(v)))
            for k, v
            in params.items()
        }
        query = urllib.parse.urlencode(params)  # 序列化参数
        wbi_sign = md5((query + mixin_key).encode()).hexdigest()  # 计算 w_rid
        params['w_rid'] = wbi_sign
        return params

    def getWbiKeys() -> tuple[str, str]:
        '获取最新的 img_key 和 sub_key'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'Referer': 'https://www.bilibili.com/'
        }
        resp = requests.get('https://api.bilibili.com/x/web-interface/nav', headers=headers)
        resp.raise_for_status()
        json_content = resp.json()
        img_url: str = json_content['data']['wbi_img']['img_url']
        sub_url: str = json_content['data']['wbi_img']['sub_url']
        img_key = img_url.rsplit('/', 1)[1].split('.')[0]
        sub_key = sub_url.rsplit('/', 1)[1].split('.')[0]
        return img_key, sub_key

    # 获取最新的 img_key 和 sub_key
    img_key, sub_key = getWbiKeys()

    # 替换为您的目标用户 mid 和 SESSDATA
    # mid = 623906369
    sessdata = "buvid3=70245222-8B53-FE5E-2312-00AE0056DB4A91540infoc; b_nut=1719119091; _uuid=B2E14C3A-E99E-2B26-10D103-E1096BC7A10CC699940infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; rpdid=|(umuk|J|lmk0J'u~umuumu|); fingerprint=44e040ac4c0fc6494559a898f04bf612; buvid_fp_plain=undefined; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjA5NDQzODIsImlhdCI6MTcyMDY4NTEyMiwicGx0IjotMX0.eCUNj7d6qpda8ho1Ud8awgIDRsvUY1dQZKy1EJnIHfo; bili_ticket_expires=1720944322; is-2022-channel=1; SESSDATA=ba575631%2C1736237829%2Ccdb91%2A72CjDhmrtavbJ9AFa-U8dteooD7ZuOxOAyiyoDWfSrCaBFWi4xMKidwDx4ICiLjGU0cYQSVnBGRktOVkFOSjNuZURLNDhVb09Zc3hVb0o5OFVrOTZ3NTdhTThLY0xVbWpHRjJPZlpaeVBsc0hkQmRIdkZ5clNqTGhzQVVIVkFCYjJVeUVnci1PQW5BIIEC; bili_jct=301a43873b2582027a3d41563cc37826; DedeUserID=1099677556; DedeUserID__ckMd5=092525581a2bebff; CURRENT_BLACKGAP=0; buvid4=EE264535-D31F-70BE-84FA-1013E49EF32457766-024021605-UGqFWAacUD6T%2BsjFcxWADQ%3D%3D; CURRENT_FNVAL=4048; buvid_fp=44e040ac4c0fc6494559a898f04bf612; bsource=search_bing; bp_t_offset_1099677556=953657660845064192; home_feed_column=4; browser_resolution=273-844; b_lsid=510A6F107B_190AC63C978"

    # 设置请求参数
    params = {
        'mid': mid
    }

    # 使用 Wbi 签名
    signed_params = encWbi(params, img_key, sub_key)

    # 请求头
    headers = {
        'Cookie': f"SESSDATA={sessdata}",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }

    # 发送 GET 请求
    response = requests.get('https://api.bilibili.com/x/space/wbi/acc/info', params=signed_params, headers=headers)

    # 解析 JSON 响应
    data = response.json()

    # 检查响应
    if data['code'] == 0:
        # 获取头像链接
        avatar_url = data['data']['face']
        print(f"用户头像链接: {avatar_url}")
    else:
        print(f"请求失败: {data['message']}")

    return avatar_url

#为up_info表中的每个uid生成头像链接
def generate_avatar_urls():
    cursor = db.cursor()
    query = "SELECT uid FROM up_info"
    cursor.execute(query)
    result = cursor.fetchall()
    #增加一列
    query = f"ALTER TABLE up_info ADD COLUMN img_url text AFTER name"
    cursor.execute(query)
    for row in result:
        uid = row[0]
        avatar_url = get_img_url(uid)
        update_query = f"UPDATE up_info SET img_url = '{avatar_url}' WHERE uid = {uid}"
        cursor.execute(update_query)
        db.commit()