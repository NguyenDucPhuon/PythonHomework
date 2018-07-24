for i in range(20):

    print(i, end=' ')

n = int(input("Enter a number : "))

for i in range(n):

    print(i, end=' ')

n = int(input("Enter the total number of 1's and 0's: "))

for i in range(1, n+1):

    if i % 2 == 1:

        print(1, end=' ')

    else:

        print(0, end=' ')



