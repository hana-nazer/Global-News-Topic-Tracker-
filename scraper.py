import requests
from bs4 import BeautifulSoup

def get_google_news():
    url = "https://news.google.com/rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')

    articles = []
    for item in items[:10]:  # Get top 10 headlines
        articles.append({
            'title': item.title.text,
            'link': item.link.text,
            'pubDate': item.pubDate.text,
        })
    return articles
