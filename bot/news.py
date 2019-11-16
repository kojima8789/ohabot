import requests
from bs4 import BeautifulSoup
#
#
# def get_yahoo_news():
#     url = 'https://www.yahoo.co.jp/'
#     res = requests.get(url)
#     content = res.content
#     soup = BeautifulSoup(content, 'html.parser')
#     sponsors = soup.find_all("a")
#
#     for sponsor in sponsors:
#         if 'pickup' in sponsor['href']:
#             news =(sponsor['href'])
#             return news
# if __name__ == '__main__':
#     get_yahoo_news()

from bs4 import BeautifulSoup
import urllib.request
import json
import requests

url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/67.0.3396.99 Safari/537.36 '

def get_yahoo_news():
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find('div', attrs={'class': 'topicsMod'})
    topics = main.select("li > a")

    count = 0
    list = []

    for topic in topics:
        if topic.contents[0].find(word) > -1:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1
    if count == 0:
        list.append("記事が見つかりませんでした！！")

    ns = '\n'.join(list)
    return ns