class MoneyMachine:
    """A class simulating a payment system for the coffee machine."""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):

        """Initialize with zero profit and no money received."""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print the current total profit."""

        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Prompt the user to insert coins and calculate the total amount.

        Returns:
            float: The total amount of money inserted.
        """

        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Handle payment for a drink.

        Args:
            cost (float): The price of the drink.

        Returns:
            bool: True if the payment was sufficient, False otherwise.
        """

        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
