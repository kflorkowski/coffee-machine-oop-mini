class MenuItem:
    """Class representing a single menu item.

    Attributes:
        name (str): Name of the drink.
        cost (float): Price of the drink.
        ingredients (dict): Required ingredients (water, milk, coffee).
    """

    def __init__(self, name, water, milk, coffee, cost):
        """Initialize a MenuItem object.

        Args:
            name (str): Drink name.
            water (int): Amount of water in ml.
            milk (int): Amount of milk in ml.
            coffee (int): Amount of coffee in g.
            cost (float): Price in dollars.
        """
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Class representing the entire menu of available drinks."""

    def __init__(self):
        """Initialize the menu with default items."""
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Return the names of all available drinks as a formatted string.

        Returns:
            str: Slash-separated list of drink names, e.g. "latte/espresso/cappuccino".
        """

        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        """Find a drink by name.

        Args:
            order_name (str): Name of the drink.

        Returns:
            MenuItem | None: The matching MenuItem if found, otherwise None.
        """

        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
