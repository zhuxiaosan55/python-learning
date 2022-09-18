from multiprocessing.sharedctypes import Value
import re
import requests
import csv
urls = ["https://book.douban.com/tag/%E6%8E%A8%E7%90%86", "https://book.douban.com/tag/%E6%8E%A8%E7%90%86?start=20",
        "https://book.douban.com/tag/%E6%8E%A8%E7%90%86?start=40"]
dic = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

mylists = []


for i in urls:
    pages = requests.get(url=i, headers=dic)
    page_content = pages.text  # 必须转换成此格式，否则，result=obj.finditer(pages)会数据类型错误。
    # print(pages.text)

    obj = re.compile(
        r' <div class="info">.*?<h2 class="">.*?<a href=.*?title="(?P<name>.*?)".*?<div class="pub">(?P<author>.*?)</div>'
        r'.*?<span class="rating_nums">(?P<score>.*?)</span>.*?<span class="pl">(?P<readers>.*?)</span>', re.S)
    result = obj.finditer(page_content)

    for it in result:
        '''print(it.group('name'))          # name记得打引号
        print(it.group('author').strip())
        print(it.group('score').strip())
        print(it.group('readers').strip())'''
        mylists.append(it.group(('name')))
        mylists.append(it.group(('author')).strip())
        mylists.append(it.group(('score')).strip())
        mylists.append(it.group(('readers')).strip())

for i in mylists:
    print(i)

f = open("data.csv", mode="w", newline='')
csvwriter = csv.writer(f)
for low in mylists:
    csvwriter.writerow([low])
f.close()
print("over!")
