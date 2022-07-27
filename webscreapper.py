

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
    # print(f'Heading News: ')

    for heading_news in article1:
        heading = heading_news.find('div', class_='_1Fkp2 _3hhnu   false')
        for headingcap in soup.find_all('figcaption'):
            headingpart = headingcap.get_text()
            # print(f'News: {headingpart}')
            # print(" ")



def Entertainment():
    soup = BeautifulSoup(html_text, 'lxml')
    ent_article = soup.find_all('div', class_ = '_1A86C')
    print("Entertainment News:")
    for ent_news in ent_article:
        heading = ent_news.find('div', class_ = 'col_l_8 col_m_12 padR32 _2aV5P')
        for newscap in soup.find_all('figcaption'):
            newspart = newscap.get_text()
            print(f"News: {newspart}")
            print(" ")




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
        # time_wait = 10
        # print(f'Waiting {time_wait} Minutes...')
        # time.sleep(time_wait*60)