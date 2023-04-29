import json


class Database:
    def __init__(self, filename, bank_filename):
        self.filename = filename
        self.bank = bank_filename
        self.products = {}
        self.bank_balance = {}

    def loader(self):
        with open(self.filename) as f:
            self.products = json.load(f)
        return self.products

    def save_prod(self):
        with open(self.filename, 'w') as f:
            json.dump(self.products, f)

    def bank_loader(self):
        with open(self.bank) as b:
            self.bank_balance = json.load(b)
        return self.bank_balance

    def save_to_bank(self):
        with open(self.bank, 'w') as b:
            json.dump(self.bank_balance, b)
