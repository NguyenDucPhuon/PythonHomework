import random

word_list = ['avenger', 'zombie', 'youtube', 'anime', 'naruto', 'sasuke']

r_andom = random.choice(word_list)

random_position = []
list_1 = []

for a in r_andom:
    list_1.append(a)

for i in range(len(r_andom)):
    x = random.choice(list_1)
    list_1.remove(x)
    random_position.append(x)

print(*random_position)

user_answer = input("Your answer : ").lower()

if user_answer == r_andom:
    print("Hura")
else:
    print(":(")

