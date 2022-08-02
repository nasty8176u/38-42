import random
g = ('Добро пожаловать в игру с конфетами. Чтобы победить, вам нужно забрать себе оставшиеся конфеты последним.Вперед!')

mes = ['Теперь вам пора брать конфеты', 'возьмите конфеты', 
            'сколько конфет вы будете брать ?', 'берите!', 'Теперь ваш черед']

def game(n, m, pls, mes):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{pls[count%2]}, {random.choice(mes)}')
        move = int(input())
        if move > n or move > m:
            print(f'Вы не можете взять более {m} конфет {letter}, у нас всего {n} конфет {letter}')
            at = 4
            while at > 0:
                if n >= move <= m:
                  break
                print(f'Попробуйте ещё раз, у Вас {at} попытки')
                move = int(input())
                at -=1
            else: 
               return print(f'Попытки закончились.К сожалению, игра окончена')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Конфеты закончены.')
        count +=1
    return players[not count%2]

print(g)

pl1 = input('Первый игрок, скажите своё имя\n')
pl2 = input('Второй игрок, а как же вас зовут? \n')
pls = [pl1, pl2]

n = int(input('Сколько конфет будет в игре?\n '))
m = int(input('А сколько конфет вы хотите брать за один раз?\n '))

winer = game(n, m, pls, mes)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю!Победил {winer}! ')

