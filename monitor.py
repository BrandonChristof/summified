# Script to monitor for big news stories

import requests
from bs4 import BeautifulSoup as BS
from monitor_reddit_news import News
from summarizer import Summarizer, Summarizer_Llama
from html_generator import get_html_document
from campaign_handler.send_all import send_all

def main():
    news = News()
    print("Getting news articles...")
    articles = news.monitor_news() # Monitors for big news stories and prints any

if __name__ == '__main__':
    main()
