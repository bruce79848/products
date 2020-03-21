products = []
while True:
	name = input('Please input the product name: ')
	if name == 'q':
		break
	price = input('Please input the product price: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], ',the price is', p[1])

with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')