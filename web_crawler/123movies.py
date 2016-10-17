#the mighty shiva
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup

def web_crawler(max_page):
    page = 1
    while page <= max_page:
        url = 'http://123movies.to/movie/topimdb/movie/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text ,"html.parser" )
        for link in soup.findAll('a',{'class' : 'ml-mask jt'}):
            href = link.get('href')
            get_title(href)
            print(href)
            page += 1

def get_title(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for title in soup.findAll('li', {'class': 'active'}):
        print(title.string)

web_crawler(1)
#Des's world..