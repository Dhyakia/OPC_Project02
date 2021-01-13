import requests
import csv
import os
import wget
from bs4 import BeautifulSoup

starting_url = 'http://books.toscrape.com/'
response = requests.get(starting_url)

# need to re-write using methods

if response.ok:
    page_counter = 1
    soup = BeautifulSoup(response.text, 'lxml')
    category_link_list = soup.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').findAll('li')

    for category_tag in category_link_list:
        link_list = []
        category_box = category_tag.find('a')
        category_link = category_box['href']
        category_url = (starting_url + category_link)

        fresh_response = requests.get(category_url)
        fresh_soup = BeautifulSoup(fresh_response.text, 'lxml')
        category_name = fresh_soup.find('li', {'class': 'active'})

        next_page_banner_exist = fresh_soup.find('li', {'class': 'next'})

        if next_page_banner_exist:
            loop_condition = 1

            while loop_condition == 1:
                multi_page_url = (category_url + '/../page-' + str(page_counter) + '.html')

                next_page_requests = requests.get(multi_page_url)
                fresh_soup = BeautifulSoup(next_page_requests.text, 'lxml')

                next_button_check = fresh_soup.find('li', {'class': 'next'})

                book_link_box = fresh_soup.findAll('h3')

                for book_tag in book_link_box:
                    book_box = book_tag.find('a')
                    book_link = book_box['href']
                    book_link_updated = book_link.replace('../../../', '')
                    link_list.append('http://books.toscrape.com/catalogue/' + book_link_updated)

                    with open('Books_to_scrap_items_links.txt', 'w') as links_file:
                        for link in link_list:
                            links_file.write(link + '\n')

                if next_button_check:
                    page_counter += 1
                else:
                    loop_condition = 0
                    page_counter = 1

        else:
            book_link_box = fresh_soup.findAll('h3')

            for book_tag in book_link_box:
                book_box = book_tag.find('a')
                book_link = book_box['href']
                book_link_updated = book_link.replace('../../../', '')
                link_list.append('http://books.toscrape.com/catalogue/' + book_link_updated)

                with open('Books_to_scrap_items_links.txt', 'w') as links_file:
                    for link in link_list:
                        links_file.write(link + '\n')

        with open('Books_to_scrap_items_links.txt', 'r') as file:
            with open(('CSV/' + category_name.text + '_scraps_output.CSV'), 'w', encoding='latin1', newline='') as scraps:

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

                        # dic Writer

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

                        image_data = wget.download(image_url)
                        string_title = str(title.text)
                        string_encode = string_title.encode("ascii", 'ignore')
                        string_decode = string_encode.decode()
                        os.rename(image_data, 'Images/' + string_decode.replace("<", "").replace(">", "")
                                  .replace(":", "").replace('"', "").replace("/", "").replace("\\", "")
                                  .replace("|", "").replace("?", "").replace("*", "") + ".jpg")

else:
    print("ERROR || connection error \n")
    print("ERROR || Html content : " + response.content)
