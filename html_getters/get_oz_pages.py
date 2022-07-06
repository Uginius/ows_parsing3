import time
from random import randint
from threading import Thread
from config import today, selenium_arguments, browser_path
from src.goods_ids import oz_links, rosel_products
from utilites import check_dir, write_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class GetterOz(Thread):
    def __init__(self):
        super().__init__()
        self.date = today
        self.browser = None
        self.html_dir = f'htmls/{today}/oz_html_files/'
        self.platform = 'oz'
        self.links = oz_links

    def run(self):
        check_dir(self.html_dir)
        self.initiate_browser()
        self.get_pages_cycle()
        if self.browser:
            self.browser.close()

    def disconnect(self):
        if self.browser:
            self.browser.close()
        time.sleep(200)
        self.initiate_browser()
        time.sleep(20)

    def reconnect(self):
        if self.browser:
            self.browser.close()
        time.sleep(2)
        self.initiate_browser()
        time.sleep(2)

    def initiate_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument(selenium_arguments[0])
        options.add_argument(selenium_arguments[1])
        self.browser = webdriver.Chrome(service=Service(executable_path=browser_path), options=options)

    def get_pages_cycle(self):
        platform = self.platform
        links_dict = self.links
        ln = len(links_dict)
        for n, rosel_id in enumerate(links_dict, start=1):
            if n < 277:
                continue
            if n > 0 and n % 70 == 0:
                self.disconnect()
            merch = rosel_products[rosel_id]
            if merch['Status OZ'] == 'архив':
                print(f'{platform}, №{n:03}/{ln:03}, rosel_id: {rosel_id} in archive')
                continue
            cur_url = links_dict[rosel_id]
            print(f'{platform}, №{n:03}/{ln:03}, rosel_id: {rosel_id}, connecting to {cur_url}')
            self.get_data_from_browser(cur_url, n)
            data = self.browser.page_source
            write_html(data, f'{self.html_dir}N{n:04}_{self.platform}_{rosel_id}.html')

    def get_data_from_browser(self, cur_url, n):
        try:
            self.browser.get(url=cur_url)
            self.scroll_down()
            time.sleep(randint(5, 15))
            self.scroll_up()
            self.scroll_down()
        except Exception as ex:
            print(f'{self.platform} №{n:03} - BROWSER ERROR, ex: {ex}')
            self.reconnect()

    def scroll_up(self):
        self.browser.execute_script(f"window.scrollTo(0, 0);")
        time.sleep(1)

    def scroll_down(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        self.browser.execute_script(f"window.scrollTo(0, {last_height});")
        sl_time = 0.5
        time.sleep(sl_time)
        for i in range(1, 5):
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            self.browser.execute_script(f"window.scrollTo(0, {new_height - 1000 * i});")
            time.sleep(sl_time * 3)
        while True:
            self.browser.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            time.sleep(sl_time * 3)
            if new_height == last_height:
                break
            last_height = new_height
        for i in range(3):
            time.sleep(sl_time)
            self.browser.execute_script(f"window.scrollBy(0, {(i + 1) * 1500})")
