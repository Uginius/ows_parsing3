import os
from threading import Thread

from bs4 import BeautifulSoup


class PagesParser:
    def __init__(self, directory):
        self.platform = None
        self.dir = directory
        self.soup = None

    def run(self):
        files = os.listdir(self.dir)
        for file in files:
            with open(f"{self.dir}/{file}", 'r', encoding='utf8') as read_file:
                self.soup = BeautifulSoup(read_file, 'lxml')
                self.parse()

    def parse(self):
        pass


class ParserOz(PagesParser):
    def __init__(self, directory):
        super().__init__(directory)
        self.platform = 'oz'


class ParserWb(PagesParser):
    def __init__(self, directory):
        super().__init__(directory)
        self.platform = 'wb'
