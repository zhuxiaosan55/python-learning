import requests
url = "https://www.sogou.com/web?query=周杰伦"
dic = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
resp = requests.get(url, headers=dic)  # 反爬
print(resp.text)
