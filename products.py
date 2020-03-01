products = []
while True:
    name = input('Please entre the product title: ')
    if name == 'q':
    	break
    price = input('Please entre the price:')
    products.append([name, price])
print(products)