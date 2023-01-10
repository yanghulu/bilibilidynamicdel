# -*- coding: utf-8 -*-
import json

import requests
import io


headers={
"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"content-length": "35",
"content-type": "application/json;charset=UTF-8",
"cookie": "填写自己的cookie",
 "origin": "https://space.bilibili.com",
"referer": "https://space.bilibili.com/408182292/dynamic",
"sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
def del1(items0):
    data2={
        "dyn_id_str":items0
    }
    y=requests.post("https://api.bilibili.com/x/dynamic/feed/operate/remove?csrf=删除一条获取",headers=headers,data=json.dumps(data2))
    x=y.text.encode("utf-8").decode("utf-8","ignore")
#w等于需要删除的动态条数
w=100
i=1
while i<=w:
    z = requests.get('https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&host_mid=自己的uuid&timezone_offset=-480')
    data = z.text.encode("utf-8").decode("utf-8","ignore")
    number1 = json.loads(data)
    data1 = number1["data"]
    items0 = data1["items"][0]["basic"]["comment_id_str"]
    del1(items0)
    print("正在删除第"+str(i)+"条动态")
    i+=1

