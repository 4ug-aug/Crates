'''

A script that takes attributes: picture, price, title and descsription of a url of an item
If missing attribute skip it.

'''
import requests
import re
from bs4 import BeautifulSoup

supported = ["komplett"]

class FetchItem():
    def fetch(self, page):
        

        domain = re.findall(r"https://www.(\w+).", page)
        if domain[0] in supported:
            r = requests.get(page)

            soup = BeautifulSoup(r.content, 'html.parser')
            # get the title
            title = soup.find("h1", {"class": "product-main-info-webtext1"})
            # get the price
            price = soup.find("span", {"class": "product-price-now"})
            # get the discription
            
            body = title.text+', '+price.text
            return(str(body))
        else:
            return False



