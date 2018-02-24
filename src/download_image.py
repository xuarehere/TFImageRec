#-*- coding:utf-8 -*-

import requests
import time
import random

hearders_android = {
            'Host': 'api.gotokeep.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'x-os-version': '7.1.2',
            'x-channel': 'keep',
            'x-locale': 'zh--CN',
            'x-screen-height': '738',
            'x-is-new-device': 'false',
            'User-Agent': 'Keep+5.5.0%2FAndroid+7.1.2-10289+Xiaomi+Redmi+5+Plus',
            'x-manufacturer': 'Xiaomi',
            'x-keep-timezone': 'Asia/Shanghai',
            'x-timestamp': '1517802215014',
            'x-screen-width': '392',
            'x-os': 'Android',
            'x-device-id': '8663990354679004d13a5e5ed611111171058727',
            'x-version-name': '5.5.0',
            'x-user-id': '5a7847e9e6668651588d3ed0',
            'x-version-code': '10289',
            'x-model': 'Redmi+5+Plus',
            # 'sign':'bbec46d779ed2167b69cf66cf2a430cace097e25'
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NWEwOGRiYjJiNTAwZmZiMzgyNTBkMDYiLCJ1c2VybmFtZSI6IndpbnRlcl95dWFuIiwiYXZhdGFyIjoiaHR0cDovL3N0YXRpYzEua2VlcGNkbi5jb20vYXZhdGFyLzIwMTUvMDYvMTkvMjMvZGM0ODAxMjkwYjdhODNjZDlkMDYzZTNkODhiNGQyNjI0NDhkZmI5Ni5qcGciLCJnZW5kZXIiOiJNIiwiZGV2aWNlSWQiOiI4NjYzOTkwMzU0Njc5MDA0ZDEzYTVlNWVkNjExMTExMTcxMDU4NzI3IiwiaXNzIjoiaHR0cDovL3d3dy5nb3Rva2VlcC5jb20vIiwiZXhwIjoxNTI2NDYwMTY2LCJpYXQiOjE1MTc4MjAxNjZ9.11Jq-3-nbyu0r8nwykMdSlCv7VFeZsfdcQhb7QJDcv0'
        }
def getHTMLText(url, header={}):
    try:
        r = requests.get(url, headers=header, timeout=10)
        return r
    except requests.exceptions.ConnectTimeout:
        print("连接超时")
        return ""
    except requests.exceptions.Timeout:
        print("超时")
        return ""
    except Exception as e:
        print("获取网页失败" + str(e))
        return ""

def downloadPic(url,path):
    html = getHTMLText(url)
    while html == "":
        time.sleep(60*random.random())
        html = getHTMLText(url)
    with open(path+url.split('/')[-1],'wb') as f:
        f.write(html.content)
        f.close()

def main():
    storage_path = '../datasets/keep_image'
    folder_name = 'original_image'
    file = open("../datasets/hot_pic.txt","r",encoding="utf-8")
    itemlist = []
    count = 0
    while 1:
        count += 1
        line = file.readline()
        if not line:
            break
        itemlist = line.split()
        url = itemlist[4]
        downloadPic(url,storage_path+'/'+folder_name+'/')
        if count % 100 == 0:
            print("已经下载了 %d 张图片" % count)
    file.close()

if __name__ == '__main__':
    main()

