import os
import time

import pandas as pd
from pandas import DataFrame

from bili_api import get_info, get_video_tags, get_video_pages, get_subtitles_from_url, get_user_access_details


def get_details(bvid,cookie):
    details = {}
    info = get_info(bvid, cookie)
    details['bid'] = info['bvid']
    details['pic']=info['pic']
    details['title']=info['title']
    timeArray = time.localtime(info['pubdate'])
    details['pubdate']=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    details['duration']=info['duration']
    details['view']=info['stat']['view']
    details['like']=info['stat']['like']
    details['coin']=info['stat']['coin']
    details['share']=info['stat']['share']
    details['danmaku']=info['stat']['danmaku']
    details['reply']=info['stat']['reply']
    details['favorite'] = info['stat']['favorite']
    details['uid'] = info['owner']['mid']
    details['uname'] = info['owner']['name']
    tags=get_video_tags(bvid,cookie)
    details['tags']=''
    for tag in tags:
        details['tags']+=tag['tag_name']+','
    details['tags']=details['tags'].strip(',')
    for key,value in details.items():
        print(key,value)
    return details




if __name__ == '__main__':
    cookie = "buvid3=A751A73D-DBDA-6890-2F5A-60EE66A85E0D93918infoc; b_nut=1720701893; b_lsid=C12347E5_190A1D35096; bsource=search_google; _uuid=B74DBF7E-E1106-CB36-1065C-334BB275D2FC98915infoc; buvid_fp=9b7d108cf00d7f97f7ffbd588730ca3d; enable_web_push=DISABLE; header_theme_version=undefined; home_feed_column=5; browser_resolution=1500-779; buvid4=DBC0E74A-FB3F-8B93-CCCE-CEA898EE6FEC98795-024071112-CkhKDGXh6Nqs6RpQ3vXuqg%3D%3D; SESSDATA=d8516f23%2C1736253936%2Ccfe77%2A71CjCVdvbqrLsNn_nD7jK0f-VoZ2vdC7nr03N9SMpJndn8-p17i31RA3Jmi40C5Ky_nv0SVnZXNGN0a2RCMG5WZzI2STE3SE5vbEs2ODJMS2R4Z0lDdklSRFpuS2Z5aDJpUi04UUJmdTdKdHUyZGoteGgtcUc5WGl2aXFiQkwyNXhjaUZRUm10S2VBIIEC; bili_jct=7f3d5de0a19f8b9b6ba7d3b9d37a39a9; DedeUserID=646950291; DedeUserID__ckMd5=0f62835e2c322395; sid=8l4jp2mr; bp_t_offset_646950291=952896691424460800; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjA5NjEzNTQsImlhdCI6MTcyMDcwMjA5NCwicGx0IjotMX0.ioKzXoMHCYwXuX0nV8flMaomQTqrG_kvbxhfIRvh9B4; bili_ticket_expires=1720961294; CURRENT_FNVAL=4048; rpdid=|(J~J)Rumu|l0J'u~k|~|kul~"  # 替换为你的b站cookies, 或者将cookies写入bilibili_api/cookies.txt
    #遍历bv_list文件夹内的所有txt文件
    bv_ids = []
    for file in os.listdir('bv_list'):
        if file.endswith('.txt'):
            with open('bv_list/'+file, 'r') as f:

                bvid_list = f.read().splitlines()
                bv_ids.extend(bvid_list)
    print(bv_ids)
    answer_list=[]
    for bvid in bv_ids:
        time.sleep(0.5)
        answer=get_details(bvid,cookie)
        #存入列表
        answer_list.append(answer)

    answer_df=pd.DataFrame(answer_list)
    answer_df.to_csv('answer.csv',index=False,encoding='utf_8_sig')
