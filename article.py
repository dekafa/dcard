import pandas as pd
import requests

def content(id, board):
    link = 'https://www.dcard.tw/service/api/v2/posts/' + str(id)
    ss = requests.session()
    requ = ss.get(link )
    rejs = requ.json()
    return(pd.DataFrame(
        data=
        [{
            'id':rejs['id'], 
            'title':rejs['title'], 
            'content':rejs['content'],
            'time':rejs['createdAt'],
            'forumname':rejs['forumName'],
            'commentcount':rejs['commentCount'],
            'likecount':rejs['likeCount'],
            'url':'https://www.dcard.tw/f/'+ board +'/p/'+str(id)
            }],
            columns=['id', 'title', 'content', 'time', 'forumname', 'commentcount', 'likecount', 'url']
            ))


