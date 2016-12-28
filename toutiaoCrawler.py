# -*- coding: utf-8 -*-  

#抓取今日头条图片

import json

import urllib 
import urllib2
import uuid
import os
import sys

url = "http://www.toutiao.com/search_content/?offset=20&format=json&keyword=$keyword&autoload=true&count=20&_=1480675595492"
localPath='/Users/wubaoguo/Pictures/toutiao'  

def downloadImg(url,keyword):
    response = urllib2.urlopen(url.replace('$keyword',keyword)) 
    res = json.loads(response.read().decode())
    #print(res)
    #print(res['data'])
    for colour in res['data']:
        for key in colour:
            if key == 'image_list':
                for k in colour[key]:
                    for url in k:
                        print(k[url])
                        fileName=generateFileName()+'.jpg'  
                        urllib.urlretrieve(k[url],createFileWithFileName(localPath,fileName))  



#生成一个文件名字符串 
def generateFileName():  
    return str(uuid.uuid1()) 

#根据文件名创建文件    
def createFileWithFileName(localPathParam,fileName):  
    totalPath=localPathParam+'/'+fileName  
    if not os.path.exists(totalPath):  
        file=open(totalPath,'a+')  
        file.close()  
        return totalPath  

#输入参数
param = sys.argv[1]

downloadImg(url,param)