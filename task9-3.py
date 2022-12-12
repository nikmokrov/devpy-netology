import requests
from datetime import datetime, timedelta

fromdate = int((datetime.today() - timedelta(days=1)).timestamp())
todate = int((datetime.today()).timestamp())
has_more = True
page = 1
news = []
while has_more:
    url = f"https://api.stackexchange.com/2.3/questions?page={page}&pagesize=25&order=asc&\
            fromdate={fromdate}&todate={todate}&sort=creation&tagged=python&site=stackoverflow"
    # print(url)
    req = requests.get(url)
    items = req.json()['items']
    for item in items:
        news.append({datetime.fromtimestamp(int(item['creation_date'])): item['title']})
    has_more = bool(req.json()['has_more'])
    print(bool(req.json()['has_more']))
    page += 1
print(news)
