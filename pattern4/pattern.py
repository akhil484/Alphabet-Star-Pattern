n=7
counter=0
for i in range((n-1)*2+1):
	for _ in range(n-counter-1):
		print(" ",end="")
	for j in range(counter+1):
		print(chr(j+65),end="")
	print()
	if i<n-1:
		counter=counter+1
	else:
		counter=counter-1