from flask import Flask, render_template
from scraper import get_google_news
from summarizer import summarize_articles

app = Flask(__name__)

@app.route("/")
def home():
    articles = get_google_news()
    summaries = summarize_articles(articles)
    return render_template("index.html", summaries=summaries)

if __name__ == "__main__":
    app.run(debug=True)
