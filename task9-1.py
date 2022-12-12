import requests

url = "https://superheroapi.com/api/2619421814940190/"
heroes = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
for hero in heroes.keys():
    request = f"search/{hero}"
    req = requests.get(url+request)
    if req.status_code == 200:
        data = req.json()
        if data.get('response', '') == 'success':
            # print(data)
            hero_intelligence = data.get('results', '')[0].get('powerstats', '').get('intelligence', '')
            heroes[hero] = int(hero_intelligence)
hero_max = max(heroes, key=heroes.get)
print(hero_max, heroes[hero_max])
