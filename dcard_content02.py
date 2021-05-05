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


# 讀取csv最後一篇id
# 先抓100篇存進空白df

df = pd.DataFrame(columns=['id', 'title', 'content', 'time', 'forumname', 'commentcount', 'likecount', 'url'])

df1 = pd.read_csv(filename)
last1 = str(int(df1.tail(1).id))
url = 'https://www.dcard.tw/service/api/v2/forums/' + board + '/posts?popular=false&limit=100&before=' + last1
ss = requests.session()
resq = ss.get(url)
rejs = resq.json()
for a in range(len(rejs)):
    df = df.append(article.content(rejs[a]['id'], board), ignore_index=True)
    sleep(random.randint(6,10))
print('ok')

# 讀取上述df的最後1個id 讀取迴圈往下爬

for j in range(1):
    last = str(int(df.tail(1).id)) # 找出爬出資料的最後一筆ID
    url = 'https://www.dcard.tw/service/api/v2/forums/'+board+'/posts?popular=false&limit=100&before=' + last
    resq = ss.get(url)
    rejs = resq.json()
    for i in range(len(rejs)):
        df = df.append(article.content(rejs[i]['id'], board), ignore_index=True)
        sleep(random.randint(6,10))
    print('ok')

df['time'] = df['time'].str.split('T',expand=True)[0]

df.to_csv(filename ,index=False, header=False, mode='a') 

print(df.shape)  #(100(x+1), 8)
print('complete')