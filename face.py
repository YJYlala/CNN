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
    p = r'<img class="mimg".*?src="([^"]*\.jpg)".*?>'
    # " src="([^"]*\.jpg)".*?>
    imglist = re.findall(p, html)
    print(imglist)
    try:
        os.mkdir("Jing")
    except FileExistsError:
        pass
    os.chdir("Jing")
    i = 0
    for each in imglist:
        if i<10:
            filename = each.split("/")[-1]
            urllib.request.urlretrieve(each, filename, None)
            i+=1
        else:
            break




if __name__ == '__main__':
    url = "https://cn.bing.com/images/search?q=%E4%BA%BA%E8%84%B8&qs=n&form=QBILPG&sp=-1&pq=%E4%BA%BA%E8%84%B8&sc=8-2&sk=&cvid=E34E930B92C148BAA50C190BD827DC47"
   # print(open_url(url))
    get_img(open_url(url))

