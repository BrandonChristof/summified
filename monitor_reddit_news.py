import requests
from bs4 import BeautifulSoup as BS
import time
from difflib import SequenceMatcher
from selenium import webdriver
import pickle
from datetime import datetime


class News():

    CATEGORIES = {0: "general",
                  1: "worldnews",
                  2: "entertainment",
                  3: "technology",
                  4: "sports",
                  5: "politics"}

    VIRAL_THRESHOLD = 200


    def __init__(self):
        self.urls = ["https://www.reddit.com/r/news/rising/.json",
                     "https://www.reddit.com/r/worldnews/rising/.json",
                     "https://www.reddit.com/r/politics/rising/.json"]
        self.seen_titles = []


    def viral_index(self, score, num_comments, age):
        return (score / age) + (num_comments/age)

    def monitor_news(self):
        stories = 0
        while True:
            big_story = False
            for url in self.urls:
                while True:
                    try:
                        content = requests.get(url).json()
                        content["data"]
                        break
                    except (KeyError, ValueError):
                        time.sleep(10)
                        continue

                for post in content["data"]["children"]:
                    num_comments = post["data"]["num_comments"]
                    score = post["data"]["score"]
                    age = (time.time() - post["data"]["created_utc"])//60
                    title = post["data"]["title"]
                    link = post["data"]["url"]

                    idx = self.viral_index(score, num_comments, age)

                    if idx > self.VIRAL_THRESHOLD:
                        for seen_title in self.seen_titles:
                            if SequenceMatcher(None, seen_title, title).ratio() > 0.7:
                                break
                        else:
                            self.seen_titles.append(title)
                            article = Article(title, link)
                            big_story = True
                            stories+=1
                            print(datetime.now())
                            print("\n\n\n\nInsane Story!")
                            print(title)
                            print(link)
                            print(article.text)
            if not big_story:
                print(f"{stories} stories so far...")
            time.sleep(30)


class Article():

    TEMP_FILE_NAME = "temp.txt"

    def __init__(self, title, url):
        self.driver = webdriver.Chrome()
        self.title = title
        self.url = url
        self.soup = self.get_soup()
        self.text = self.get_reuters_text() if "reuters" in url else self.get_text()
        self.summary = ""

        self.driver.quit()

    def __str__(self):
        return self.title

    def get_soup(self):
        self.driver.get(self.url)
        return BS(self.driver.page_source, "html.parser")

    def get_article_text(self):

        divs = self.soup.find_all("div")
        articles = self.soup.find_all("article")

        article_text = ""

        if len(articles) > 0:
            for article in articles:
                if self.get_paragraph_count(article) > 3:
                    article_text = "\n".join(e.text for e in article.select("div p"))
                    break
        else:
            for div in divs:
                if self.get_paragraph_count(div) >= 5:
                    article_text = "\n".join(e.text for e in div.select("div p"))
                    break
        return article_text

    def get_paragraph_count(self, div):
        return len(div.find_all("p"))

    def get_text(self):
        unparsed_text = self.get_article_text()
        self.write_to_file(unparsed_text)
        return self.read_file()

    def write_to_file(self, text):
        with open(self.TEMP_FILE_NAME, "w", encoding="utf8") as f:
            f.write(text)

    def read_file(self):
        with open(self.TEMP_FILE_NAME, "r", encoding="utf8") as f:
            lines = f.readlines()
        contents = []
        for line in lines:
            stripped_line = line.rstrip()
            if stripped_line == "":
                continue
            contents.append(line.rstrip())
        contents = " ".join(contents)
        contents = contents.replace("’", "'").replace("‘", "'")
        return contents

    def get_img(self):
        imgs = self.soup.find_all("img")
        pictures = self.soup.find_all("picture")
        main_img_url = None
        main_img_size = 400*300
        for img in imgs:
            w = img.get("width")
            h = img.get("height")
            if None not in (w, h):
                if int(w)*int(h) > main_img_size:
                    main_img_url = img.get("src")
                    main_img_size = int(w)*int(h)
        if main_img_url is None:
            for picture in pictures:
                children = picture.findChildren("source", recursive=False)
                for child in children:
                    w = child.get("width")
                    h = child.get("height")
                    if None not in (w, h):
                        if int(w)*int(h) > main_img_size:
                            main_img_url = child.get("src")
                            main_img_size = int(w)*int(h)
        return main_img_url

    def get_reuters_text(self):
        divs = self.soup.find_all("div")
        article_text = ""
        for div in divs:
            if div.get("data-testid") is None:
                continue
            if "paragraph" in div.get("data-testid"):
                article_text += div.text + " "
        return article_text
