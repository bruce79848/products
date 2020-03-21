# Loading file 
products = []
with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'Product,Price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# Let the user input
while True:
	name = input('Please input the product name: ')
	if name == 'q':
		break
	price = input('Please input the product price: ')
	price = int(price)
	products.append([name, price])
print(products)

# Print out the purchased products name and corresponding prices
for p in products:
	print(p[0], ',the price is', p[1])

# Writing file
with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')