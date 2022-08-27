from ast import keyword
from email import header
from random import betavariate
from re import X
from turtle import title
import requests
from bs4 import BeautifulSoup
from csv import writer
import re
import pandas as pd


headers = {'User-agent': 'Chrome/103.0.5060.134'}

request = requests.get('https://timesofindia.indiatimes.com/', headers=headers)
html = request.content

soup = BeautifulSoup(html, 'html.parser')

for i in range(1):
    x = input("Enter The news you want to search for: ")


# print(soup.prettify)


class webSracping():
    def toi_news_scrapper(keyword):
        news_list = []
        with open('news_scraping.csv', 'w', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header = ['Index', 'Head Lines', 'Keyword']
            thewriter.writerow(header)
            for h in soup.find_all('a',  class_="linktype1" ): #finds all the header in TOI home
                for i in soup.find('figcaption'):
                    news_title = h.contents[0].text

                #Avoiding duplicates 
                if news_title not in news_list: 
                        if 'Times of India' not in news_title:
                            news_list.append(news_title)

            no_of_news = 0
            keyword_list = [] #list of all the keywords that are in the title
            # Goes through the list and searches for the keyword
            for i, title in enumerate(news_list): #Basically indexing the news
                text = ''
                
                if keyword.lower() in title:
                    text = ' <---------- KEYWORD'
                    no_of_news += 1
                    keyword_list.append(title)

                info = [i + 1, title, text]
                thewriter.writerow(info)

            # Prints the Titles of the articles that contain the keywords
        with open('Searched_news.csv', 'w',encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header1 = ['Keyword', 'Number of articles found']
            thewriter.writerow(header1)
            info1 = [keyword, no_of_news]
            thewriter.writerow(info1)
            header2 = ['Searched News', 'Article Link']
            thewriter.writerow(header2)
                # links_list = soup.find_all('a')
            for i, title in enumerate(keyword_list):
                # # for link in soup.findAll('a', attrs={'href': re.compile("^https://timesofindia.indiatimes.com/")}):
                    # for link in links_list:
                    #     if 'href' in link.attrs:
                for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
            # display the actual urls
            # print(link.get('href')) 
                    info = [title, link.get('href')]
                    thewriter.writerow(info)
            filename = 'news_scraping.csv'
            r = pd.read_csv(filename,nrows=5)
            print(r)

                




    toi_news_scrapper(x)



if __name__ == "__main__":
    webSracping()

# def recent_search_csv():
            # filename = 'Searched_news.csv'
            # r = pd.read_csv(filename,nrows=5)
            # print(r)




# from bs4 import BeautifulSoup
# import requests

# # Creates a header
# headers = {'User-agent': 'Mozilla/5.0'}

# # Requests the webpage
# request = requests.get('https://www.bbc.com/news', headers=headers)
# html = request.content

# # Create some soup
# soup = BeautifulSoup(html, 'html.parser')


# # Used to easily read the HTML that we scraped
# # print(soup.prettify())

# def bbc_news_scraper(keyword):
#     news_list = []

#     # Finds all the headers in BBC Home
#     for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
#         news_title = h.contents[0].lower()

#         if news_title not in news_list:
#             if 'bbc' not in news_title:
#                 news_list.append(news_title)


    # no_of_news = 0
    # keyword_list = []
    # # Goes through the list and searches for the keyword
    # for i, title in enumerate(news_list):
    #     text = ''
    #     if keyword.lower() in title:
    #         text = ' <------------ KEYWORD'
    #         no_of_news += 1
    #         keyword_list.append(title)

    #     print(i + 1, ':', title, text)

    # # Prints the Titles of the articles that contain the keywords
    # print(f'\n--------- Total mentions of "{keyword}" = {no_of_news} ---------')
    # for i, title in enumerate(keyword_list):
    #     print(i + 1, ':', title)


# bbc_news_scraper('covid')