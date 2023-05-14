# Enter coordinates of a cell like 1 and 3
def main():
    user = '_________'
    make_grid(user)
    turn = 'X'
    while True:
        user = make_move(user, turn)
        make_grid(user)
        x_wins = winner_x(user)
        o_wins = winner_o(user)
        turn = switch(turn)
        if x_wins:
            print("X wins")
            break
        elif o_wins:
            print("O wins")
            break
        elif draw(user):
            print("Draw")
            break
def switch(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'
def make_move(user, turn):
    while True:
        xy = input("Next move. Enter coordinates like '1 1' or '1 3': ").replace(' ', '')
        x = int(xy[0])
        y = int(xy[1])
        try:
            i = y + 2
            j = x - 1
            index = (j * 3 + i) - 3  # замена нужной координаты
            list = [c for c in user]
            if x not in range(1,4) or y not in range(1,4):
                print('Coordinates should be from 1 to 3!')
            elif list[index] != '_':
                print('This cell is occupied! Choose another one!')
            elif turn == 'X':
                list[index] = 'X'
                break
            else:
                list[index] = 'O'
                break
        except ValueError:
            print('You should enter numbers!')

    return ''.join(list)  # обратная конвертация списка в строку

def impossible(x_wins, o_wins, user):
    if (x_wins and o_wins) or (abs(user.count('X') - user.count('O')) > 1 ):
        return True
    else:
        return False

def winner_x(user):
    if 'XXX' in (user[:3], user[3:6], user[6:9], user[::3], user[1:8:3], user[2:9:3], user[2:7:2], user[0:9:4]):
        return True
    else:
        return False

def winner_o(user):
    if 'OOO' in (user[:3], user[3:6], user[6:9], user[::3], user[1:8:3], user[2:9:3], user[2:7:2], user[0:9:4]):
        return True
    else:
        return False

def draw(user):
    for c in user:
        if c =='_':
            return False
    return True


def make_grid(user):
    print('---------')
    print('| ', end = '')
    for i in range(len(user)):
        print(f'{user[i]}', end = ' ')
        if ( i + 1 ) % 3 == 0:
            print('|')
            if i % 8 != 0:
                print('| ', end = '')
    print('---------')
    return user

if __name__ == '__main__':
    main()
