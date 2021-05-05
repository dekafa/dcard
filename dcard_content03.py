#2021/4/30  Dekafa
#爬取每日新資料

import pandas as pd
import requests
from time import sleep
import random

# my package
import article

# 時事版
# board = 'trending'
# filename = 'newdcard_trending.csv'

# 親子版
board = 'parentchild'
filename = 'newdcard_parentchild.csv'

# 自訂文章數量 100內
page = 100

# # 讀取最新100篇(最大)
url = 'https://www.dcard.tw/service/api/v2/forums/'+board+'/posts?popular=false&limit=' + str(page)
ss = requests.session()
resq = ss.get(url)
rejs = resq.json()
df = pd.DataFrame(columns=['id', 'title', 'content', 'time', 'forumname', 'commentcount', 'likecount', 'url'])
for i in range(len(rejs)):
    df = df.append.content(article(rejs[i]['id'], board),ignore_index=True)
    sleep(random.randint(6,10))

df['time'] = df['time'].str.split('T',expand=True)[0]
df.to_csv(filename, index=False, header=True, mode='a')

print(df.shape)
print('complete')