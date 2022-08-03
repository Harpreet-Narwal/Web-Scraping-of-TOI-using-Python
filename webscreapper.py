from ast import keyword
from email import header
from random import betavariate
from re import X
from turtle import title
import requests
from bs4 import BeautifulSoup
from csv import writer


headers = {'User-agent': 'Chrome/103.0.5060.134'}

request = requests.get('https://timesofindia.indiatimes.com/', headers=headers)
html = request.content

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify)
def toi_news_scrapper(keyword):
    news_list = []
    with open('news_scraping.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Index', 'Head Lines', 'Keyword']
        thewriter.writerow(header)
        for h in soup.find_all('a',  class_="linktype1" ):
            for i in soup.find('figcaption'):
                news_title = h.contents[0].text

            if news_title not in news_list:
                    if 'Times of India' not in news_title:
                        news_list.append(news_title)

        no_of_news = 0
        keyword_list = []
        # Goes through the list and searches for the keyword
        for i, title in enumerate(news_list):
            text = ''
            if keyword in title:
                text = ' <------------ KEYWORD'
                no_of_news += 1
                keyword_list.append(title)

            info = [i + 1, title, text]
            thewriter.writerow(info)

        # Prints the Titles of the articles that contain the keywords
        info1 = [keyword, no_of_news]
        thewriter.writerow(info1)
        for i, title in enumerate(keyword_list):
            info = [i + 1, title]
            thewriter.writerow(info)

toi_news_scrapper('Covid')


