# app.py
from flask import Flask, render_template, request, jsonify
from scraper import get_google_news
from summarizer import summarize_articles

app = Flask(__name__)

@app.route("/")
def home():
    articles = get_google_news(limit=10, offset=0)
    summaries = summarize_articles(articles)
    return render_template("index.html", summaries=summaries)

@app.route("/load_news")
def load_news():
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit
    articles = get_google_news(limit=limit, offset=offset)
    summaries = summarize_articles(articles)
    return jsonify(summaries)

if __name__ == "__main__":
    app.run(debug=True)
