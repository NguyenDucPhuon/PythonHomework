sizes = [5, 90, 42, 137, 768, 345, 389]

print('Hello, my name is Pyscho and these are my ship sizes')

print(sizes)


biggest_one = sizes[0]
for _ in sizes:
    if _ > biggest_one:
        biggest_one = _

n = sizes.index(biggest_one)
sizes[n] = 8

print("Now my biggest sheep hsa size", biggest_one, "let shear it")

print('After shearing, here is my flock')
print(sizes)

for a in range(3):
    for i in range(7):
        sizes[i] = sizes[i] + 50
    print('MONTH', a, ':')
    print('One month has passed, now here is my flock')
    print(sizes)

    biggest_one = sizes[0]
    for _ in sizes:
        if _ > biggest_one:
            biggest_one = _

    n = sizes.index(biggest_one)
    sizes[n] = 8

    print("Now my biggest sheep hsa size", biggest_one, "let shear it")

    print('After shearing, here is my flock')
    print(sizes)
    print("**********************************************************************")

for i in range(7):
    sizes[i] = sizes[i] + 50
print('MONTH 3 :')
print('One month has passed, now here is my flock')
print(sizes)

sum = 0
for p in sizes:
    sum = sum + p

print('My flock has size in total: ', sum)
print('I would get', sum, '* 2$ = ', sum * 2, '$')




