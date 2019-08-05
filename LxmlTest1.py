#_*_ coding:UTF-8 _*_
import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

url = 'http://www.qiushibaike.com/text/'
res = requests.get(url, headers = headers)
selector = etree.HTML(res.text)
url_infos = selector.xpath('//div[starts-with(@class,"article block untagged mb15 typs")]')
for url_info in url_infos:
    id = url_info.xpath('div[1]/a[2]/h2/text()')[0]
    print(id)
