import requests
from bs4 import BeautifulSoup

def get_brand_list():
    alba_url = "http://www.alba.co.kr"
    html = requests.get(alba_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    boxs = soup.select('#MainSuperBrand .goodsBox .impact')
    brand_list = []
    for box in boxs:
        company = box.select_one('.company').string
        if '/' in company:
            company = company.replace('/', '-')
        link = box.select_one('a')['href']
        brand = {'company': company, 'link': link}
        brand_list.append(brand)
    print('brand list successfully organized')
    return brand_list