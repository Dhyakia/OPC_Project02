import requests
import os
import csv
from bs4 import BeautifulSoup

# TODO V.1 : Loop that goes trough all the pages (pagination)
# TODO V.2 : Loop that goes trough all the category
# TODO V.3 : .CSV doc headers output is weird : ',' between every character
# TODO V.3.1 : Why Does the program stop after setting up the header ?!
# TODO V.4 : After all that, make it so it download the picture of the item being scrapped

url = 'http://books.toscrape.com/catalogue/category/books/default_15/page-1.html'
response = requests.get(url)
link_list = []
headers = 'product_page_url%universal_product_code%title%price_including_tax%price_excluding_tax%number_available' \
          '%product_description%category%review_rating%image_url'

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    category_index = soup.find('div', {'class': 'page-header action'}).find('h1')
    '''
    result_per_page = soup.find('form', {'class': 'form-horizontal'}).find('strong')
    '''
    book_link_box = soup.findAll('h3')

    # TODO : For every category in the website / class=nav nav-list / Where 1 is index and 2 to 51 are category

    # TODO : For every page in the category : result_per_page (max 20 per page)
    #  if there's only 1 page = /index.html
    #  if there more than one = /page-1.html

    for h3 in book_link_box:
        link_box = h3.find('a')
        link = link_box['href']
        link_list.append(url + '/../' + link)

with open((category_index.text + '_links.txt'), 'a') as links_file:
    for link in link_list:
        links_file.write(link + '\n')

    with open((category_index.text + '_links.txt'), 'r') as file:
        with open((category_index.text + '_scraps_output.CSV'), 'a', encoding='utf-8') as scraps:

            file_is_empty = os.stat((category_index.text + '_links.txt')).st_size == 0
            writer = csv.writer(scraps, lineterminator='')

            if file_is_empty:
                writer.writerow(headers)
                print('header in place')

        for row in file:
            url_2 = row.strip()
            response2 = requests.get(url_2)

            if response2.ok:
                soup = BeautifulSoup(response2.text, 'lxml')

                # url from above
                upc = soup.find('td')
                title = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
                price_including_tax = soup.find('td').find_next('td').find_next('td').find_next('td')
                price_excluding_tax = soup.find('td').find_next('td').find_next('td')
                number_available = soup.find('td')\
                    .find_next('td').find_next('td').find_next('td').find_next('td').find_next('td')
                product_description = soup.find('article', {'class': 'product_page'})\
                    .find_next('p').find_next('p').find_next('p').find_next('p')
                category = soup.find('ul', {'class': 'breadcrumb'})\
                    .find('li').find('a').find_next('a').find_next('a')
                review_rating_tag = soup.find('div', {'class': 'col-sm-6 product_main'}).find('p')\
                    .find_next('p').find_next('p')
                review_rating = review_rating_tag['class']
                image_url_tag = soup.find('div', {'class': 'item active'}).find('img')
                image_url = image_url_tag['src']

                scraps.write(str(url_2)
                             + '%' + str(upc.text)
                             + '%' + title.text
                             + '%' + str(price_including_tax.text)
                             + '%' + str(price_excluding_tax.text)
                             + '%' + str(number_available.text)
                             + '%' + str(product_description.text)
                             + '%' + str(category.text)
                             + '%' + str(review_rating[1])
                             + '%' + str(image_url) + '\n')

                print('Loop successful')
