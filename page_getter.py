import os
from datetime import datetime
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import selenium_arguments, browser_path
from src.goods_ids import oz_links, wb_links


class PageGetter(Thread):
    def __init__(self):
        super().__init__()
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.html_dir = None
        self.platform = None
        self.links = {}
        self.browser = None
        self.cur_url = None

    def run(self):
        self.check_html_dir()
        # self.initiate_browser()
        self.search_cycle()
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

    def search_cycle(self):
        ln = len(self.links)
        for n, art in enumerate(self.links):
            self.cur_url = self.links[art]
            order = n + 1
            print(f'{self.platform}, №{order:04}/{ln}, art: {art}, connecting to {self.cur_url}')


class GetterOz(PageGetter):
    def __init__(self):
        super().__init__()
        self.html_dir = f'htmls/{self.date}/oz_html_files/'
        self.platform = 'oz'
        self.links = oz_links


class GetterWb(PageGetter):
    def __init__(self):
        super().__init__()
        self.html_dir = f'htmls/{self.date}/wb_html_files/'
        self.platform = 'wb'
        self.links = wb_links


class GetterSm(PageGetter):
    def __init__(self):
        super().__init__()
        self.html_dir = f'htmls/{self.date}/sm_html_files/'
        self.platform = 'sm'
        self.links = []
