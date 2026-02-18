from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffe_machine():
    menu = Menu()

    user_chioce = input(f"What would you like?{menu.get_items()}\n")

    if menu.find_drink(user_chioce) is None:
        return

    coffee_maker = CoffeeMaker()
    coffee_maker.is_resource_sufficient(menu)

if __name__ == '__main__':
    coffe_machine()