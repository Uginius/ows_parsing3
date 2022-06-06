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

    def no_url(self):
        self.__init__(self.shop_id)

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
        target = 4
        need_votes = 0
        votes = list(self.votes.values())
        return [self.rosel_id, self.name, self.rating, target, need_votes, self.quantity, *votes, self.url]
