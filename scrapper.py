import requests
from bs4 import BeautifulSoup

# TODO : Now that it browse every page of any given category, make it browse EVERY category
# TODO : I might also need to change the way the scripts check the number of page

for page_number in range(10):
    url = 'http://books.toscrape.com/catalogue/category/books/default_15/page-' + str(page_number) + '.html'
    print(page_number)
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')

        link_list = []
        category_index = soup.find('div', {'class': 'page-header action'}).find('h1')
        result_per_page = soup.find('form', {'class': 'form-horizontal'}).find('strong')
        book_link_box = soup.findAll('h3')

        for h3 in book_link_box:
            link_box = h3.find('a')
            link = link_box['href']
            link_list.append(url + '/../' + link)

        with open((category_index.text + '_links.txt'), 'w') as links_file:
            for link in link_list:
                links_file.write(link + '\n')

        with open((category_index.text + '_links.txt'), 'r') as file:
            with open((category_index.text + '_scraps_output.CSV'), 'w', encoding='utf-8') as scraps:

                # TODO : Because it get open every loop as 'w", every page overwrite itself

                for row in file:
                    url2 = row.strip()
                    response2 = requests.get(url2)

                    if response2.ok:
                        soup = BeautifulSoup(response2.text, 'lxml')

                        # TODO : titles should be set-up when the CSV is created(), not every iteration

                        scraps.write('product_page_url%universal_product_code%title%price_including_tax'
                                     '%price_excluding_tax%number_available%product_description%category'
                                     '%review_rating%image_url\n')

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

                        scraps.write(str(url2) + '%'
                                     + str(upc.text) + '%'
                                     + title.text + '%'
                                     + str(price_including_tax.text) + '%'
                                     + str(price_excluding_tax.text) + '%'
                                     + str(number_available.text) + '%'
                                     + str(product_description.text) + '%'
                                     + str(category.text) + '%'
                                     + str(review_rating[1]) + '%'
                                     + str(image_url) + '\n')

                        print('Loop successful')
