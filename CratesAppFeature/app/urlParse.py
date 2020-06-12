'''

A script that takes attributes: picture, price, title and descsription of a url of an item
If missing attribute skip it.

'''
import requests
import re
from bs4 import BeautifulSoup
import uuid

import os
import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

supported = ["komplett", "elgiganten", "matas", "zalando"]

class FetchItem():
    def fetch(self, page):

        domain = re.findall(r"https://www.(\w+).", page)
        if domain and domain[0] in supported:
            if domain[0] == supported[0]:
                try:
                    r = requests.get(page, headers=headers)
                except requests.exceptions.RequestException:
                    return False

                soup = BeautifulSoup(r.content, 'html.parser')
                # get the title
                title = soup.find("h1", {"class": "product-main-info-webtext1"})
                # get the price
                price = soup.find("span", {"class": "product-price-now"})
                # get the discription
                price = price.text
                price = price.replace(',-', '')
                price = price.replace('.', '')

                # get image
                image = soup.find_all('img', class_='absolute-center swiper-lazy')
                image_path = 'https://komplett.dk'+str(image[0]['data-src'])

                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)

                id = uuid.uuid1()

                fullfilename = os.path.join('C:\\Users\\augus\\OneDrive\\Skrivebord\\CratesAppFeature\\app\\static', str(id))

                urllib.request.urlretrieve(image_path, fullfilename+'.jpg')


                return {'body':str(title.text), 'price': price, 'image': str(id)}
            
            elif domain[0] == supported[1]:
                try:
                    r = requests.get(page, headers=headers)
                except requests.exceptions.RequestException:
                    return False

                soup = BeautifulSoup(r.content, 'html.parser')
                # get the title
                title = soup.find("h1", {"class": "product-title"})

                # get the price
                price = soup.find("div", {"class": "product-price-container"})
                price = price.text
                price = price.replace(u'\xa0', '')

                # get image
                image = soup.find_all('img', class_='first-product-image')
                image_path = 'https://elgiganten.dk'+str(image[0]['src'])

                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)

                id = uuid.uuid1()

                fullfilename = os.path.join('C:\\Users\\augus\\OneDrive\\Skrivebord\\CratesAppFeature\\app\\static', str(id))

                urllib.request.urlretrieve(image_path, fullfilename+'.jpg')

                return {'body':str(title.text), 'price': price, 'image': str(id)}
            
            elif domain[0] == supported[2]:
                try:
                    r = requests.get(page, headers=headers)
                except requests.exceptions.RequestException:
                    return False

                soup = BeautifulSoup(r.content, 'html.parser')
                # get the title
                title = soup.find("span", class_= "breadcrumb__text js-csquare-currentBreadcrumbText")
                # title = soup.find_all('img', class_='product-page__image-large')
                # title = title[0]['alt']

                # get the price
                price = soup.find("div", {"class": "product-page__price"})
                price = price.text
                price = price.replace(u'\n', '')
                price = price.replace(u' kr.', '')
                price = price.replace(u',', '.')

                # get the image url
                image = soup.find_all('img', class_='product-page__image-large')
                image_path = image[0]['src']

                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)

                id = uuid.uuid1()

                fullfilename = os.path.join('C:\\Users\\augus\\OneDrive\\Skrivebord\\CratesAppFeature\\app\\static', str(id))

                urllib.request.urlretrieve(image_path, fullfilename+'.jpg')

                return {'body':str(title.text), 'price': price, 'image': str(id)}

            elif domain[0] == supported[3]:
                try:
                    r = requests.get(page, headers=headers)
                except requests.exceptions.RequestException:
                    return False

                soup = BeautifulSoup(r.content, 'html.parser')
                # get the title
                title = soup.find("h1", class_= "A95iT1 pDVUjz nmA88J FI5Jsp x--xNS Y6OuCD BicgmA")
                # title = soup.find_all('img', class_='product-page__image-large')
                # title = title[0]['alt']

                # get the price
                price = soup.find("span", {"class": "A95iT1 pDVUjz nmA88J _0uQAcH AHAcbe gzB009"})
                price = price.text
                price = price.replace(u'\n', '')
                price = price.replace(u' kr.', '')
                price = price.replace(u',', '.')
                price = price.replace(u'00&nbsp;', '.')
                price = price.replace(u'\xa0', '')
                price = price.replace(u'kr', '')


                # get the image url
                image = soup.find_all('img', class_='Q8HVfj oMyDaX hsKyRV _8Nfi4s BQJRnm uijqg-')
                image_path = image[0]['src']

                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)

                id = uuid.uuid1()

                fullfilename = os.path.join('C:\\Users\\augus\\OneDrive\\Skrivebord\\CratesAppFeature\\app\\static', str(id))

                urllib.request.urlretrieve(image_path, fullfilename+'.jpg')

                return {'body':str(title.text), 'price': price, 'image': str(id)}

            else:
                return False

        else:
            return False



