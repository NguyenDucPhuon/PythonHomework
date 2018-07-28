items = ['T-Shirt', 'Sweater']

question_on = True

while question_on == True:

    choice = input("Welcome to our shop, what do you want (C, R, U, D) ? ").upper()

    if choice == 'R':
        print('Our items :', end=' ')
        print(*items, sep=', ')

    if choice == 'C':
        new_item = input('Enter new item : ')
        items.append(new_item)
        print('Our items :', end=' ')
        print(*items, sep=', ')

    if choice == 'U':
        while question_on == True:
            update_position = int(input('Update Position : '))
            while update_position > len(items) or update_position < -len(items):
                print('We do not have that position in our items, please try again')
                update_position = int(input('Update Position : '))
            new_iten = input('New item ? ')
            items[update_position-1] = new_iten
            print('Our items :', end=' ')
            print(*items, sep=', ')
            break

    if choice == 'D':
        while question_on == True:
            delete_position = int(input('Delete position : '))
            while delete_position > len(items) or delete_position < -len(items):
                print('We do not have that position in our items, please try again')
                delete_position = int(input('Delete Position : '))
            items.pop(delete_position-1)
            print('Our items :', end=' ')
            print(*items, sep=', ')
            break

