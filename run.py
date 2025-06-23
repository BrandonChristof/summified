# Script to run every 24 hours
# Collects top 10 news articles in the past 24 hours, summarizes them, and emails them to a list of recipients

import requests
from bs4 import BeautifulSoup as BS
from reddit_news import News
from summarizer import Summarizer, Summarizer_Llama
from html_generator import get_html_document
from campaign_handler.send_all import send_all

def main():
    news = News(urls_to_skip=["semafor"])
    print("Getting news articles...")
    articles = news.get_top_articles() # Returns list of Article objects
    summarizer = Summarizer_Llama() # Summarizer_Llama for testing
    print("Summarizing Articles...")
    summarizer.summarize_articles(articles)
    html = get_html_document(articles)
    send_all(html, send_campaign=False)
    print("Done!")

if __name__ == '__main__':
    main()
