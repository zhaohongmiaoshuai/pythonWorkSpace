#_*_ coding:UTF-8 _*_
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36    (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

res = requests.get('http://bj.xiaozhu.com/',headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.find_all('li', attrs={"class":"list_li"}))
prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
for price in prices:
    print(price.get_text())