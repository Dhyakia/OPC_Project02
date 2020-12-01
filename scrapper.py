import requests
from bs4 import BeautifulSoup

liList = []

for i in range(1, 51):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    response = requests.get(url)

    if response.ok:
        print('Page: ' + str(i) + ' links is being stored')
        soup = BeautifulSoup(response.text, 'lxml')
        h3s = soup.findAll('h3')

        for h3 in h3s:
            a = h3.find('a')
            link = a['href']
            liList.append('http://books.toscrape.com/catalogue/' + link)

            with open('urlsOutput.txt', 'w') as file:
                for link in liList:
                    file.write(link + '\n')


with open('urlsOutput.txt', 'r') as file:
    with open('scrapsOutput.CSV', 'w') as scraps:
        scraps.write('product_page_url,universal_ product_code,title,price_including_tax,price_excluding_tax,'
                     'number_available,product_description,category,review_rating,image_url\n')

    for row in file:
        url = row.strip()
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')

            product_page_url = url
            print(product_page_url)

            upc = soup.find('td')
            print(upc.text)

            title = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
            print(title.text)

            price_including_tax = soup.find('td').find_next('td').find_next('td').find_next('td')
            print(price_including_tax.text)

            price_excluding_tax = soup.find('td').find_next('td').find_next('td')
            print(price_excluding_tax.text)

            number_available = soup.find('p', {'class': 'instock availability'})
            print(number_available.text)

            product_meta_description = soup.find('head').find('meta', {'name': 'description'})
            product_description = product_meta_description['content']
            print(product_description)

            category = soup.find('ul', {'class': 'breadcrumb'}).find('li').find('a').find_next('a').find_next('a')
            print(category.text)

            review_star = soup.find('div', {'class': 'col-sm-6 product_main'}).find('p').find_next('p').find_next('p')
            review_rating = review_star['class']
            print(review_rating)

            image_source = soup.find('div', {'class': 'item active'}).find('img')
            image_url = image_source['src']
            print(image_url)

            scraps.write(product_page_url + ',' + upc.text + ',' + title.text + ',' + price_including_tax.text + ','
                         + price_excluding_tax.text + ',' + number_available + ',' + product_description + ',' +
                         category.text + ',' + review_rating + ',' + image_url.text + '\n')
