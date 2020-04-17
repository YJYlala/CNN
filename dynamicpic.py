# python 3.6.3
import re
import os
from urllib import parse
from urllib import request

###################################################
# 搜索关键字   下载数量  存放路径
word = '人脸'
num = 10
path = 'C:/Users/10732/Desktop/img/'
###################################################
# 网页地址  正则表达式
url = ('https://image.baidu.com/search/acjson?'
       'tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&'
       'queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&'
       'word={word}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&'
       'pn={pn}&rn=30&gsm=5a&1516945650575=')
pattern = '"thumbURL":"(.+?\.jpg)"'


###################################################
# 输入需要下载数量和关键字  返回获取所有url
def geturls(num, word):
    word = parse.quote(word)
    urls = []
    pn = (num // 30 + 1) * 30
    for i in range(30, pn + 1, 30):
        urls.append(url.format(word=word, pn=i))
    return urls


# 输入需要下载数量和urls 返回所有图片
def getimgs(num, urls):
    imgs = []
    reg = re.compile(pattern)
    for url in urls:
        page = request.urlopen(url)
        code = page.read()
        code = code.decode('utf-8')
        imgs.extend(reg.findall(code))
        # print(code)
    return imgs


# 下载图片
if not os.path.exists(path):
    print('路径不正确')
    os._exit()
urls = geturls(num, word)
imgs = getimgs(num, urls)

i = 0
for img in imgs:
    i = i + 1
    request.urlretrieve(img, path + '%s.jpg' % i)
    # print(img)
    print('成功下载第' + str(i) + '个图片')
    if i >= num:
        break

################问题#####################
# 1.parse.quote(word) 要把关键字转成url
# 2.url 正则表达式 要细心
# 3.注意图片的url 有的不能访问

################总结#####################
# 1.先分析动态网页请求图片的url 分析url参数并仿照着请求
# 2.成功后解析返回的数据 可以选用正则表达式提取需要的数据
# 3.使用所提取到的数据