import os
from bs4 import BeautifulSoup

src_folder = 'htmls/2022-07-04/wb_html_files'
files = os.listdir(src_folder)
wb_results = {}
for file in files:
    rosel_id = int(file.split('_')[-1].split('.')[0])
    with open(f'{src_folder}/{file}', 'r', encoding='utf8') as rf:
        soup = BeautifulSoup(rf, 'lxml')
        wb_slider_item = soup.find('a', class_='comment-card__more j-read-full-feedback')
        if wb_slider_item:
            wb_item = wb_slider_item['href'].split('feedbacks?imtId=')[1].split('&size')[0]
            wb_results[rosel_id] = int(wb_item)
print(wb_results)
