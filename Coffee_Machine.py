class Coffee_machine:

    def __init__(self):
        self.machine = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

    def main(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit): ')
            s = input()
            if s == 'buy':
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
                s1 = input()
                self.make_coffee(s1)
            elif s == 'fill':
                self.fill_machine()
            elif s == 'take':
                self.take_money()
            elif s == 'remaining':
                self.print_status()
            elif s == 'exit':
                break

    def make_coffee(self, s1):
        espresso = {'water': 250,'milk': 0,'beans': 16,'cups': 1,'money': -4}
        latte = {'water': 350,'milk': 75,'beans': 20,'cups': 1,'money': -7}
        cappuccino = {'water': 200,'milk': 100,'beans': 12,'cups': 1,'money': -6}
        menu = [espresso, latte, cappuccino]
        if s1 == 'back':
            return None
        else:
            i = int(s1) - 1
            for key in self.machine:
                if self.machine[key] >= menu[i][key]:
                    self.machine[key] = self.machine[key] - menu[i][key]
                else:
                    print(f'Need more {key}')
                    break
            print('I have enough resources, making you a coffee!')

    def fill_machine(self):
        print('Write how many ml of water you want to add:')
        water_add = int(input())
        self.machine['water'] = self.machine['water'] + water_add
        print('Write how many ml of milk you want to add:')
        milk_add = int(input())
        self.machine['milk'] = self.machine['milk'] + milk_add
        print('Write how many grams of coffee beans you want to add:')
        beans_add = int(input())
        self.machine['beans'] = self.machine['beans'] + beans_add
        print('Write how many disposable cups you want to add:')
        cups_add = int(input())
        self.machine['cups'] = self.machine['cups'] + cups_add

    def take_money(self):
        print()
        print(f"I gave you ${self.machine['money']}")
        print()
        self.machine['money'] = 0

    def print_status(self):
        print('The coffee machine has: ')
        print(f"{self.machine['water']} ml of water")
        print(f"{self.machine['milk']} ml of milk")
        print(f"{self.machine['beans']} g of coffee beans")
        print(f"{self.machine['cups']} disposable cups")
        print(f"${self.machine['money']} of money")
        print()



if __name__ == '__main__':
    Coffee_machine().main()
