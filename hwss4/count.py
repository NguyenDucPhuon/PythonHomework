list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list_2 = []

user_string = input("What is your fucking string ????? ").lower()

for _ in user_string:
    list_2.append(_)
for letters in list_1:
    if list_2.count(letters) != 0 :
        print(letters, list_2.count(letters))











