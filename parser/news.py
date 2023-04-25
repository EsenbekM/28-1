import datetime
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_url(day, month, year):
    base_url = f"https://kaktus.media/?lable=8&order=time&date={year}-{month}-{day}"
    return base_url


# POST, GET, PUT, PATCH, DELETE
def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="Tag--article")
    news = []
    for item in items:
        news.append({
            "title": item.find("a", class_="ArticleItem--name").string,
            "url": item.find("a", class_="ArticleItem--name").get('href'),
            "time": item.find("div", class_="ArticleItem--time").getText(),
            "photo": item.find("a", class_="ArticleItem--image").find("img").\
                get("src").replace("/small/", "/big/")
        })

    return news


def parser(day=None, month=None, year=None):
    current_date = datetime.datetime.now()
    url = get_url(
        day=current_date.day if not day else day,
        month=current_date.month if not month else month,
        year=current_date.year if not year else year
    )
    html = get_html(url)
    if html.status_code != 200:
        raise Exception("Error in parser!")
    data = get_data(html.text)
    return data
