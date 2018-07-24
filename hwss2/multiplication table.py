n = int(input("Enter a number : "))
a = n

for a in range(1, n+1):
    for i in range(1, n+1):
        print(a*i, end='\t')
        i = i + 1
    print()




