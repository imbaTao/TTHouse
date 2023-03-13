import requests
from bs4 import BeautifulSoup
url = 'https://hz.lianjia.com/ditiefang/li18000011986630/sf1/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
house_list_items = soup.find_all('div', class_='info clear')
for house in house_list_items:
    name = house.find('div', class_='title').find('a').text.strip()
    price = house.find('div', class_='priceInfo').find('div', class_='totalPrice').text.strip()
    unit_price = house.find('div', class_='priceInfo').find('div', class_='unitPrice').text.strip()

    # 去掉 price 字段中的 "万" 单位
    unit_price = unit_price.replace('元/平', '')
    unit_price = unit_price.replace(',', '')
    if float(unit_price) < 26000:
        print('Name: {}, Price: {}, Unit Price: {}元'.format(name, price, unit_price))
