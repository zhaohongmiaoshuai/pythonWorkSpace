#_*_ coding:UTF-8 _*_
import csv
fp = open('C:/Users/zhaoo/Desktop/csvtest.csv','w+',newline='')
#newline='' 可以解决空行问题

writer = csv.writer(fp)
writer.writerow(('id', 'name'))
writer.writerow(('1', 'xiaoming'))
writer.writerow(('2', 'haha'))
writer.writerow(('3', 'dsdasdfa'))