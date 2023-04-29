from store import Store
from database import Database
from product import Product


s = Store(Database, 'data.json', 'bank.json')



while True:
    if s.balance == {}:
        investment = int(input('Make an investment..'))
        s.enter_investment(investment)
    else:
        command = input("Enter the command; (enter, sell, balance, profit, exit) --->")
        if command == 'exit':
            break
        elif command == 'enter':
            p_name = input('Enter the name of product..')
            p_quantity = int(input('Enter the quantity of product...'))
            p_price = int(input('Enter the price of product...'))
            p_pay_price = int(input('Enter the payment price of product...'))
            try:
                s.enter_product(Product(p_name,p_quantity,p_price,p_pay_price))
            except ValueError:
                print('Something went wrong!!! Try again...')
                continue
        elif command == 'sell':
            p_name = input('Enter the name of product..')
            p_quantity = int(input('Enter the quantity of product...'))
            s.sell(p_name,p_quantity)
        elif command == 'balance':
            s.stock_balance()
        elif command == 'profit':
            if s.balance != {}:
                print(f'Profit is {s.balance["profit"]}...')
            else:
                print('No profit')
        else:
            print('Wrong command!!!  Try again...')


