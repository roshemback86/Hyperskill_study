from random import choice

my_dict = {}
number = int(input("Enter the number of friends joining (including you): "))
print()

if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(int(number)):
        name = input()
        my_dict[name] = 0
    total = int(input("Enter the total bill value: "))
    print()
    ans = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    
    if ans == "Yes":
        lucky = choice(list(my_dict))
        print()
        print(f'{lucky} is the lucky one!')
        print()
        pp = round(total / (number - 1), 2)
        for name in my_dict:
            if name == lucky:
                my_dict[name] = 0
            else:
                my_dict[name] = pp   
        print(my_dict)
    else:
        print()
        print('No one is going to be lucky')
        print()
    
        pp = round(total / number, 2)
        for name in my_dict:  
            my_dict[name] = pp
        print()
        print(my_dict) 
