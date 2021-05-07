## dcard  2021/05/06

內容為 
爬取dcard 時事版及親子版
存檔為csv or 存進資料庫

### dcard_content01
dcard初爬 爬取文章id, 標題, 內文, 發文時間, 版名, 回文數, 喜歡數, 網址 等欄位

### dcard_content02
爬取dcard以前資料(dcard_content01以前的資料)

### dcard_new_parentchild_content.py dcard_new_trending_content.py
爬取每日新文章，可設定排成每日自動抓資料


### article.py
擷取資料的function

### page.py
擷取網頁上每日更新文章數量的function
