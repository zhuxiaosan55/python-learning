from distutils.filelist import findall
import re
from tokenize import group
from unittest import result
'''# findall:匹配字符串所有符合正则的内容，第一个参数是正则，第二个是字符串
lst = re.findall(r"\d+", "我的电话是10086，我女朋友的电话是10010")
print(lst)

# finditer:匹配字符串所有内容并返回迭代器，从迭代器中找到内容用.group
it = re.finditer(r"\d+", "我的电话是10086，我女朋友的电话是10010")
for i in it:
    print(i.group())

#search返回的结果是match对象，拿数据用.group,找到一个结果就返回
s=re.search(r"\d+", "我的电话是10086，我女朋友的电话是10010")
print(s.group())

#match是从头开始匹配，

#预加载正则表达式
obj=re.compile(r"\d+")
ret=obj.findall
'''
# '''不仅可以做注释，还可用于长字符串，不用考虑换行。
s = ''' 
<div class="jay"><span id="1">郭麒麟</span></div>
<div class="jj"><span id="2">张若昀</span></div>
<div class="jolin"><span id="3">宋轶</span></div>
<div class="Bob"><span id="4">大宝</span></div>
'''
# (?P<anything>.*?)把选出来的放在anything里。re.S让匹配可以忽略换行。
obj = re.compile(
    r'<div class=".*?"><span id="\d+">(?P<wahaha>.*?)</span></div>', re.S)
result = obj.finditer(s)
for it in result:
    print(it.group('wahaha'))
