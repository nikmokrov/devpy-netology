import json
import collections


with open('newsafr.json', encoding='utf8') as file:
    content = json.load(file)

cnt = collections.Counter()
for news in content['rss']['channel']['items']:
    for word in news['description'].split():
        if len(word) > 6:
            cnt[word] += 1
print('Top-10 слов длиннее 6 символов:')
for elem in cnt.most_common(10):
    print(f'"{elem[0]}" встретилось {elem[1]} раз')
