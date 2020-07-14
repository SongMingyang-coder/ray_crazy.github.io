import urllib.request        #导入urllib.request库

b = str(input("输入帖子编码："))
b = "https://api.codemao.cn/web/forums/posts/"+b+"/details"
#提示用户输入信息，并强制类型转换为字符串型
a = urllib.request.urlopen(b)
#打开指定网址
html = a.read()
#读取网页源码
html = html.decode("utf-8")
html = html.replace('false','False')
code = eval(html)

#获取信息
user = code["user"]["nickname"]
title = code["title"]
content = code["content"]

#输出信息
print("===================")
print(user)
print("===================")
print(title)
print("===================")
print(content)
print("===================")