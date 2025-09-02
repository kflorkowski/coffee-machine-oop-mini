class CoffeeMaker:
    """
    Class representing a coffee machine that manages available resources
    (water, milk, coffee) and prepares drinks based on given recipes.

    Attributes:
        resources (dict): Available resources (water, milk, coffee).
    """

    def __init__(self):
        """Initialize the coffee machine with default resource amounts."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Print a report of current resource levels (water, milk, coffee)."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Check if there are enough resources to prepare the selected drink.

        Args:
            drink (MenuItem): The drink object containing required ingredients.

        Returns:
            bool: True if resources are sufficient, False otherwise.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Prepare the coffee by deducting ingredients from the resources.

        Args:
            order (MenuItem): The drink to be prepared.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
