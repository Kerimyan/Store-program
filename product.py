class Product:
    def __init__(self, name, quantity, purchase_price, payment_price):
        if type(name) == str and \
        type(quantity) == int and \
        type(purchase_price) == int and\
        type(payment_price) == int:
            self.name = name
            self.quantity = quantity
            self.purchase_price = purchase_price
            self.payment_price = payment_price
        else:
            raise ValueError

