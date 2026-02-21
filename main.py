from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffe_machine():

    while True:

        # 주문
        choice = input(f"What would you like?{menu.get_items()}\n")
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else :
            drink = menu.find_drink(choice)
            # 제조
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

if __name__ == '__main__':
    coffe_machine()