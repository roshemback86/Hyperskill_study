from random import randint

def main():
    n = get_positive_int()
    s = get_name()
    winner = play_game(n,s)


def get_positive_int():
    print("How many pencils would you like to use: ")
    while True:
        try:
            i = int(input())
            if i == 0:
                print("The number of pencils should be positive")
            elif i < 0:
                raise ValueError
            else:
                return i
        except ValueError:
            print("The number of pencils should be numeric")


def get_name():
    print("Who will be the first (John, Jack): ")
    while True:
        name = input()
        if name == 'John' or name == 'Jack':
            return name
        else:
            print("Choose between 'John' and 'Jack'")


def get_pencil(n):
    while True:
        try:
            i = int(input())
            if i < 1 or i > 3:
                raise ValueError
            elif i > n:
                print("Too many pencils were taken")
            else:
                return i
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def play_game(n,s):
    print("|" * n)
    while n > 0:
        if s == 'Jack':
            print(f"{s}'s turn:")
            x = bot_move(n)
            print(x)
            s = 'John'

        elif s == 'John':
            print(f"{s}'s turn!")
            x = get_pencil(n)
            s = 'Jack'
        n = n - x
        print("|" * (n))
    print(f"{s} won!")

def bot_move(i):
    j = i % 4
    if i == 1:
        return 1
    elif j == 1:
        return randint(1,3)
    elif j == 0:
        return 3
    elif j == 3:
        return 2
    elif j == 2:
        return 1


if __name__ == "__main__":
    main()
