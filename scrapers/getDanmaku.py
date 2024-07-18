import requests
import re
import datetime
import time
import json
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def getOid(bv):
    option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    option.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    option.add_argument("--headless")
    # caps = DesiredCapabilities.CHROME
    # caps["goog:loggingPrefs"] = {"performance": "ALL"}
    driver = webdriver.Chrome(options=option)
    # print(1)
    driver.get("https://www.bilibili.com/video/" + bv)
    time.sleep(0.5)
    t1=time.time()
    logs = driver.get_log('performance')
    url_list = []
    for packet in logs:
        message = json.loads(packet.get('message')).get('message')  # 获取message的数据
        if message.get('method') != 'Network.responseReceived':  # 如果method 不是 responseReceived 类型就不往下执行
            continue
        # packet_type = message.get('params').get('response').get('mimeType')  # 获取该请求返回的type
        # requestId = message.get('params').get('requestId')  # 唯一的请求标识符。相当于该请求的身份证
        url = message.get('params').get('response').get('url')  # 获取 该请求  url
        if 'oid=' in url:
            pattern = r'oid=(.*?)&'
            match = re.search(pattern, url)
            if match is not None:
                return match.group(1)
            else:
                print(False)
                return getOid(bv)
    print(time.time()-t1)

def getDanmaku(bv, curDate):
    # content_list存放所有弹幕
    oid = getOid(bv)
    print(oid)
    content_list = []
    curYear = int(curDate.split('-')[0])
    curMonth = int(curDate.split('-')[1])
    curDay = int(curDate.split('-')[2])
    # 爬取开始日期和结束日期范围内的弹幕
    cur = datetime.date(curYear, curMonth, curDay)
    url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={oid}&date={cur}'
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'cookie':"buvid3=70245222-8B53-FE5E-2312-00AE0056DB4A91540infoc; b_nut=1719119091; _uuid=B2E14C3A-E99E-2B26-10D103-E1096BC7A10CC699940infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; rpdid=|(umuk|J|lmk0J'u~umuumu|); fingerprint=44e040ac4c0fc6494559a898f04bf612; buvid_fp_plain=undefined; is-2022-channel=1; CURRENT_BLACKGAP=0; buvid4=EE264535-D31F-70BE-84FA-1013E49EF32457766-024021605-UGqFWAacUD6T%2BsjFcxWADQ%3D%3D; bp_t_offset_1099677556=953923562270359552; DedeUserID=646950291; DedeUserID__ckMd5=0f62835e2c322395; bsource=search_bing; SESSDATA=daf4ca2d%2C1736759006%2C1879e%2A72CjCfIhaMDdldO2x1WxfrN6aRopUvo_8vz1C33J_j1Sxg9XVIPtwDpMO6TJdbtV7ZzJsSVmFPYzhyQkd2bDVGOU9aQUNIdHktakhVSXBNb0dHUE45aEhXcEJSMTBRcU4zYXEtQTBwREtnMTE0WXFEU1ByOXVLMDFJRlBlMEVlaTl5dUpNODZ4SV9RIIEC; bili_jct=08b669ea54230527630abe8e18cae476; sid=6d07aqc6; LIVE_BUVID=AUTO3417212073685102; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE0NjY1NzAsImlhdCI6MTcyMTIwNzMxMCwicGx0IjotMX0.xEBwrf8gzNfsUi69r0c67CxmT9wyoHU0Y6ewOz1iNRM; bili_ticket_expires=1721466510; PVID=1; CURRENT_FNVAL=4048; buvid_fp=44e040ac4c0fc6494559a898f04bf612; bp_t_offset_646950291=955130675713802240; b_lsid=DEB105AF3_190C47F4215; home_feed_column=4; browser_resolution=696-830"
        }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    temp_list = re.findall('[\u4e00-\u9fa5]+', response.text)
    content_list.extend(temp_list)
    print("爬取", cur, "日弹幕,获取到：", len(temp_list), "条弹幕，已经增加到总列表。总列表共有", len(content_list),
              "条弹幕。")
    print(content_list)
    # 保存数据
    content = '\n'.join(content_list)
    return content_list


