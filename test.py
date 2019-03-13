# coding=UTF-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import codecs
import urllib3
import random
import certifi

url = 'https://www.dcard.tw/f'

my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
#randdom_header=random.choice(my_headers)
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
#res = requests.get(url)
#print(res.status_code)
#print(res.status_code)
index = 1
tag = ['.PostEntry_title_H5o4d', '.PostEntry_excerpt_2eHlN', '.PostAuthorHeader_meta_331_g', '.PostEntry_comments_2iY8V']
background_tag = ['.PostAuthor_root_3vAJf']
i = 0 #tag index and filename index
save_file_name = ['Top_ten_title.txt', 'Top_ten_content.txt', 'Top_ten_school.txt', 'Top_ten_com_num.txt']
file_list = 1

#tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
#print(res.text)
#soup = BeautifulSoup(res.text, "lxml")
#print (soup.text)
while 1:
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, "lxml")
    Current_time = time.asctime(time.localtime(time.time()))
    i = 0
    while i <= 3:
        for drink in soup.select('{}'.format(tag[i])):
            if index < 31:
                if drink.get_text() != 0:
                    f = codecs.open(str(file_list)+'.'+save_file_name[i], 'a+', "utf-8")
                    if index == 1:
                        f.write('%s \n' % Current_time)
                        print(Current_time)
                        print(index, drink.get_text())
                        f.write('%s %s \n' % (index, drink.get_text()))
                        f.close()
                    else:
                        print(index, drink.get_text())
                        f.write('%s %s \n' % (index, drink.get_text()))
                        f.close()
                    index += 1
                else:
                    print('error to write')
            else:
                break
        i += 1
        index = 1
    if i == 4:
        file_list += 1
        #print(file_list)
        #time.sleep(5)
    time.sleep(1800)



