data = []
out_filename = ''
for i in range(1, 4):
    out_filename += str(i)
    with open(str(i) + '.txt') as file:
        content = file.readlines()
        data.append({'filename': str(i) + '.txt', 'length': len(content), 'content': content})
data.sort(key=lambda x: x.get('length'))

with open(out_filename + '.txt', mode='w', encoding='utf8') as file:
    for f in data:
        print(f['filename'], file=file)
        print(f['length'], file=file)
        file.writelines(f['content'])
