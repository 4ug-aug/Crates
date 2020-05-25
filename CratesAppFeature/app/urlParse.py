'''

A script that takes attributes: picture, price, title and descsription of a url of an item
If missing attribute skip it.

'''
import requests
import re
from bs4 import BeautifulSoup

supported = ["komplett", "elgiganten"]

class FetchItem():
    def fetch(self, page):

        domain = re.findall(r"https://www.(\w+).", page)
        if domain and domain[0] in supported:
            if domain[0] == supported[0]:
                try:
                    r = requests.get(page)

                    soup = BeautifulSoup(r.content, 'html.parser')
                    # get the title
                    title = soup.find("h1", {"class": "product-main-info-webtext1"})
                    # get the price
                    price = soup.find("span", {"class": "product-price-now"})
                    # get the discription
                    price = price.text
                    price = price.replace(',-', '')
                    price = price.replace('.', '')
                    return {'body':str(title.text), 'price': price}
                except requests.exceptions.RequestException:
                    return False
            
            elif domain[0] == supported[1]:
                try:
                    r = requests.get(page)

                    soup = BeautifulSoup(r.content, 'html.parser')
                    # get the title
                    title = soup.find("h1", {"class": "product-title"})

                    # get the price
                    price = soup.find("div", {"class": "product-price-container"})
                    price = price.text
                    price = price.replace(u'\xa0', '')
                    return {'body':str(title.text), 'price': price}
                except requests.exceptions.RequestException:
                    return False
            else:
                return False
        else:
            return False



