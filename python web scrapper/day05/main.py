import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "https://www.iban.com/currency-codes"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tbody = soup.find('tbody')

items = []

trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    info_index = {
        0: 'Country',
        1: 'Currency',
        2: 'Code',
        3: 'Number'
    }
    info = {
        'Country': None,
        'Currency': None,
        'Code': None,
        'Number': None
    }
    for idx in range(4):
        if idx != 0:
            info[info_index[idx]] = tds[idx].text
        else:
            info[info_index[idx]] = tds[idx].text.capitalize()
    if info['Currency'] != 'No universal currency':
        items.append(info)

def retry():
    try:
        user_input = int(input('#: '))
        if 0 <= user_input < len(items):
            chose_item = items[user_input]
            print(f"You chose {chose_item['Country']}")
            print(f"The currency code is {chose_item['Code']}")
        else:
            print('Choose a number from the list.')
            retry()
    except:
        print("That wasn't a number.")
        retry()

for i, item in enumerate(items):
    row = f"# {i} {item['Country']}"
    print(row)

retry()