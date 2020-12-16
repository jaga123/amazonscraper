import pandas as pd
from Functions import *
import time

datalist = []

searchterm = input("Enter Search Term: ")

try:
    number_of_pages = int(input("Number of Pages to be Scraped: "))
except:
    print('Error! Should be Number')
    number_of_pages = int(input("Re enter the number of pages to be Scraped: "))

product_category = input("Enter the product category: ")
x = 1
url = f'https://www.amazon.ca/s?k={searchterm}&i={product_category}'
while True:
    soup = geturl(url)
    getdata(soup, datalist)
    url = amazonpagination(soup)
    x = x + 1
    print(x)
    if not url or x > int(number_of_pages):
        print(url)
        break
    else:
        print(url)
        print(len(datalist))
    time.sleep(1)

df = pd.DataFrame(datalist)
df.to_csv(searchterm + product_category + '.csv', encoding='utf-8')
