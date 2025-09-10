# scraper.py
import requests
from bs4 import BeautifulSoup

def get_google_news(limit=12, offset=0):
    url = "https://news.google.com/rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')

    articles = []
    for item in items[offset:offset+limit]:
        articles.append({
            'title': item.title.text,
            'link': item.link.text,
            'pubDate': item.pubDate.text,
        })
    return articles
