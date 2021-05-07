import requests
from lxml import etree
import base64
import time
#By ZiHeny

c = input("请输入COOKIE值(fofa_token=xxx)：")
name = input("查询语句：")
name2 = base64.b64encode(name.encode('utf-8'))
num = 0
f = open("./fofa.txt","w+")
while True:
    num += 1
    url = "https://fofa.so/result?page={2}&q={0}&qbase64={1}".format(name,str(name2)[2:-1],num)
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Host": "fofa.so",
        "Referer": "https://fofa.so/",
        "Cookie": "{0}".format(c.replace(": ", "="))
    }
    r = requests.get(url=url,headers=headers).text
    tree = etree.HTML(r)
    div = tree.xpath('//div[@class="rightListsMain"]/div[@class="listAddr"]/div[@class="addrLeft"]/span/a[@target="_blank"]/@href')
    if div == []:
        print('没有更多了');break
    for i in div:
        print(i)
        f.write(i+'\n')
    time.sleep(1)
f.close()

