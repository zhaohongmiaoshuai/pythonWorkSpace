#_*_ coding:UTF-8 _*_
import requests
from bs4 import BeautifulSoup
import time

f = open('C:/Users/zhaoo/Desktop/NetWormtest2.txt','w+',encoding='UTF-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

def get_info(url):
    wb_data = requests.get(url, headers = headers)
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for rank, title, time in zip(ranks, titles, times):
        data={
            'rank' : rank.get_text().strip(),
            'singer' : title.get_text().split('-')[0],
            'song' : title.get_text().split('-')[1],
            'time' : time.get_text().strip()
        }
        print(data)
        f.write(data.get('rank')+"\t|")
        f.write(data.get('singer')+"\t|")
        f.write(data.get('song')+"\t|")
        f.write(data.get('time'))
        f.write("\n")

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(2)
    f.close()