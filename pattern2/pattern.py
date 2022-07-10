from colorama import init, Fore, Back, Style
init(autoreset=True)

i=0
j=5
while i<=6 or j>=0:
    for _ in range(30):
        print(end=" ")
    if i<=6:
        for c in range(0,i):
            print(Style.BRIGHT + Fore.GREEN +chr(c+65), end =" ")
        print()
        i=i+1
    else:
        for c in range(0,j):
            print(Style.BRIGHT + Fore.BLUE +chr(c+65), end =" ")
        print()
        j=j-1
