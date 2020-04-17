import requests
r = requests.get("http://www.amazon.cn/")
import  re
pa = re.compile(r'<option.+>(.+?)</option>')
option = pa.findall(r.text)
for get in option:
    print(get)
