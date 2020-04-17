import os
import random
import urllib.request


def imgs(url):
    try:
        rep = urllib.request.Request(url)
        res = urllib.request.urlopen(rep)
        html = res.read().decode("utf-8", 'ignore')
        # print(html)
        import re

        from bs4 import BeautifulSoup

        web = BeautifulSoup(html, features="html.parser")

        img = web.select("img[src*=/uploads/allimg/]")

        for s in img:
            img_url = "http://pic.netbian.com" + s.get("src")
            file_path = 'D:/book/img'
            file_name = "img" + str(int(random.uniform(20, 10) * 10 ** 14))
            if not os.path.exists(file_path):
                # 创建路径
                os.makedirs(file_path)
                # 获得图片后缀
            file_suffix = os.path.splitext(img_url)[1]
            print(file_suffix)
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
            print(filename)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, filename=filename)
    except:
        print("重复")



i = 1
try:
    while i < 1092:
        url = "http://pic.netbian.com/index"
        if i == 1:
            url += ".html"
        else:
            url += "_" + str(i) + ".html"
        imgs(url)
        i += 1
except:
    print("错误")

