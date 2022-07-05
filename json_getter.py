from config import today
from utilites import check_dir


class JsonDataGetter:
    def __init__(self):
        self.platform = None
        self.dir = f'json_data/{today}'
        check_dir(self.dir)

    def run(self):
        pass


class OzJsonGetter(JsonDataGetter):
    def __init__(self):
        super().__init__()
        self.platform = 'oz'


class WbJsonGetter(JsonDataGetter):
    def __init__(self):
        super().__init__()
        self.platform = 'wb'
