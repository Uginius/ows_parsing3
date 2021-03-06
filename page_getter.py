import os
import time
from datetime import datetime
from random import randint
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import selenium_arguments, browser_path, date_pattern
from src.goods_ids import oz_links, wb_links
from utilites import write_utf8_file


class PageGetter(Thread):
    def __init__(self):
        super().__init__()
        self.date = datetime.now().strftime(date_pattern)
        self.html_dir = None
        self.platform = None
        self.links = {}
        self.browser = None

    def run(self):
        self.check_html_dir()
        self.initiate_browser()
        self.get_pages_cycle()
        if self.browser:
            self.browser.close()

    def check_html_dir(self):
        if not os.path.exists(self.html_dir):
            os.makedirs(self.html_dir)

    def initiate_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument(selenium_arguments[0])
        options.add_argument(selenium_arguments[1])
        self.browser = webdriver.Chrome(service=Service(executable_path=browser_path), options=options)

    def get_pages_cycle(self):
        ln = len(self.links)
        for n, art in enumerate(self.links):
            cur_url = self.links[art]
            order = n + 1
            print(f'{self.platform}, №{order:04}/{ln:04}, art: {art}, connecting to {cur_url}')
            self.browser.get(url=cur_url)
            self.scroll_down()
            time.sleep(randint(5, 15))
            self.scroll_up()
            self.scroll_down()
            data = self.browser.page_source
            write_utf8_file(data, f'{self.html_dir}N{order:04}_{self.platform}_{art}.html')

    def scroll_up(self):
        self.browser.execute_script(f"window.scrollTo(0, 0);")
        time.sleep(1)

    def scroll_down(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        self.browser.execute_script(f"window.scrollTo(0, {last_height});")
        sl_time = 0.5
        time.sleep(sl_time)
        while True:
            self.browser.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            time.sleep(sl_time)
            if new_height == last_height:
                break
            last_height = new_height
        self.browser.execute_script(f"window.scrollTo(0, {new_height - 2000});")
        time.sleep(sl_time * 3)


class GetterWb(PageGetter):
    def __init__(self):
        super().__init__()
        self.html_dir = f'htmls/{self.date}/wb_html_files/'
        self.platform = 'wb'
        self.links = wb_links

    def scroll_down(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        self.browser.execute_script(f"window.scrollTo(0, {last_height});")
        sl_time = 1
        time.sleep(sl_time)
        for i in range(1, 5):
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            self.browser.execute_script(f"window.scrollTo(0, {new_height - 1000 * i});")
            time.sleep(sl_time * 2)
        while True:
            self.browser.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            time.sleep(sl_time * 2)
            if new_height == last_height:
                break
            last_height = new_height


class GetterSm(PageGetter):
    def __init__(self):
        super().__init__()
        self.html_dir = f'htmls/{self.date}/sm_html_files/'
        self.platform = 'sm'
        self.links = []
