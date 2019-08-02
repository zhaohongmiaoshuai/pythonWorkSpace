#_*_ coding:UTF-8 _*_
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36    (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

res = requests.get('http://bj.xiaozhu.com/',headers = headers)
print(res)
f = open('C:/Users/zhaoo/Desktop/adasd.txt','w+')
print(res.text)
f.write(res.text)