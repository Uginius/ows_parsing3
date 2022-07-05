import os

from bs4 import BeautifulSoup

src_folder = 'htmls/2022-07-04/wb_html_files'
files = os.listdir(src_folder)


def get_price(soup):
    price_block = soup.find('div', class_='product-page__aside-container j-price-block')
    if 'Нет в\xa0наличии' in price_block.text:
        return 'Нет в наличии'
    pr = price_block.div.text.strip().split('₽')[0].replace(' ', '').strip() + ' ₽'
    return pr


wb_results = {}
for file in files:
    rosel_id = int(file.split('_')[-1].split('.')[0])
    with open(f'{src_folder}/{file}', 'r', encoding='utf8') as rf:
        soup = BeautifulSoup(rf, 'lxml')
        wb_results[rosel_id] = get_price(soup)
print(wb_results)
