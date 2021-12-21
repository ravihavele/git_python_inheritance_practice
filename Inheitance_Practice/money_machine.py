class MoneyMachine:

    # CURRENCY = "$"
    CURRENCY_Rs = "₹"
    profit = 0
    money_received = 0

    # COIN_VALUES = {
    #         "quarters": 0.25,
    #         "dimes": 0.10,
    #         "nickles": 0.05,
    #         "pennies": 0.01
    # }

    COIN_VALUES_RS = {
        "Ten Rupees": 10,
        "Twenty Rupees": 20,
        "Fifty Rupees": 50,
        "Hundred Rupees": 100
    }

    # def __init__(self):
    #     self.profit = 0
    #     self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY_Rs }{self.profit}")

    # def process_coins(self):
    #     """Returns the total calculated from coins inserted."""
    #     print("Please insert coins.")
    #     for coin in self.COIN_VALUES:
    #         self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
    #     return self.money_received

    def process_Rupees(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert Rupees.")
        for coin in self.COIN_VALUES_RS:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES_RS[coin]
        return self.money_received

    # def make_payment(self, cost):
    #     """Returns True when payment is accepted, or False if insufficient."""
    #     self.process_coins()
    #     if self.money_received >= cost:
    #         change = round(self.money_received - cost, 2)
    #         print(f"Here is {self.CURRENCY}{change} in change.")
    #         self.profit += cost
    #         self.money_received = 0
    #         return True
    #     else:
    #         print("Sorry that's not enough money. Money refunded.")
    #         self.money_received = 0
    #         return False

    def make_payment_Rs(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_Rupees()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY_Rs}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        
