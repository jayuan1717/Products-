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

	with open('products.csv', 'w', encoding='utf-8') as f:
		f.write('product, price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')