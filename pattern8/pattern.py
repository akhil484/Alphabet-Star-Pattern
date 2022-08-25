row = 1
print()
print()
while row<=8:
	bit = row%2
	for _ in range(12):
		print('  ',end="")
	for _ in range(8):
		print(bit,end="")
		bit = 1 - bit
	print()
	row=row+1
print()
