# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





#coding=utf-8
import re 
import urllib
import os

html = urllib.request.urlopen('http://qq.yh31.com/zjbq/0551964.html').read().decode('utf-8') 
reg='''<img src="(.*?)"'''
htmls = re.findall(reg,html)
htmls_finall=[]
htmls_finall = ['http://qq.yh31.com'+i for i in htmls]

for i in htmls_finall:
    try:
        path='%s'%i.split('/')[-1]
        if not os.path.exists(path):
            urllib.request.urlretrieve(i,'%s'%i.split('/')[-1])
            print('%s保存成功'%i.split('/')[-1])
        else:
            print('已存在')
    except:
        continue
print('完成')
