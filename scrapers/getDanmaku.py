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
        'cookie': 'buvid3=4A0421A6-20F9-29DB-5D32-D6673056E9BF31924infoc; b_nut=1718016531; _uuid=1D65FAE2-6A86-46C3-610105-9BECC2B3859F32633infoc; enable_web_push=DISABLE; DedeUserID=48002287; DedeUserID__ckMd5=be7b54b6f8c02f7a; header_theme_version=CLOSE; rpdid=0zbfVGbwlN|emrFgv9m|34P|3w1SgCAz; CURRENT_QUALITY=80; fingerprint=6f18e1821ef7aaf9e9dafaa65e4fb2e1; buvid_fp_plain=undefined; buvid4=540E941F-F4C2-4E75-25A7-6135D0C343ED32675-024061010-%2BoqH4JWpvfIOkbWcOWAb2uGZwrqLAPoF9BKMMtVS3dbhvHdeJA0PPF4D%2BJlhZeVU; LIVE_BUVID=AUTO5017193226842845; is-2022-channel=1; CURRENT_BLACKGAP=0; PVID=1; buvid_fp=6f18e1821ef7aaf9e9dafaa65e4fb2e1; home_feed_column=5; hit-dyn-v2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjExMzIxODEsImlhdCI6MTcyMDg3MjkyMSwicGx0IjotMX0.rGsF2g-1F59q-li7SzieOeQHBuxmWuod5jyCLAPmBPQ; bili_ticket_expires=1721132121; SESSDATA=7b8f2a35%2C1736427340%2C2ea2a%2A72CjCA-DToinsih4Q3dJ3G-_IDzgOFUY3Rdj_FfH1W81zVNoC3_-exBkiaHAzAMmYWDYUSVmw0NEh2X09jS1hmREtMc0JpS1c2azZ2Zmc1enpUZDFJTVVwemptR2h3ckJKcmhlcml1X0U5QTA5QnVzS0tpZWVGdFhTVl9kWGwtcF9XNkozLVFidm1RIIEC; bili_jct=5a7127cf5ac87fc687b42175f38c4d12; sid=4kqg0i5i; CURRENT_FNVAL=4048; bp_t_offset_48002287=954034329476923392; b_lsid=1810B8F58_190B1D9533B; browser_resolution=1612-470'
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

getDanmaku('BV17b421e7Ei', '2024-7-16')
