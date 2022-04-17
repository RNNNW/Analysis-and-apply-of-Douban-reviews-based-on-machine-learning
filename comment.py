# coding: utf-8
import requests
import pandas as pd  # 存储文件使用pandas，然后转成csv文件
import re
import time
import html
from bs4 import BeautifulSoup
import os
from urllib import request

if __name__ == '__main__':
    # url请求头文件
    header = {'Content-Type': 'text/html;charset:utf-8',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}
    # 登录cookie
    Cookie = {
        'Cookie': 'bid=F3L-t4rHJlM; douban-fav-remind=1; ll="118254"; push_doumail_num=0; __utmv=30149280.23524; push_noty_num=0; ct=y; __utmc=30149280; __gads=ID=639a2e7b8f5d0738-2249a55230c5009d:T=1607868167:S=ALNI_MYOhWB-LoMruzjufCtem25Z1P3b9w; __utmz=30149280.1618327524.33.16.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/subject/34815432/comments; ap_v=0,6.0; __utma=30149280.59022717.1607868168.1618391458.1618400489.36; __utmt=1; __utmb=30149280.13.5.1618400489; apiKey=; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1618402720%2C%22https%3A%2F%2Fmovie.douban.com%2Fsubject%2F33442331%2F%22%5D; _pk_id.100001.2fad=031e9bfc68946447.1615862166.4.1618402720.1617351880.; _pk_ses.100001.2fad=*; login_start_time=1618402721994; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2213098846394%22%2C%22code%22:%221845%22}; dbcl2="235243654:DD/in3eV6bo'}
    # 构造请求头
    url_1 = 'https://movie.douban.com/subject/30122638/comments?start='
    url_2 = '&limit=20&status=P&sort=new_score'

    # 循环抓取
    i = 0
    while True:
        url = url_1 + str(i * 20) + url_2
        print(url)
        # noinspection PyBroadException
        try:
            res = requests.get(url, headers=header, cookies=Cookie)
            body = html.unescape(res.text).replace("\n", "")
            # body1 = body.replace("\u00a0", "")
            # beautifulsoup解析网址
            soup = BeautifulSoup(body, 'lxml')

            # 评论时间
            comment_time_list = soup.find_all('span', attrs={"class": "comment-time"})
            # 用户名
            user_list = soup.find_all('span', attrs={"class": "comment-info"})
            if len(user_list) == 0:
                break
            # 评论内容
            comment_list = soup.find_all('span', attrs={"class": "short"})
            # 评分
            rating_list = soup.find_all('span', attrs={"class": re.compile(r"allstar(\s\w+)?", re.S)})
            for j in range(len(comment_time_list)):
                data1 = [(comment_time_list[j].text.strip(), user_list[j].a.string,
                          comment_list[j].string, rating_list[j].get('class')[0],
                          rating_list[j].get('title'))]
                if len(comment_list[j].string) < 5:
                    data1.clear()
                data2 = pd.DataFrame(data1)
                data3 = data2.to_csv('douban_moive.csv', header=False, index=False, mode='a+', encoding="utf-8-sig")

        except Exception as e:
            print("wrong")

        print("page" + str(i + 1) + " has finished")
        i = i + 1
        time.sleep(2)
