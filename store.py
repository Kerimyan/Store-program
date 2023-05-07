class Store:
    def __init__(self, Database_class, d_file_name, b_file_name):
        self.prod_j_file = d_file_name
        self.bank_j_file = b_file_name
        self.database = Database_class()
        self.available_products = self.database.loader(d_file_name)
        self.balance = self.database.loader(b_file_name)

    def enter_investment(self, investment: int):
        self.balance = {'balance': investment, 'profit': 0}
        self.database.save(self.balance,self.bank_j_file)
        self.balance = self.database.loader(self.bank_j_file)
        print('The investment is made...')

    def enter_product(self, product):
        if product.name in self.available_products:
            self.available_products[product.name]['quantity'] += product.quantity
            if product.purchase_price != self.available_products[product.name]['purchase_price'] or \
                    product.payment_price != self.available_products[product.name]['payment_price']:
                self.available_products[product.name] = {'quantity': self.available_products[product.name]['quantity'],
                                                         'purchase_price': product.purchase_price,
                                                         'payment_price': product.payment_price}
                self.balance['balance'] -= product.purchase_price * product.quantity
                self.database.save(self.balance,self.bank_j_file)
                self.database.save(self.available_products, self.prod_j_file)
                print(f'Prices of {product.name} is changed in stock')
            else:
                self.balance['balance'] -= product.purchase_price * product.quantity
                self.database.save(self.balance,self.bank_j_file)
                self.database.save(self.available_products, self.prod_j_file)
                print(f'Quantity of {product.name} is changed in stock::  '
                      f'Quantity -- <{self.available_products[product.name]["quantity"]}>')

        else:
            self.available_products[product.name] = {'quantity': product.quantity,
                                                     'purchase_price': product.purchase_price,
                                                     'payment_price': product.payment_price}
            self.balance['balance'] -= product.purchase_price * product.quantity
            self.database.save(self.balance, self.bank_j_file)
            self.database.save(self.available_products, self.prod_j_file)
            print(f'{product.name} is saved in stock::')

    def del_prod(self, name_p):
        del self.available_products[name_p]
        self.database.save(self.available_products, self.prod_j_file)

    def sell(self, name_p, quantity_p):
        if type(name_p) == str and type(quantity_p) == int:
            if name_p in self.available_products:
                if self.available_products[name_p]['quantity'] >= quantity_p:
                    self.available_products[name_p]['quantity'] -= quantity_p
                    self.balance['balance'] += quantity_p * self.available_products[name_p]['payment_price']
                    self.balance['profit'] += (self.available_products[name_p]['payment_price'] -
                                               self.available_products[name_p]['purchase_price']) * quantity_p
                    self.database.save(self.balance, self.bank_j_file)
                    if self.available_products[name_p]['quantity'] == 0:
                        self.database.save(self.available_products, self.prod_j_file)
                        print('The product is sold::')

                    else:
                        self.database.save(self.available_products, self.prod_j_file)
                        print('The product is sold::')
                else:
                    print('Not enough quantity...')
            else:
                print('Product is not available...')
        else:
            raise TypeError

    def stock_balance(self):
        for prod in self.available_products:
            print(f'{prod}--{self.available_products[prod]["quantity"]}')


