from random import randint, choice
g = ('Добро пожаловать в игру с конфетами. Чтобы победить, вам нужно забрать себе оставшиеся конфеты последним.Вперед!')

mes = ['Теперь вам пора брать конфеты', 'возьмите конфеты', 
            'сколько конфет вы будете брать ?', 'берите!', 'Теперь ваш черед']
def game():
    pl1 = input('Привет,как Вас зовут?\n')
    pl2 = 'Валли'
    print(f'Приятно познакомится, я- {pl2}')
    return [pl1, pl2]


def get(players):
    n = int(input('Сколько всего конфет будет в игре?\n '))
    m = int(input('А сколько конфет будем брать за один раз?\n '))
    first = int(input(
        f'{pls[0]},вы можете ходить первым, если хотите, но для этого нажмите 2, иначе нажмите любую другую кнопку \n'))
    if first != 2:
        first = 0
    return [n, m, int(first)]


def play(rules, pls, mes):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Беру {move}')
        else:
            print(f'{pls[0]}, {choice(mes)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                at = 3
                while at > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {at} попытки')
                    move = int(input())
                    at -= 1
                else:
                    return print(f'Попытки закончились.К сожалению, игра окончена((')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return pls[count % 2]


print(g)

pls = game()
rules = get(pls)

w = play(rules, pls, mes)
if not w:
    print('К сожалению, победителей нет')
else:
    print(
        f'Поздравляю! Победил {w}! ')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
from random import randint, choice

g = ('Добро пожаловать в игру с конфетами. Чтобы победить, вам нужно забрать себе оставшиеся конфеты последним.Вперед!')

mes = ['Теперь вам пора брать конфеты', 'возьмите конфеты', 
            'сколько конфет вы будете брать ?', 'берите!', 'Теперь ваш черед']

def game():
    pl1 = input('Как же Вас зовут?\n')
    pl2 = 'Валли'
    print(f'А меня зовут {pl2}')
    return [pl1, pl2]


def get(pls):
    n = int(input('Сколько конфет будет в игре?\n '))
    m = int(input('Сколько конфет можно будет брать максимально за один ход?\n '))
    
def play(get, pls, mes):
    count = get1[2]
    if get1[0] % 10 == 1 and 9 > get1[0] > 10:
        letter = 'а'
    elif 1 < get1[0] % 10 < 5 and 9 > get1[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while get1[0] > 0:
        if not count % 2:
            move = randint(1, get1[1])
            print(f'Я забираю {move}')
        else:
            print(f'{pls[0]}, {choice(mes)}')
            move = int(input())
            if move > get1[0] or move > get1[1]:
                print(
                    f'Это слишком много, можно взять не более {get1[1]} конфет{letter}, у нас всего {get1[0]} конфет{letter}')
                at = 3
                while at > 0:
                    if get1[0] >= move <= get1[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {at} попытки')
                    move = int(input())
                    at-= 1
                else:
                    return print(f'Попытки закончены. К сожалению, игра окончена(((')
        get1[0] = get1[0] - move
        if get1 > 0:
            print(f'Осталось {get1[0]} конфет{letter}')
        else:
            print('Упс,конфеты закончились.')
        count += 1
    return pls[count % 2]


print(g)

pls = game()
get1 = get(pls)

winer = play(get, pls, mes)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}!')

