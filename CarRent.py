class Dealer:

    def __init__(self, cars, prices):
        self.cars = cars
        self.prices = prices

    def show_cars(self):

        for car in self.cars:
            print(car)

    def show_prices(self):
        print('Which one?')
        choice = input()

        if choice in self.prices:
            print(self.prices[choice])


class Customer:

    def __init__(self, money):
        self.money = money
        self.garage = []

    def rent(self):
        choice = input('I want to rent ')

        if choice == 'nothing':
            quit()

        else:

            time = int(input('for '))
            print('days')

            if choice in dealer.cars:
                cost = dealer.prices[choice]*time

                if self.money >= cost:
                    self.money -= cost
                    customer.garage.append(choice)
                    dealer.cars.remove(choice)
                    print(f'Nice to have a deal with you, your current balance is {self.money}$')

                else:
                    print(f'You do not have enough money, your current balance is {self.money}$')

            else:
                print('Sorry, this car is unavailable now.')


listOfCars = ['HatchBack', 'Sedan', 'SUV']
listOfPrices = {'HatchBack': 30, 'Sedan': 50, 'SUV': 100}
capital = 100000

dealer = Dealer(listOfCars, listOfPrices)
customer = Customer(capital)

while True:

    print('Enter 1 to look at the cars')
    print('Enter 2 to see the prices')
    print('Enter 3 to start trading')
    print('Enter 4 to open your garage')
    print('Enter q to exit from shop')

    try:
        customerChoice = int(input())

        if customerChoice == 1:
            dealer.show_cars()
        elif customerChoice == 2:
            dealer.show_prices()
        elif customerChoice == 3:
            customer.rent()
        elif customerChoice == 4:
            print(customer.garage)
        elif customerChoice == 'q':
            quit()
    except ValueError:
        print('emm.. Okay! See you again')
        quit()
