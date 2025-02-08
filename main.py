### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if ingredients["bread"] <= self.machine_resources["bread"] and ingredients["ham"] <= self.machine_resources["ham"] and ingredients["cheese"] <= self.machine_resources["cheese"]:
            return True
        return False


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print('Please insert coins.')
        large_dollars = float(input("how many large dollars?: "))
        half_dollars = float(input("how many half dollars?: "))
        quarters = float(input("how many quarters: "))
        nickels = float(input("how many nickels: "))
        return float(large_dollars + (half_dollars * 0.5) + (quarters * 0.25 ) + (nickels * 0.05))

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        return False



    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

        for resource in resources.keys():
            resources[resource] -= order_ingredients[resource]
        print(sandwich_size + " sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###

##Creating sandwich machine object
SandwichMachine = SandwichMachine(resources)

user_input = ""

while user_input != "off":

    user_input = input("What would you like? (small/ medium/ large/ off/ report): ")

    if user_input == "off":
        break

    if user_input == "report":
        print("Bread: " + str(resources['bread']) + " slice(s)")
        print("Ham: " + str(resources['ham']) + " slice(s)")
        print("Cheese: " + str(resources['cheese']) + " pound(s)")
        continue

    if SandwichMachine.check_resources(recipes[user_input]["ingredients"]):
        coins_collected = SandwichMachine.process_coins()
        if SandwichMachine.transaction_result(float(coins_collected), float(recipes[user_input]["cost"])):
             print('Here is $'+ str(round(coins_collected - recipes[user_input]["cost"], 2)) + ' in change.')
             SandwichMachine.make_sandwich(user_input, recipes[user_input]["ingredients"])
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        for resource in resources.keys():
            if resources[resource] - recipes[user_input]["ingredients"][resource] < 0:
                print("Sorry there is not enough" + " " + resource + "")
                break
