#_*_ coding:UTF-8 _*_
import requests
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

info_lists = []

def judgement_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'

def get_info(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i> 好笑</span>', res.text, re.S)
#    laughs = re.findall('<i class="number">(\d+)</i> 好笑">', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {
            'id':id.strip(),
            'level':level.strip(),
            'sex':judgement_sex(sex),
            'content':content.strip(),
            'laugh':laugh.strip(),
            'comment':comment.strip()
        }
        info_lists.append(info)

if __name__ == "__main__":
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,10)]
    for url in urls:
        get_info(url)
        for info_list in info_lists:
            f = open('C:/Users/zhaoo/Desktop//Retest/qiushi.txt','a+',encoding='UTF-8')
            try:
                f.write('id:'+info_list['id']+'\n')
                f.write('年龄：'+info_list['level']+'\n')
                f.write('性别：'+info_list['sex'] + '\n')
                f.write('内容：'+info_list['content'] + '\n')
                f.write('好笑数：'+info_list['laugh'] + '\n')
                f.write('评论数：'+info_list['comment'] + '\n\n')
                f.close()

            except UnicodeEncodeError:
                pass