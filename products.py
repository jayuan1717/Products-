products = []
while True:
    name = input('Please entre the product title: ')
    if name == 'q':
    	break
    price = input('Please entre the price:')
    products.append([name, price])
#print(products)
for p in products:
	print(p[0], 'is selling at price of', p[1], 'CAD')