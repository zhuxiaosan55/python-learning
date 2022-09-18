from os import write
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)


with open("/Users/slk/Documents/code/python/claw/mybaidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")
