row = 5
n=0

while n<row:
	if n == 0 or n == row-1:
		for i in range(row):
			print(chr(i+65),end="")

	else:
		for i in range(row):
			if i == 0 or i == row-1:
				print(chr(i+65),end="")
			else:
				print(" ", end="")
	print()
	n=n+1
