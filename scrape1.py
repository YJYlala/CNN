import requests
r = requests.get("https://www.amazon.cn")


print(r.text)
