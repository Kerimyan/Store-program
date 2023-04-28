class Product:
    def __init__(self, name, quantity, purchase_price, payment_price):
        if type(name) == str and \
        type(quantity) == int and \
        type(purchase_price) == int and\
        type(payment_price) == int:
            self._name = name
            self.quantity = quantity
            self.purchase_price = purchase_price
            self.payment_price = payment_price
        else:
            raise ValueError

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError



if __name__ == '__main__':
    p = Product(87, 'davo', 'arshak', 56)

    print(p.quantity)