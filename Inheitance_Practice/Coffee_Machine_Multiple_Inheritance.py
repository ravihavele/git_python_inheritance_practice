from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine(Menu, MenuItem, CoffeeMaker, MoneyMachine):
    pass

cm = CoffeeMachine()
is_on = True
while is_on:
    choice = input(f"What would you like ? ({cm.get_items()}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cm.report_ingdt()
        cm.report()
    else:
        drink = cm.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            # process_coins()
            if cm.make_payment_Rs(drink.cost):
                cm.make_coffee(drink)

