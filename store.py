from product import Product
from database import Database
import json


class Store:
    def __init__(self, Database_class, d_file_name):
        self.database = Database_class(d_file_name)
        self.available_products = self.database.loader()

    def enter_product(self, product):
        if product.name in self.available_products:
            self.available_products[product.name]['quantity'] += product.quantity
            if product.purchase_price != self.available_products[product.name]['purchase_price'] or \
                    product.payment_price != self.available_products[product.name]['payment_price']:
                self.available_products[product.name] = {'quantity': self.available_products[product.name]['quantity'],
                                                         'purchase_price': product.purchase_price,
                                                         'payment_price': product.payment_price}
                self.database.save_prod()
                print(f'Prices of {product.name} is changed in stock')
            else:
                self.database.save_prod()
                print(f'Quantity of {product.name} is changed in stock::  '
                      f'Quantity -- <{self.available_products[product.name]["quantity"]}>')

        else:
            self.database.available_products[product.name] = {'quantity': product.quantity,
                                                              'purchase_price': product.purchase_price,
                                                              'payment_price': product.payment_price}
            self.database.save_prod()
            print(f'{product.name} is saved in stock::')

    def check_prod(self, name_p):
        del self.available_products[name_p]
        self.database.save_prod()

    def sell(self, name_p, quantity_p):
        if type(name_p) == str and type(quantity_p) == int:
            if name_p in self.available_products:
                if self.available_products[name_p]['quantity'] >= quantity_p:
                    self.available_products[name_p]['quantity'] -= quantity_p
                    if self.available_products[name_p]['quantity'] == 0:
                        self.check_prod(name_p)
                        print('the product is sold')

                    else:
                        self.database.save_prod()
                        print('the product is sold')
                else:
                    print('Not enough quantity...')
            else:
                print('Product is not available...')
        else:
            raise TypeError

    def stock_balance(self):
        for prod in self.available_products:
            print(f'{prod}--{self.available_products[prod]["quantity"]}')


if __name__ == '__main__':
    s = Store(Database, 'test.json')
    # s.enter_product(Product('qqqqqqqq', 123, 45, 77))
    # s.enter_product(Product('wwwwwwwww', 123, 45, 77))
    #
    # s.enter_product(Product('asd',6,23,23))
    s.stock_balance()
    # print(s.available_products)
