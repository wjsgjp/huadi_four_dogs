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
    #输入自己的cookie
    cookie=''
    #遍历bv_list文件夹内的所有txt文件
    bv_ids = []
    #改成自己要跑的数据集
    for file in os.listdir('bv_list_1'):
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
        #每第100个存一次
        if len(answer_list)%100==0:
            #存入一次列名就可以了
            print('正在写入第'+str(len(answer_list))+'个')
            answer_df=DataFrame(answer_list)
            # 检查文件是否存在
            if not os.path.exists('answer_1.csv'):
                # 文件不存在，首次写入数据，包含列名
                answer_df.to_csv('answer_1.csv', index=False, encoding='utf_8_sig')
            else:
                # 文件已存在，追加数据，不包含列名
                answer_df.to_csv('answer_1.csv', mode='a', index=False, encoding='utf_8_sig', header=False)
            print(answer_df)
            answer_list=[]


