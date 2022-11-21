import xml.etree.ElementTree as ET
import collections

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_items = root.findall("channel/item")

cnt = collections.Counter()
for elem in xml_items:
    for word in elem.find("description").text.split():
        if len(word) > 6:
            cnt[word] += 1
print('Top-10 слов длиннее 6 символов:')
for elem in cnt.most_common(10):
    print(f'"{elem[0]}" встретилось {elem[1]} раз')
