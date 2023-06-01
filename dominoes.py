import random
import sys


my_list = []
stock = []
pc = []
player = []
snake = []
status = ''

def main():

    my_list = create_dice()
    stock, pc, player, snake, status = shuffle(my_list)
    print_status(stock, pc, player, snake, status)
    play_game(stock, pc, player, snake, status)


def check_status(stock, pc, player, snake):
    if len(pc) == 0:
        status ='Status: The game is over. The computer won!'
        print_status(stock, pc, player, snake, status)
        sys.exit()
    elif len(player) == 0:
        status ='Status: The game is over. You won!'
        print_status(stock, pc, player, snake, status)
        sys.exit()
    elif draw(snake):
        status = "Status: The game is over. It's a draw!"
        print_status(stock, pc, player, snake, status)
        sys.exit()
    else:
        return True

def play_game(stock, pc, player, snake, status):
    while True:
        check_status(stock, pc, player, snake)
        if status == 'player':
            stock, player, snake = players_move(stock, player, snake)
            status = 'computer'
        elif status == 'computer':
            stock, pc, snake = pss_move(stock, pc, snake)
            status = 'player'
        print_status(stock, pc, player, snake, status)


def draw(snake):
    counter = 1
    start = snake[0][0]
    end = snake[len(snake) - 1][1]
    if start == end:

        for el in snake:
            if el[0] == start:
                counter += 1
            if el[1] == start:
                counter += 1
    if counter >= 8:
        return True

def players_move(stock, player, snake):
    while True:
        try:
            s = int(input())
            if abs(s) > len(player):
                raise ValueError
            elif s == 0:
                if stock != []:
                    x = random.choice(stock)
                    player.append(x)
                    stock.remove(x)
                break
            else:
                dice = player[abs(s) - 1]
                if s > 0:
                    if dice[0] == snake[len(snake) - 1][1]:
                        snake.append(dice)
                        player.remove(dice)
                        break
                    elif dice[1] == snake[len(snake) - 1][1]:
                        player.remove(dice)
                        dice.reverse()
                        snake.append(dice)
                        break
                    else:
                        raise SyntaxError
                elif s < 0:
                    if dice[1] == snake[0][0]:
                        snake.insert(0, dice)
                        player.remove(dice)
                        break
                    elif dice[0] == snake[0][0]:
                        player.remove(dice)
                        dice.reverse()
                        snake.insert(0, dice)
                        break
                    else:
                        raise SyntaxError
        except ValueError:
            print('Invalid input. Please try again.')
            continue
        except SyntaxError:
            print('Illegal move. Please try again.')
            continue
    return stock, player, snake

def pss_move(stock, pc, snake):

    my_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    pc_score = dict()  # Очищаем словарь частоты чисел

    for el in snake:  # Считаем в дикт частоту чисел в списке snake
        my_dict[el[0]] += 1
        my_dict[el[1]] += 1

    for el in pc: # Добавляем в дикт частоту чисел в спискe pc
        my_dict[el[0]] += 1
        my_dict[el[1]] += 1

    i = 0  # Создаем словарь по весу кости
    for el in pc:
        score = my_dict[el[0]] + my_dict[el[1]]
        pc_score.update( { i : score } )
        i += 1

    s = input()
    while True:
        if pc_score == {}:
            if stock != []:
                temp = random.choice(stock)
                pc.append(temp)
                stock.remove(temp)
            break
        pair = max(pc_score.items(), key=lambda k: k[1])
        n = pair[0]
        pc_dice = pc[abs(n)]

        if pc_dice[0] == snake[len(snake) - 1][1]:
            snake.append(pc_dice)
            pc.remove(pc_dice)
            break
        elif pc_dice[1] == snake[len(snake) - 1][1]:
            pc.remove(pc_dice)
            pc_dice.reverse()
            snake.append(pc_dice)
            break

        if pc_dice[1] == snake[0][0]:
            snake.insert(0, pc_dice)
            pc.remove(pc_dice)
            break
        elif pc_dice[0] == snake[0][0]:
            pc.remove(pc_dice)
            pc_dice.reverse()
            snake.insert(0, pc_dice)
            break

        del pc_score[max(pc_score, key=lambda key: pc_score[key])]
        continue


    pc_score = {x: 0 for x in pc_score}  # Очищаем словарь веса костей
    return stock, pc, snake

def create_dice():
    for i in range(0,7):
        for j in range(0,7):
            dice = [i,j]
            if i == j:
                my_list.append(dice)
            elif [j,i] not in my_list:
                my_list.append(dice)
    return my_list

def shuffle(my_list):
    for i in range(14):  # Stock pieces
        x = random.choice(my_list)
        stock.append(x)
        my_list.remove(x)

    for i in range(7):  # pc pieces, player pieces
        x = random.choice(my_list)
        pc.append(x)
        my_list.remove(x)
        y = random.choice(my_list)
        player.append(y)
        my_list.remove(y)

    for i in range(6,-1,-1):
        dice = [i,i]
        if dice in pc:
            snake.append(dice)
            pc.remove(dice)
            status = 'player'
            break
        elif dice in player:
            snake.append(dice)
            player.remove(dice)
            status = 'computer'
            break
        else:
            continue
    return stock, pc, player, snake, status

def print_status(stock, pc, player, snake, status):
    print('=' * 70)
    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(pc)}')
    print()
    print_snake(snake)
    print()
    print('Your pieces:')
    for i in range(len(player)):
        print(f'{i + 1}: {player[i]}')

    if status == 'player':
        print(f"Status: It's your turn to make a move. Enter your command.")
    elif status == 'computer':
        print(f"Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print()
        print(status)

def print_snake(snake):

    if len(snake) > 6:
        print(f'{snake[0]}{snake[1]}{snake[2]}...{snake[len(snake) - 3]}{snake[len(snake) - 2]}{snake[len(snake) - 1]}')
    else:
        for el in snake:
            print(el, end='')
        print()

if __name__ == "__main__":
    main()
