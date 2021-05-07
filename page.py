import requests
from bs4 import BeautifulSoup


# 每日篇數
def get_page (url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    ss = requests.session()
    res = ss.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    page_title = soup.find("div", {"class":"n2egih-3 iBropO"})
    for p in page_title.findAll():
        p.decompose()
    page = page_title.text[4:-4]
    return page