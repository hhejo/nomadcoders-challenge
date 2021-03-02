import requests
from bs4 import BeautifulSoup


def get_last_page(soup):
    last_page = soup.select_one('#NormalInfo .jobCount strong')
    if last_page is None:
        last_page = soup.select_one('#NormalInfo .listCount strong')
    last_page = last_page.string
    if ',' in last_page:
        last_page = last_page.replace(',', '')
    last_page = str(last_page)
    last_page = int(last_page)
    last_page = (last_page // 50) + 1
    return last_page


def get_alba(alba_row):
    place = alba_row.select_one('.local').get_text(strip=True)
    title = alba_row.select_one('.title a span').string
    work_time = alba_row.select_one('.data span').string
    pays = alba_row.select('.pay span')
    pay = f"{pays[0].string}{pays[1].string}"
    reg_date = alba_row.select_one('.regDate').string
    alba = {'place': place, 'title': title, 'time': work_time, 'pay': pay,'date': reg_date}
    return alba


def get_alba_list(brand):
    link = brand['link']
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'html.parser')
    alba_container = soup.select_one('#NormalInfo tbody')
    alba_rows = alba_container.select('tr:nth-child(2n+1)')
    alba_list = []
    last_page = get_last_page(soup)
###################################################################
    #last_page = 1 # 테스트
###################################################################
    for i in range(1, last_page+1):
        link = f'{link}?page={i}'
        html = requests.get(link)
        soup = BeautifulSoup(html.text, 'html.parser')
        alba_container = soup.select_one('#NormalInfo tbody')
        alba_rows = alba_container.select('tr:nth-child(2n+1)')
        for alba_row in alba_rows:
            alba = get_alba(alba_row)
            alba_list.append(alba)
        print(f"alba: {brand['company']} page: {i}/{last_page} ")
    return alba_list