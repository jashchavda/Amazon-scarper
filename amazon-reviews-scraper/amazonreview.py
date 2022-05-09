from sys import version
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import json
from bs4 import SoupStrainer

main_list = []


for x in range(1,99):
    url = f'https://www.amazon.co.uk/product-reviews/B07WD58H6R/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber={x}'
    headers = {'User-Agent': 'put your agent here'}
    r = requests.get(url, headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')

    main_div = soup.find('div',class_='a-section a-spacing-none reviews-content a-size-base')
    main_name = soup.find_all('div',class_='main-name-section-one')
    main_rate = soup.find_all('h1',class_='mais-rate-price')
    
    main_item  = main_div.find_all('div',class_='a-section celwidget')


    for z in main_item:
        name = z.find('span',class_='a-profile-name').text.strip()
        rateing  = z.find('span',class_='a-icon-alt').text.strip()
        reviews = z.find('span',class_='a-size-base review-text review-text-content').text.strip()
        main_haed  = z.find('a',class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').find('span').text.strip()
        
        main_dir = {
            'profile_name':name,
            'ratings': rateing,
            'reviews': reviews,
            'main_reviews': main_haed

        }
        main_list.append(main_dir)
        print(f'current_page{x}')


csv = pd.DataFrame(main_list)
csv.to_csv('data.csv',index=False)
