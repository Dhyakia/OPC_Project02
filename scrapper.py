import requests
import csv
import wget
from bs4 import BeautifulSoup

starting_url = 'http://books.toscrape.com/'
response = requests.get(starting_url)

if response.ok:
    link_list = []
    soup = BeautifulSoup(response.text, 'lxml')
    category_link_box = soup.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').findAll('li')

    for category_tag in category_link_box:
        category_box = category_tag.find('a')
        category_link = category_box['href']
        category_url = (starting_url + category_link)

        category_response = requests.get(category_url)
        category_soup = BeautifulSoup(category_response.text, 'lxml')

        category_name = category_soup.find('li', {'class': 'active'})
        book_link_box = category_soup.findAll('h3')

        # TODO : Last objective left -> pages loop

        for book_tag in book_link_box:
            book_box = book_tag.find('a')
            book_link = book_box['href']
            link_list.append(category_url + '/../' + book_link)

            with open('Books_to_scrape_items_links.txt', 'w') as links_file:
                for link in link_list:
                    links_file.write(link + '\n')

        with open('Books_to_scrape_items_links.txt', 'r') as file:
            with open((category_name.text + '_scraps_output.CSV'), 'w', encoding='latin1', newline='') as scraps:

                writer = csv.writer(scraps, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

                header = "product_page_url", "universal_product_code", "title", "price_including_tax", \
                         "price_excluding_tax", "number_available", "product_description", "category", \
                         "review_rating", "image_url", "\n"

                writer.writerow(header)

                for row in file:
                    url_2 = row.strip()
                    response2 = requests.get(url_2)

                    if response2.ok:
                        soup = BeautifulSoup(response2.text, 'lxml')

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
                        image_url_suffix = image_url_tag['src']
                        image_url = (url_2 + '/../' + image_url_suffix)

                        scrap_data = f"{str(url_2)}", f"{str(upc.text)}", f"{str(title.text)}",\
                                     f"{str(price_including_tax.text)}", f"{str(price_excluding_tax.text)}", \
                                     f"{str(number_available.text)}", f"{str(product_description.text)}", \
                                     f"{str(category.text)}", f"{str(review_rating[1])}", \
                                     f"{str(image_url)}", "\n"

                        writer.writerow(scrap_data)
                        '''
                        image_data = wget.download(image_url)
                        '''
                        print(' Loop successful')
