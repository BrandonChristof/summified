from datetime import datetime

category_tags = {
    "politics": r"""<p style="background-color:#F99F4D;float:right;margin: 0px 0px 5px 10px;color: white;border-radius:8px;font-weight:bold;max-width: 80px;text-align: center;font-size: 10px;padding:5px 7px 5px 7px;">Politics</p>""",
    "sports": r"""<p style="background-color:#BA7848;float:right;margin: 0px 0px 5px 10px;color: white;border-radius:8px;font-weight:bold;max-width: 80px;text-align: center;font-size: 10px;padding:5px 7px 5px 7px;">Sports</p>""",
    "worldnews": r"""<p style="background-color:#36B9E1;float:right;margin: 0px 0px 5px 10px;color: white;border-radius:8px;font-weight:bold;max-width: 80px;text-align: center;font-size: 10px;padding:5px 7px 5px 7px;">World News</p>""",
    "technology": r"""<p style="background-color:#70C652;float:right;margin: 0px 0px 5px 10px;color: white;border-radius:8px;font-weight:bold;max-width: 80px;text-align: center;font-size: 10px;padding:5px 7px 5px 7px;">Technology</p>""",
    "entertainment": r"""<p style="background-color:#DB7AB8;float:right;margin: 0px 0px 5px 10px;color: white;border-radius:8px;font-weight:bold;max-width: 80px;text-align: center;font-size: 10px;padding:5px 7px 5px 7px;">Entertainment</p>""",
    "general": r"""<p style="background-color:#B690E4;float:right;margin: 0px 0px 5px 10px;color: white;border-radius:8px;font-weight:bold;max-width: 80px;text-align: center;font-size: 10px;padding:5px 7px 5px 7px;">General</p>""",
}

def get_html(date, titles, categories, summaries, urls):
    html =rf"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Summified</title>
                </head>
                <body style="max-width:600px;font-family: Arial, sans-serif;margin: 0 auto;padding: 20px;background-color:#fff;color: #505050;">
                    <div class="header" style="display: flex;justify-content: space-between;align-items: center;margin-bottom: 10px;">
                        <div class="header-left" style="text-align: left;">
                            <img src="https://i.imgur.com/SLDez2R.png" width="200" height="32">
                            <div class="date" style="font-size: 14px;text-align: left;color: #A1A1A1;">{date}</div>
                        </div>
                    </div>
                    <br><br>
                    <div class="subtitle" style="font-size: 18px;text-align: center;margin-left: auto;margin-right: auto;">Your daily news summary is ready! Here are the top 10 news stories over the last 24 hours:</div>
                    <br><br>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[0]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[0]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[0]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[0]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[1]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[1]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[1]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[1]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[2]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[2]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[2]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[2]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[3]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[3]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[3]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[3]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[4]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[4]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[4]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[4]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[5]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[5]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[5]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[5]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[6]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[6]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[6]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[6]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[7]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[7]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[7]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[7]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[8]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[8]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[8]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[8]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="news-item" style="padding: 30px 25px 0px 5px;margin-bottom: 0px;border-top: 1px solid #ddd;">
                        {category_tags[categories[9]]}
                        <h2 style="font-size: 18px;margin-top: 0;">{titles[9]}</h2>
                        <p class="summary" style="font-size: 13px;color: #777;">{summaries[9]}</p>
                        <div class="source" style="font-size: 12px;color: #999;text-align: right;padding-bottom: 10px;"><a href={urls[9]} style="color: #888;font-weight: bold;">source</a></div>
                    </div>
                    <div class="footer" style="text-align: center;margin-top: 20px;font-size: 12px;color: #666;text-decoration: none;"">
                        <a href="https://buymeacoffee.com/summified" style="color: #888;">Tips are appreciated!</a>
                    </div>
                </body>
                </html>"""
    return html

def suffix(d):
    day_endings = { 1: 'st',
                    2: 'nd',
                    3: 'rd',
                    21: 'st',
                    22: 'nd',
                    23: 'rd',
                    31: 'st'}
    if d in day_endings:
        return day_endings[d]
    else:
        return "th"

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def get_html_document(articles):
    date = custom_strftime('%B {S}, %Y', datetime.now())
    titles = []
    categories = []
    summaries = []
    urls = []
    for article in articles:
        titles.append(article.title)
        categories.append(article.category)
        summaries.append(article.summary)
        urls.append(article.url)
    html = get_html(date, titles, categories, summaries, urls)

    with open("python_html.html", "w", encoding="utf8") as f:
        f.write(html)
    return html
