from colorama import init, Fore, Back, Style
init(autoreset=True)

n = 10
k=n
for i in range(n):
	for j in range(k):
		if i<n/2:
			print(Style.BRIGHT + Fore.RED +'*', end =" ")
		else:
			print(Style.BRIGHT + Fore.YELLOW +'*', end =" ")
	print()
	k=k-1