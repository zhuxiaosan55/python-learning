import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code", r.status_code)
# API响应存储在一个变量中
response_dict = r.json()
# 打印GitHub一共有多少个仓库
print("total repositories:", response_dict['total_count'])
# 我们获得了多少仓库的数据
repo_dicts = response_dict['items']
print("respositories returned:", len(repo_dicts))
# 研究第一个仓库
repo_dict = repo_dicts[0]
# 打印第一个仓库有几个健
print("\nKeys:", len(repo_dict))
# 打印所有键
for key in sorted(repo_dict.keys()):
    print(key)
# 打印第一个仓库的一些键值
print("\nSelected information about first repository:")
# 打印仓库名
print("Name:", repo_dict['name'])
# 打印所有者的登录名，嵌套
print("Owner:", repo_dict['owner']['login'])
# 打印星星数
print("Stars:", repo_dict['stargazers_count'])
# 打印URL地址
print('Repository:', repo_dict['html_url'])
# 打印创建时间
print('Created:', repo_dict['created_at'])
# 打印更新时间
print("Updated:", repo_dict['updated_at'])
# 打印描述信息
print("Description:", repo_dict['description'])
