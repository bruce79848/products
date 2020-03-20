products = []
while True:
	name = input('Please input the product name: ')
	if name == 'q':
		break
	price = input('Please input the product price: ')
	products.append([name, price])
print(products)