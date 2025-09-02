# CoffeeMachineOOP
This is an educational project developed for learning and practicing Object-Oriented Programming (OOP) in Python. The program allows users to interact with a virtual coffee machine: order drinks, manage resources (like water, milk, coffee), process payments using virtual coins, and generate reports.

## Installation guide
This project does not require any external dependencies, it runs entirely with Python’s standard library.

1. Make sure you have Python 3.6 or higher installed.
2. Download CoffeMachine project.
3. Open a terminal and navigate to the project folder.
4. Run the script: `python main.py`

## Usage guide
After starting the script, the machine will display: 
`What would you like? (espresso/latte/cappuccino):`

You can type one of the following commands:

| Command                             | Description                                              |
|-------------------------------------|----------------------------------------------------------|
| `espresso` / `latte` / `cappuccino` | Order selected coffee type                               |
| `report`                            | Display current levels of water, milk, coffee, and money |
| `refill`                            | Refill all resources to their maximum capacity           |
| `off`                               | Turn off the machine                                     |

Coffee ordering process

1. Choose a drink - e.g. `latte`.

2. Resources check - the machine verifies if resources are sufficient.

    - If not enough resources - a message will be displayed: `Sorry there is not enough water`.

    - If resources are sufficient - the program proceeds to payment.

3. Payment - insert coins by specifying the number of quarters, dimes, nickels, and pennies.

    - If the amount is insufficient - money is refunded.

    - If sufficient - change is calculated (if needed) and the coffee is brewed.

4. Enjoy your coffee! ☕

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.