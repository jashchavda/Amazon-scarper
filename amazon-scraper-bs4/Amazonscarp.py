from numpy.lib.shape_base import get_array_prepare
import pandas as pd
from sys import version
from bs4 import BeautifulSoup
import requests
import random
from bs4 import SoupStrainer


main_list=[]
g=0
search_term = 'headphone'
for z in range(1,15):
    url =f'https://www.amazon.in/s?k={search_term}&page={z}'
    print(url)
    headers = {'yout user agent...'}
    r = requests.get(url,headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')

    name  = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
    price = soup.find_all('span',class_='a-price-whole')

    data = soup.find_all('div',class_='a-row a-size-base a-color-secondary s-align-children-center')
    rateings = soup.find_all('span',class_='a-icon-alt')
    imgs = soup.find_all('img',class_='s-image')
    for x in range(0,len(name)):
        title  = name[x].text
        try:
            mal = price[x].text
        except:
            mal = 'no_price'
        try:
            product_data = data[x].text
        except:
            product_data = 'none'
        try:
            rateing = rateings[x].text
        except:
        
            rateing = 'none'
        try:
             img = imgs[x]['src']
        except:
            img = 'Img_link_not_found'
        main_dir = {
            'product_name':title,
            'product_price':mal,
            'product_data':product_data,
            'product_rateing':rateing,
            'img_link':img
        }
        main_list.append(main_dir)
    print(f'printing_page {z}')


h = random.randrange(2,100)
data_frame = pd.DataFrame(main_list)

data_frame.to_csv(f'Amazon_data{h}.csv',index=False)

#new changes to improve speed


# Sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
