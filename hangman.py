import random

my_list = ["python", "java", "swift", "javascript"]

def main():
    x, y = 0, 0
    print('''H A N G M A N  # 8 attempts''')
    while True:
        menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if menu == 'exit':
            break
        elif menu == 'play':
            print()
            n = random.choice(my_list)
            a, b = play_game(n)
            x = x + a
            y = y + b
        elif menu == 'results':
            print(f'You won: {x} times')
            print(f'You lost: {y} times')


def play_game(n):
    guesses = set()
    count = 8
    b = ("-" *(len(n)))
    my_set = set(n)
    while count > 0:
        if b == n:
            print(f'You guessed the word {n}!')
            print('You survived!')
            return 1, 0
        else:
            print(b)
            print("Input a letter: ", end = '')
            s = input()

            if s.islower() and len(s) == 1:
                if s in guesses:
                    print(f"You've already guessed this letter.")
                else:
                    if s in my_set:
                        guesses.add(s)
                    else:
                        guesses.add(s)
                        count-=1
                        print(f"That letter doesn't appear in the word. # {count} attempts")
                print()
                b = replace(b, s, n)
            elif len(s) != 1:
                print("Please, input a single letter")
            else:
                print("Please, enter a lowercase letter from the English alphabet.")


    print("You lost!")
    return 0, 1

def replace(b, s, n):
    i = 0
    for c in n:
        if c == s:
            b = b[:i] + c + b[i+1:]
        i+=1
    return b



if __name__ == "__main__":
    main()
