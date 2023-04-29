from store import Store
from database import Database
from product import Product


s = Store(Database, 'data.json', 'bank.json')

### tests
# while True:
#     if s.balance == {}:
#         investment = int(input('Make an investment..'))
#         s.enter_investment(investment)
#     else:
#         c = input("--->")
#         if c == '1':
#             s.enter_product(Product('asd',12,34,34))
#

