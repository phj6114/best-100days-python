from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffe_machine():

    while True:
        menu = Menu()
        coffee_maker = CoffeeMaker()
        money_machine = MoneyMachine()

        # 주문
        user_chioce = input(f"What would you like?{menu.get_items()}\n")

        # 주문 메뉴 존재 확인
        menu_item = menu.find_drink(user_chioce)
        if menu_item is None:
            continue

        # 재료 잔량 확인
        if not coffee_maker.is_resource_sufficient(menu_item):
            continue

        # 비용 안내
        print(f"price is {menu_item.cost}")

        # 비용 지불 - 금액 부족할 경우 break
        if not money_machine.make_payment(menu_item.cost):
            break

        # 음료 제조
        coffee_maker.make_coffee(menu_item)

        # 리포트 출력
        coffee_maker.report()

if __name__ == '__main__':
    coffe_machine()