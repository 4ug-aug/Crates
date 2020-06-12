from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get('https://www.zalando.dk/asics-sportstyle-gel-1090-sneakers-whiteblue-coast-a0h15o03i-a12.html', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

image = soup.find_all('img', class_='Q8HVfj oMyDaX hsKyRV _8Nfi4s BQJRnm uijqg-')
image_path = image[0]['src']
print(image_path)