#2021/4/27  Dekafa
#dcard初爬 爬取最新文章id, 標題, 內文, 發文時間, 版名, 回文數, 喜歡數, 網址 等欄位

import pandas as pd
import requests
from time import sleep
import random

# my package
import article

#時事版
board = 'trending'
filename = 'dcard_trending.csv'

#親子版
# board = 'parentchild'
# filename = 'dcard_parentchild.csv'

# # 讀取最新100篇(最大)
url = 'https://www.dcard.tw/service/api/v2/forums/'+board+'/posts?popular=false&limit=100'
ss = requests.session()
resq = ss.get(url)
rejs = resq.json()
df = pd.DataFrame()
for i in range(len(rejs)):
    df = df.append(article(rejs[i]['id']),ignore_index=True)
    sleep(random.randint(6,10))

df['time'] = df['time'].str.split('T',expand=True)[0]
df.to_csv(filename, index=False)

print(df.shape)
print('complete')
# print(df)
