import math


class Product:
    def __init__(self):
        self.rosel_id = None
        self.shop_id = None
        self.name, self.url = 'name missing', 'url missing'
        self.status = None
        self.price = 0
        self.rating = 0
        self.quantity = None
        self.votes = {'5*': 0, '4*': 0, '3*': 0, '2*': 0, '1*': 0}

    def out_items(self):
        return [self.shop_id, self.name, self.url, self.price]

    def product_reviews_dict(self):
        return {
            'Rosel': self.rosel_id,
            'Артикул МП': self.shop_id,
            'Наименование': self.name,
            'Рейтинг': self.rating,
            'Количество отзывов на товар': self.quantity,
            '5*': self.votes['5*'], '4*': self.votes['4*'],
            '3*': self.votes['3*'], '2*': self.votes['2*'],
            '1*': self.votes['2*'],
            'url': self.url,
            'Статус': self.status,
        }

    def xlsx_line(self):
        r_id = self.rosel_id
        rating = self.rating
        target = 4
        votes = self.votes
        quantity = int(self.quantity) if self.quantity else None
        if rating >= target:
            need_votes = 'Все ОК'
        else:
            if rating:
                need_votes = math.ceil((quantity * (target - rating)) / (5 - target))
            else:
                need_votes = 2
        return [r_id, self.name, rating, target, need_votes, quantity, *list(votes.values()), self.status, self.url]
