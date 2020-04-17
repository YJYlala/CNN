import multiprocessing
import requests
from requests.exceptions import ConnectionError
def scrape(url):
    try:
        print('抓取%s成功!收到%s'%(url,requests.get(url)))
    except ConnectionError:
        print('抓取%s出错！'%(url))
if __name__ == '__main__':
    pool = multiprocessing.Pool()
    url = [
        'http://www.metro.cn/',
        'http://www.shuichan.cc/',
        'http://wwww.51sole.com',
        'http://wwww.x009.com',
        'http://wwww.x009.comd'
    ]
    pool.map(scrape,url)
