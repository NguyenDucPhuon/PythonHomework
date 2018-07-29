inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry',  'lint']


inventory['backpack'].remove('dagger')


inventory['gold'] += 50

for _ in inventory:
    if type(inventory[_]) == int:
        print(_, " : ", inventory[_])
    else:
        print(_, ' : ', end=' ')
        print(*inventory[_], sep=',  ')

