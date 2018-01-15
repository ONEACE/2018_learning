import urllib.request
import re
import time
import random

name=[]
mark=[]

def url_req(url):
    html=urllib.request.urlopen(url)
    return html.read().decode('utf-8')

def catch_name(html):
    xre=r'(<img width="100" alt=")(.+)(" src=")'
    temp_list=re.findall(xre,html)
    for i in temp_list:
        name.append(i[1])
    return name

def catch_mark(html):
    xre = r'(<span class="rating_num" property="v:average">)(.+)(</span>)'
    temp_list = re.findall(xre, html)
    for i in temp_list:
        mark.append(i[1])
    return mark

def mix_name_mark(name1,mark1):
    mix=dict(map(lambda x,y:[x,y],name1,mark1))
    return mix


for i in range(10):
    if i < 1:
        url='https://movie.douban.com/top250'
        html = url_req(url)
        name = catch_name(html)
        mark = catch_mark(html)
        time.sleep(random.random())
    else:
        url='https://movie.douban.com/top250?start=%d&filter='%(25*i)
        html = url_req(url)
        name = catch_name(html)
        mark = catch_mark(html)
        time.sleep(random.random())
result=mix_name_mark(name,mark)
print(result)