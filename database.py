import json


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.available_products = {}

    def loader(self):
        with open(self.filename) as f:
            self.available_products = json.load(f)
        return self.available_products

    def save_prod(self):
        with open(self.filename, 'w') as f:
            json.dump(self.available_products, f)

