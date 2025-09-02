from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

power_on = True
while power_on:
    choice = input(f"What would you like? ({menu.get_items()}):")

    if choice in menu.get_items():
        chosen_drink = menu.find_drink(choice)

        # Check if resources are sufficient
        if coffee_maker.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)
        else:
            print("Refill needed.")

    elif choice == "report":
        """Print a report of available resources and current profit."""
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        """Reset the CoffeeMaker object (refills all resources)."""
        coffee_maker = CoffeeMaker()
    elif choice == "off":
        """Turn off the coffee machine simulation."""
        print("Shutting down.")
        power_on = False
    else:
        print("You typed invalid input, try again.")
