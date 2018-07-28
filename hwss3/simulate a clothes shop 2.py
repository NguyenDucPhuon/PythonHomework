choice = input("Welcome to our shop, what do you want (C, R, U, D) ? ").upper()

items = ['T-Shirt', 'Sweater']

if choice == 'R':
    print('Our items :', end=' ')
    print(*items, sep=', ')

if choice == 'C':
    new_item = input('Enter new item : ')
    items.append(new_item)
    print('Our items :', end=' ')
    print(*items, sep=', ')

if choice == 'U':
    update_position = int(input('Update Position : ')) - 1
    new_iten = input('New item ? ')
    items[update_position] = new_iten
    print('Our items :', end=' ')
    print(*items, sep=', ')

if choice == 'D':
    delete_position = int(input('Delete position ? ')) - 1
    items.pop(delete_position)
    print('Our items :', end=' ')
    print(*items, sep=', ')


