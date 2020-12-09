import requests
import csv
from bs4 import BeautifulSoup

# TODO : Loop that goes trough all the category
# TODO : Change the delimitation character in the csv file (QUOTE.MINIMAL) from import csv - % cause some things to bug
# TODO : Finally, Download the picture of the item being scrapped

url = 'http://books.toscrape.com/catalogue/category/books/default_15/index.html'
response = requests.get(url)
link_list = []

# TODO : For every category in the website / class=nav nav-list / Where 1 is index and 2 to 51 are category

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    category_name = soup.find('div', {'class': 'page-header action'}).find('h1')

    result_per_page = soup.find('form', {'class': 'form-horizontal'}).find('strong')
    page_number = 1

    book_link_box = soup.findAll('h3')
    '''
    if int(result_per_page.text) > 20:
        for result_per_page in soup:
            url = (url + '/../page-' + str(page_number + 1) + '.html')
            page_number += 1
            print(url)'''

    for h3 in book_link_box:
        link_box = h3.find('a')
        link = link_box['href']
        link_list.append(url + '/../' + link)

        with open((category_name.text + '_links.txt'), 'w') as links_file:
            for link in link_list:
                links_file.write(link + '\n')

    with open((category_name.text + '_links.txt'), 'r') as file:
        with open((category_name.text + '_scraps_output.CSV'), 'w', encoding='utf-8') as scraps:

            # TODO : Need to find a way to "quote" without getting out of cell

            writer = csv.writer(scraps, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL)

            writer.writerow("product_page_url" + "," + "universal_product_code" + "," + "title" + ","
                            + "price_including_tax" + "," + "price_excluding_tax" + "," + "number_available" + ","
                            + "product_description" + "," + "category" + "," + "review_rating" + "," + "image_url"
                            + "\n")

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

                    writer.writerow('' + str(url_2) + ","
                                    + str(upc.text) + ","
                                    + title.text + ","
                                    + str(price_including_tax.text) + ","
                                    + str(price_excluding_tax.text) + ","
                                    + str(number_available.text) + ","
                                    + str(product_description.text) + ","
                                    + str(category.text) + ","
                                    + str(review_rating[1]) + ","
                                    + str(image_url) + ","
                                    + '\n')

                    print('Loop successful')
