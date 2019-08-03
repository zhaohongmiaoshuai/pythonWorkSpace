﻿#_*_ coding:UTF-8 _*_
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36    (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

def judgement_sex(class_name):
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'

def get_links(url):
    wb_data = requests.get(url, headers = headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    links = soup.select('#page_list>ul>li>a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    tittles = soup.select('div.pho_info>h4')
    addresses1 = soup.select('span.pr5')
    addresses = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for tittle, address, price, img, name, sex in zip(tittles, addresses, prices, imgs, names, sexs):
        data = {
            'tittle':tittle.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'img':img.get("src"),
            'name':name.get_text(),
            'sex':judgement_sex(sex.get("class"))
        }
        print(data)

if __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format (number) for number in range(1,14)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)