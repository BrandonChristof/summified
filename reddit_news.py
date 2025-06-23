import requests
from bs4 import BeautifulSoup as BS
import time
from difflib import SequenceMatcher
from selenium import webdriver

class News():

    CATEGORIES = {0: "general",
                  1: "worldnews",
                  2: "entertainment",
                  3: "technology",
                  4: "sports",
                  5: "politics"}

    def __init__(self, urls_to_skip=[]):
        self.urls = ["https://www.reddit.com/r/news/top/.json",
                     "https://www.reddit.com/r/worldnews/top/.json",
                     "https://www.reddit.com/r/entertainment/top/.json",
                     "https://www.reddit.com/r/technology/top/.json",
                     "https://www.reddit.com/r/sports/top/.json",
                     "https://www.reddit.com/r/politics/top/.json"
                     ]
        self.articles = []
        self.urls_to_skip = urls_to_skip

    def get_top_articles(self, amount=10):
        articles = []
        for idx, url in enumerate(self.urls):
            print(f"Getting {url}")
            while True:
                try:
                    content = requests.get(url).json()
                    content["data"]
                    break
                except (KeyError, ValueError):
                    time.sleep(10)
                    continue
            for post in content["data"]["children"]:
                title = post["data"]["title"]
                category = self.CATEGORIES[idx]
                link = post["data"]["url"]
                score = post["data"]["score"]
                if "redd" in link or any(u in link for u in self.urls_to_skip):
                    continue
                if self.CATEGORIES[idx] == "politics":
                    score = score//2.5
                elif self.CATEGORIES[idx] == "sports":
                    score *= 2
                elif self.CATEGORIES[idx] == "entertainment":
                    score *= 2
                elif self.CATEGORIES[idx] == "worldnews":
                    score = score//1.5
                elif self.CATEGORIES[idx] == "technology":
                    score *= 2
                data = (title, category, link, score)
                articles.append(data)

        top_articles = sorted(articles, key=lambda tup: tup[-1], reverse=True)

        article_data = []
        for article in top_articles:
            article = Article(article[0], article[1], article[2]) # (title, category, link, score)
            if article.text == "":
                print(f"Couldnt get text from {article.url}")
                continue
            for a in article_data:
                seq = SequenceMatcher(None, article.title, a.title).ratio()
                if seq > 0.4:
                    break
            else:
                article_data.append(article)
            if len(article_data) == amount:
                break
        return article_data

class Article():

    TEMP_FILE_NAME = "temp.txt"

    def __init__(self, title, category, url):
        self.driver = webdriver.Chrome()
        self.title = title
        self.category = category
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

        article_text = ""
        article_div = None
        div_list = []
        p_counts = set()
        for div in divs:
            p_count = self.get_paragraph_count(div)
            if p_count not in p_counts:
                div_list.append((div, p_count))
                p_counts.add(p_count)

        ordered_divs = sorted(div_list, key=lambda tup: tup[1])
        max_diff = 0
        for idx in range(1, len(ordered_divs)-1):
            diff = ordered_divs[idx+1][1] - ordered_divs[idx-1][1]
            if diff >= max_diff and ordered_divs[idx][1] > 3:
                max_diff = diff
                article_div = ordered_divs[idx][0]
        if article_div is None:
            return ""
        article_text = "\n".join(e.text for e in article_div.select("p"))
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
        unparsed_text = self.get_reuters_article_text()
        self.write_to_file(unparsed_text)
        return self.read_file()

    def get_reuters_article_text(self):
        divs = self.soup.find_all("div")
        article_text = ""
        for div in divs:
            if div.get("data-testid") is None:
                continue
            if "paragraph" in div.get("data-testid"):
                article_text += div.text + " "
        return article_text
