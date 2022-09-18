from re import S
import requests
url = "https://fanyi.baidu.com/sug"
s = input("请输入你要翻译的单词：")
dat = {
    "kw": s
}

# 发送Post请求,发送的数据必须放在字典中，通过data来传送。
resp = requests.post(url, data=dat)
print(resp.json())  # 将服务器返回的内容处理成json()
