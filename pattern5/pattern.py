i=0
j=8
total_chars=9
while j>=0:
	if j==8:
		for index in range(i,j+1):
			print(chr(index+65),end="")
	else:
		for index in range(total_chars):
			if index==i:
				print(chr(65),end="")
			elif index==(total_chars-1-i) and j!=0:
				print(chr(j+65),end="")
			else:
				print(" ",end="")
	j=j-2
	i=i+1
	print()