game_on = True

while game_on == True:
    import random

    word_list = ['avenger', 'zombie', 'youtube', 'anime', 'naruto', 'sasuke']

    r_andom = random.choice(word_list)

    random_position = []

    list_1 = []

    for _ in r_andom:
        list_1.append(_)

    for _ in range(len(r_andom)):
        x = random.choice(list_1)
        list_1.remove(x)
        random_position.append(x)

    print(*random_position)

    user_answer = input('Your answer: ').lower()

    if user_answer == r_andom:
        print('Hura')
    else:
        print(':(')
    user_game = input('Do you want to play again (type no to stop playing and type everything else to play again): ').lower()
    if user_game == 'no':
        game_on = False
    else:
        game_on = True





