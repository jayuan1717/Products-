import os # operating system
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'product, price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print('Listed products: ', products)
	return products

def user_input(products):
	while True:
		name = input('Please entre the product title: ')
		if name == 'q':
			break
		price = float(input('Please entre the price:'))
		products.append([name, price])
	return products	 # let user add new product and price

def print_products(products):
	for p in products:
		print(p[0], 'is selling at price of', p[1], 'CAD') # print out the porduct and price 

def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('product, price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def mainnn(file):
	if os.path.isfile(file):
		print('File is found!')
		products = read_file(file)
		products = user_input(products)
		print_products(products)
		write_file(file, products)
	else:
		print('The file is not found..:(')

mainnn(input('pleae entre a file name: '))