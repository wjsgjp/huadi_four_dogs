import json
from time import sleep,time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import DesiredCapabilities
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# options = {
#     'ignore_http_methods': ['GET', 'POST'],  # 提取XHR请求，通常为GET或POST。如果你不希望忽略任何方法，可以忽略此选项或设置为空数组
#     'custom_headers': {
#         'X-Requested-With': 'XMLHttpRequest'  # 筛选XHR请求
#     }
# }







def getOid(bv):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.bilibili.com/video/" + bv)
    sleep(0.5)

    # sleep(5)
    # t1 = time()
    # for request in driver.requests:
    #     if "main?oid=" in request.url and request.response:
    #         print(request.url)
    #         # break
    # t2 = time()
    # print(t2-t1)
    # sleep(10)
    t1=time()
    logs = driver.get_log('performance')
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
                return getOid(bv)
    print(time()-t1)

print(getOid('BV1kr421T7z4'))

