from operator import and_
import time
from bs4 import BeautifulSoup
import requests

# print('Enter the news you want to search about')
# search_news = input('>')
# print(f'Filtering out {search_news}')
html_text = requests.get('https://timesofindia.indiatimes.com/').text #website ka URL daalna h..

def main_heading():
    soup = BeautifulSoup(html_text, 'lxml')
    article1 = soup.find_all('div', class_= '_1SDbg')
    # print('Heading News: ')

    for heading_news in article1:
        heading = heading_news.find('div', class_='_1Fkp2 _3hhnu   false')
        for headingcap in soup.find_all('figcaption'):
            headingpart = headingcap.get_text()
            # print(f'News: {headingpart}')
            # print(" ")



def Entertainment():
    soup = BeautifulSoup(html_text, 'lxml')
    ent_article = soup.find_all('div', class_ = '_1A86C')
    # print("Entertainment News:")
    for ent_news in ent_article:
        heading = ent_news.find('div', class_ = 'col_l_8 col_m_12 padR32 _2aV5P')
        for newscap in soup.find_all('figcaption'):
            newspart = newscap.get_text()
            print(f"News: {newspart}")
            print(" ")

# def citynews():
#     soup = BeautifulSoup(html_text, 'lxml')
#     city_article = soup.find_all('div', class_ = "row")
#     print("city_news: ")
#     for city_news in city_article:
#         news_heading1  = city_news.find('div', class_ = 'col_l_3 col_m_3 bdr_right no_bdr_last ')
#         # news_heading2  = city_news.find('div', class_ = 'col_l_3 col_m_3 bdr_right no_bdr_last ')
#         # news_heading3  = city_news.find('div', class_ = 'col_l_3 col_m_3 bdr_right no_bdr_last ')
#         # news_heading4  = city_news.find('div', class_ = 'col_l_3 col_m_3 bdr_right no_bdr_last ')

#         for i in soup.find_all('span'):
#             newsofcity = i.get_text()
#             print(f'City News: {newsofcity}')
#             print(" ")


# def explore():
#     soup = BeautifulSoup(html_text, 'lxml')
#     expo_article = soup.find_all('div', class_ ='_3HWV3')
#     print("Explore Section:")
#     for exp_news in expo_article:
#         article = exp_news.find('figure', class_="_1Fkp2 _2dA8K   false")
#         for explore_news in  soup.find_all('figcaption'):
#             explore_news1 = explore_news.get_text().strip()
#             print(f'News: {explore_news1}')
#             print(" ")


def covid19():
    soup = BeautifulSoup(html_text, 'lxml')
    covid_articles = soup.find_all('div', class_ = '_2ofaX')
    # print('Covid Section:')
    for c19_news in covid_articles:
        news1 = c19_news.find('div', class_ ='col_l_8 col_m_12 padR32  _19nxj')
        for covid19 in soup.find_all('span'):
            covid_news = covid19.get_text()
            # print(f'Covid Updates: {covid_news}')
            # print(" ")

def sports():
    soup = BeautifulSoup(html_text, 'lxml')
    sports_news_articles = soup.find_all('div', class_ = '_2ofaX _1cORx')
    # print("Sports News:")
    for spn in sports_news_articles:
        sp_news =  spn.find('figure', class_ = '_1Fkp2 _2dA8K   false')
        for news in soup.find_all('figcaption'):
            spn1 = news.get_text()
            # print(f'News: {spn1}')
            # print(' ')



def find_articles():
    soup = BeautifulSoup(html_text, 'lxml')
    article1 = soup.find_all('div', class_= '_1SDbg')
    # print(article1)
    for bk_news in article1:
        # published_date = job.find('span', class_ ='sim-posted').span.text
        # if 'few' in published_date:

        first_section = bk_news.find('div', class_="_2r4Y_ _3abpr grid_wrapper")
        # for figcap in soup.find_all('fidcaption'):
            # if search_news in first_section:
            # print(figcap.get_text())
    
        # news_name = bk_news.find('div', class_ = 'col_l_6')
        # skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        # more_info = job.header.h2.a['href']
       
            
        # print(f"Company Nmae: {news_name.strip()}\n")
        # print(f"Requirede Skills: {skills.strip()}\n")
        # print(f'More Infor: {more_info}')
        # print('')

    

if __name__ == '__main__':
    if True:
        find_articles()
        main_heading()
        Entertainment()
        covid19()
        sports()
        # citynews()
        # explore()

        # time_wait = 10
        # print(f'Waiting {time_wait} Minutes...')
        # time.sleep(time_wait*60)