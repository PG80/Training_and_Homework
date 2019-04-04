# 2019.01.11. TASK_5_PG_Visit Cards New generation




class Product:
    price = 10
    name = 'test'
    description = 'test for test '

    def __init__(self, price, name, description=''):
        self.price = price
        self.name = name
        self.description = description
        print('in __init__ {}'.format(self.name))

    def get_sell_price(self, vat=0.2):
        print(self.name)
        return self.price + self.price * vat

    def __del__(self):
        print('in del {}'.format(self.name))


tv = Product(10, 'tv')
radio = Product(-5.0, 'radio')
tv = Product(100, 'tv123123')

print(tv.get_sell_price())
print(radio.get_sell_price(vat=0.2))

