import urllib.request
import re
import os


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_img(html):
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    # " src="([^"]*\.jpg)".*?>
    imglist = re.findall(p, html)
    print(imglist)
    try:
        os.mkdir("Jing")
    except FileExistsError:
        pass
    os.chdir("Jing")
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = "https://tieba.baidu.com/p/4942551901"
    #print(open_url(url))
    get_img(open_url(url))
