from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(100):
    url= base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), 'url:',base_url+ his[-1])
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("(?=^/item)/item/(%.{2})+$")})
    print ('爬到了'+str(i+1))
    if len(sub_urls) != 0 :
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        if len(his)==1:
            pass
        else:
            his.pop()