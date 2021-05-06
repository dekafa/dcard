#2021/4/28  Dekafa
#爬取dcard以前資料, 先run dcard_trending_content01.py

import pandas as pd
import requests
from time import sleep
import random

# my package
import article

# 時事版
board = 'trending'
filename = 'dcard_trending.csv'

# 親子版
# board = 'parentchild'
# filename = 'dcard_parentchild.csv'


# 讀取csv最後一篇id 並往下抓100x篇的json
df = pd.read_csv(filename)

for j in range(3):
    last = str(int(df.tail(1).id)) 
    url = 'https://www.dcard.tw/service/api/v2/forums/'+board+'/posts?popular=false&limit=100&before=' + last
    ss = requests.session()
    resq = ss.get(url)
    rejs = resq.json()
    sleep(random.randint(6,10))
    for i in range(len(rejs)):
        df = pd.DataFrame(columns=['id', 'title', 'content', 'time', 'forumname', 'commentcount', 'likecount', 'url'])
        df = df.append(article.content(rejs[i]['id'], board), ignore_index=True)
        df['time'] = df['time'].str.split('T',expand=True)[0]
        print(df.tail(1).url)
        print(df.tail(1).time )
        df.to_csv(filename ,index=False, header=False, mode='a') 
        sleep(random.randint(6,10))
    print('ok')


print('complete')
