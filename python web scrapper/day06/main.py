import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

#print(format_currency(5000, "KRW", locale="ko_KR"))

############################ INITIALIZING ############################
os.system("clear")
url = "https://www.iban.com/currency-codes"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tbody = soup.find('tbody')
items = []
trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    info = {
        'Country': None,
        'Code': None,
    }
    for idx in range(4):
        if idx == 0:
            info['Country'] = tds[idx].get_text().capitalize()
        elif idx == 2:
            info['Code'] = tds[idx].get_text()
    currency = tds[1].string
    if currency != 'No universal currency':
        items.append(info)
######################################################################


def how_many():
    while True:
        try:
            amount = int(input())
            if amount >= 0:
                break
            else:
                print('\nHave to bigger than 0\n')
        except:
            print("\nThat wasn't a number.\n")
    return amount


def second_try():
    while True:
        try:
            another_country = int(input('#: '))
            if 0 <= another_country < len(items):
                print(items[another_country]['Country'])
                break
            else:
                print('\nChoose a number from the list.\n')
        except:
            print("\nThat wasn't a number.\n")
    return another_country


def first_try():
    while True:
        try:
            user_country = int(input('#: '))
            if 0 <= user_country < len(items):
                print(items[user_country]['Country'])
                break
            else:
                print('\nChoose a number from the list.\n')
        except:
            print("\nThat wasn't a number.\n")
    return user_country


################################ MAIN ################################
print('Welcome to CurrencyConvert PRO 2000')
for i, item in enumerate(items):
    print('#{} {}'.format(i, item['Country']))

print('\nWhere are you from? Choose a country by number.\n')
first_num = first_try()
first_choice = items[first_num]['Code']

print('\nNow choose another country.\n')
second_num = second_try()
second_choice = items[second_num]['Code']

print(f'\nHow many {first_choice} do you want to convert to {second_choice}?\n')
amount = how_many()

URL_CURRENCY = f'https://transferwise.com/gb/currency-converter/{first_choice}-to-{second_choice}-rate?amount={amount}'

r = requests.get(URL_CURRENCY)
s = BeautifulSoup(r.text, 'html.parser')
final_value = s.find('h3', class_='cc__source-to-target')
final_value = final_value.find_all('span')
final_value = final_value[2]
final_value = float(final_value.string)

my_currency = format_currency(amount, first_choice)

final_currency = format_currency(amount * final_value, second_choice)

print(f"\n{my_currency} is {final_currency}\n")

######################################################################