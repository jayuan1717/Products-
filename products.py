products = []
while True:
    name = input('Please entre the product title: ')
    if name == 'q':
    	break
    price = input('Please entre the price:')
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)