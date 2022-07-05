import json
import time
from random import randint

import requests

from config import today
from product import JsonProduct
from src.goods_ids import rosel_products
from src.shop_to_rosel_ids import platform_ids, shop_to_rosel, rosel_wb_feedback_items
from utilites import check_dir


class JsonDataGetter:
    def __init__(self):
        self.platform = None
        self.dir = f'json_data'
        check_dir(self.dir)
        self.id = None
        self.result = {}
        self.cp = None
        self.goods = {}

    def run(self):
        platform = self.platform
        cur_platform_ids = platform_ids.get(platform)
        ll = len(cur_platform_ids)
        for order, self.id in enumerate(cur_platform_ids, start=1):
            self.set_cp()
            print(f'{platform} ({order:03}/{ll}) - getting json data for {self.id}')
            self.get_rating_from_json()
            self.goods.update(self.cp.data_out())
        with open(f'{self.dir}/{today}_{platform}.json', 'w', encoding='utf8') as write_file:
            json.dump(self.goods, write_file, ensure_ascii=False)

    def set_cp(self):
        platform = self.platform
        rosel_id = int(shop_to_rosel[platform][self.id])
        merch = rosel_products[rosel_id]
        cp = JsonProduct()
        cp.url = merch[f'url {platform.upper()}']
        cp.rosel_id = rosel_id
        cp.name = merch['Name']
        cp.shop_id = self.id
        self.cp = cp

    def get_rating_from_json(self):
        pass


class OzJsonGetter(JsonDataGetter):
    def __init__(self):
        super().__init__()
        self.platform = 'oz'


class WbJsonGetter(JsonDataGetter):
    def __init__(self):
        super().__init__()
        self.platform = 'wb'

    def get_rating_from_json(self):
        post_url = 'https://public-feedbacks.wildberries.ru/api/v1/summary/full'
        wb_feedback_item = rosel_wb_feedback_items.get(self.cp.rosel_id)
        if not wb_feedback_item:
            return
        json_data = {"imtId": wb_feedback_item, "take": 30, "skip": 0}
        req = requests.post(post_url, json=json_data)
        loaded_json_data = req.json()
        self.cp.rating = float(loaded_json_data['valuation'])
        self.cp.quantity = int(loaded_json_data['feedbackCount'])
        time.sleep(randint(3, 5))
