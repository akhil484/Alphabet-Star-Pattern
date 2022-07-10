num=11
row=0
while num>0:
	for _ in range(row):
		print(" ",end="")
	for i in range(num):
		print(chr(i+65),end="")
	for _ in range(row):
		print(" ",end="")
	print("")
	num=num-2
	row=row+1

