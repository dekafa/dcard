import pandas as pd
import json
from sqlalchemy import create_engine

# 時事版
filename = "dcard_trending.csv"
table = 'dcard_trending_content'

# 親子版
# filename = 'dcard_parentchild.csv'
# table = 'dcard_parentchild_content'

df = pd.read_csv(filename)

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
print('ok')