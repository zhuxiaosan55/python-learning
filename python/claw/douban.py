import requests
url = "https://movie.douban.com/j/chart/top_list"
param = {  # 将URL？后的封装，从Playload下的query string params中找参数。
    "type": "10",  # 字典记得打逗号。
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 100,
}  # 多行注释三行引号

dic = {  # 代理反爬
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

}
resp = requests.get(url=url, params=param, headers=dic)
print(resp.text)
# with open("/Users/slk/Documents/code/python/claw/top_movies", mode="w", encoding='utf-8') as f:
#   f.write(resp.read().decode("utf-8"))   #
resp.close()  # 关掉
