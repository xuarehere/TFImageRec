#-*- coding:utf-8 -*-

import os
import requests
import json
import urllib
import time
import random

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

def getNextPage(url,tags):
    item = json.loads(url)
    nextPage = 'https://api.gotokeep.com/social/v3/hashtag/'+tags+'/timeline?lastId='+item.get("data").get("lastId")+'&sort=heat'
    return nextPage

def downloadPic(url,path):
    html = getHTMLText(url)
    while html == "":
        time.sleep(60 * random.random())
        html = getHTMLText(url)
    with open(path+url.split('/')[-1],'wb') as f:
        f.write(html.content)
        f.close()

def main():
    storagePath = '../datasets/keep_image'

    print('输入爬取页数')
    total_page = input()
    url = 'https://api.gotokeep.com/social/v3/hashtag/'
    print('输入关键字')
    tags = input()
    folderName = tags
    os.chdir(storagePath)
    os.makedirs(folderName, exist_ok=True)
    tags = urllib.parse.quote(tags)
    url = url + tags + '/timeline?sort=heat'
    for i in range(int(total_page)):
        html = getHTMLText(url)
        while html == "":
            time.sleep(60 * random.random())
            html = getHTMLText(url)
        html = html.text
        #print(html)
        postPageList = []
        detailPage = json.loads(html).get("data").get("results")
        lenth = len(detailPage)
        for j in range(lenth):
            #print(json.loads(html))
            if 'photo' in detailPage[j]:
                item = detailPage[j].get("photo")
                postPageList.append(item)
        for postPage in postPageList:
            downloadPic(postPage,'./'+folderName+'/')
        url = getNextPage(html,tags)
        #print(url)
        print("爬取第{0}页面照片数为{1}".format(i+1,len(postPageList)))

if __name__ == '__main__':
    main()