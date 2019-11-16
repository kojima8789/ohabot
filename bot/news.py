import requests
from bs4 import BeautifulSoup


def get_yahoo_news():
    url = 'https://www.yahoo.co.jp/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all("a")

    for sponsor in sponsors:
        if 'pickup' in sponsor['href']:
            news =(sponsor['href'])
            return news
if __name__ == '__main__':
    get_yahoo_news()