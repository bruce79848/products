products = []
while True:
	name = input('Please input the product name: ')
	if name == 'q':
		break
	price = input('Please input the product price: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], ',the price is', p[1])