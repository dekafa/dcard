#2021/5/5  Dekafa
#爬取每日時事版新資料

import pandas as pd
import requests
from time import sleep
import random
from bs4 import BeautifulSoup
import json
from sqlalchemy import create_engine

# my package
import page
import article


# 時事版
board = 'trending'
filename = 'newdcard_trending.csv'
table = 'dcard_trending_content'
url = 'https://www.dcard.tw/f/trending'


# 取得每日新增篇數
page = page.get_page(url)

## 讀取每日篇數
url = 'https://www.dcard.tw/service/api/v2/forums/'+board+'/posts?popular=false&limit=' + page
ss = requests.session()
resq = ss.get(url)
rejs = resq.json()
df = pd.DataFrame(columns=['id', 'title', 'content', 'time', 'forumname', 'commentcount', 'likecount', 'url'])
for i in range(len(rejs)):
    df = df.append(article.content(rejs[i]['id'], board),ignore_index=True)
    sleep(random.randint(6,10))

df['time'] = df['time'].str.split('T',expand=True)[0]
df.to_csv(filename, index=False, header=True, mode='a')
print(df.shape)

secretFile = json.load(open('.vscode/mysql.json', 'r', encoding='utf-8'))
dbHost = secretFile['host']
dbUser = secretFile['user']
dbPassword = secretFile['password']
dbPort = secretFile['port']
dbName = secretFile['dbName']
engine = create_engine('mysql+pymysql://' + dbUser + ':' + dbPassword + '@' +
                       dbHost + ':' + dbPort + '/' + dbName)
conn = engine.connect()

df.to_sql(table, conn, index=False, if_exists='append')
conn.close()
engine.dispose()

print('complete')