import requests
url = 'https://www.biquxsw.com/79_79765/59362645.html'
response = requests.get(url)
response.encoding = 'gbk'
print(response.text)
