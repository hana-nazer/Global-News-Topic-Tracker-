from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_articles(articles):
    summaries = []
    for article in articles:
        title = article['title']
        link = article['link']   # include the link
        try:
            result = summarizer(title, max_length=40, min_length=10, do_sample=False)
            summary = result[0]['summary_text']
        except Exception as e:
            summary = f"⚠️ Error: {str(e)}"
        summaries.append({
            'title': title,
            'summary': summary,
            'link': link  # add link here
        })
    return summaries

