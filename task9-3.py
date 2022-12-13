import requests
from datetime import datetime, timedelta

fromdate = int((datetime.today() - timedelta(days=2)).timestamp())
todate = int((datetime.today()).timestamp())
has_more = True
page = 1
news = []
while has_more:
    url = f"https://api.stackexchange.com/2.3/questions?page={page}&pagesize=20&order=asc\
    &fromdate={fromdate}&todate={todate}&sort=creation&tagged=python&site=stackoverflow"
    req = requests.get(url)
    if req.status_code != 200:
        break
    items = req.json()['items']
    for item in items:
        news.append((datetime.fromtimestamp(int(item['creation_date'])), item['title']))
    has_more = bool(req.json()['has_more'])
    page += 1

print('All news tagged with Python in the last 2 days:')
for item in news:
    print(item[0], item[1])
print(f'Total pages: {page-1}')
