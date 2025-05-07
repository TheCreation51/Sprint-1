# This code will define a class called drink where it will take the base, size, flavors and calculate the price of a drink. 

class Drink: 


    bases = ["Water", "Sbrite", "Pokeacola", "Mr.Salt", "Hill Fog", "Leaf Wine"]
    flavors = ["Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", "Lime"]
    sizes = {"Small": 1.50, "Medium": 1.75, "Large": 2.05, "Mega": 2.15}
    additional_flavor_cost = 0.15

    def __init__(self):
        self.base = None
        self.flavors = []
        self.size = None

    def get_base(self):
        return self.base
    
    def get_flavors(self):
        return list(self.flavors)
    
    def get_size(self):
        return self.size
    
    def set_base(self, base):
        base = base.title()
        if base in self.bases:
            self.base = base
        else:
            raise ValueError(f"Invalid base. Valid options are: {', '.join(self.bases)}")
    
    def set_size(self, size):
        size = size.title()
        if size in self.sizes:
            self.size = size
        else:
            raise ValueError(f"Invalid size. Valid options are: {', '.join(self.sizes.keys())}")
    
    def add_flavor(self, flavor):
        flavor = flavor.title() 
        if flavor in Drink.flavors:
            if flavor not in self.flavors:
                self.flavors.append(flavor)
            else:
                raise ValueError(f"The flavor {flavor} has already been added.")
        else:
            raise ValueError(f"Invalid flavor. Valid options are: {', '.join(Drink.flavors)}")
    
    def calculate_price(self):
        if not self.size:
            raise ValueError("Size must be set before calculating price.")
        base_price = Drink.sizes[self.size]
        additional_flavors_cost = len(self.flavors) * Drink.additional_flavor_cost
        return base_price + additional_flavors_cost

class Food:

    
    food_items = {"Hotdog": 2.30, "Corndog": 2.00, "Ice Cream": 3.00, "Onion Rings": 1.75, "French Fries": 1.50, "Tater Tots": 1.70, "Nacho Chips": 1.90}
    toppings = {"Cherry": 0.00, "Whipped Cream": 0.00, "Caramel Sauce": 0.50, "Chocolate Sauce": 0.50, "Nacho Cheese": 0.30, "Chili": 0.60, "Bacon Bits": 0.30, "Ketchup": 0.00, "Mustard": 0.00}

    def __init__(self):
        self.food_item = None
        self.toppings = []

    def set_food_item(self, food_item):
        food_item = food_item.title()
        if food_item in self.food_items:
            self.food_item = food_item
        else:
            raise ValueError(f"Invalid food item. Valid options are: {', '.join(self.food_items.keys())}")

    def add_topping(self, topping):
        topping = topping.title()
        if topping in self.toppings:
            raise ValueError(f"The topping {topping} has already been added.")
        if topping in Food.toppings.keys():
            self.toppings.append(topping)
        else:
            raise ValueError(f"Invalid topping. Valid options are: {', '.join(Food.toppings.keys())}")

    def calculate_price(self):
        if not self.food_item:
            raise ValueError("Food item must be set before calculating price.")
        base_price = self.food_items[self.food_item]
        toppings_cost = sum(Food.toppings[topping] for topping in self.toppings)
        return base_price + toppings_cost

    def get_food_item(self):
        return self.food_item

    def get_toppings(self):
        return list(self.toppings)

class Order: 
    tax_rate = 0.0725
    
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items
    
    def get_receipt(self):
        receipt = []
        total = 0
        drink_count = 0
        food_count = 0

        for item in self._items:
            if isinstance(item, Drink):
                drink_count += 1
                item_price = item.calculate_price()
                receipt.append(
                    f"Drink {drink_count}: Base - {item.get_base()}, Size - {item.get_size()}, "
                    f"Flavors - {', '.join(item.get_flavors())}, Price - ${item_price:.2f}"
                )
            elif isinstance(item, Food):
                food_count += 1
                item_price = item.calculate_price()
                receipt.append(
                    f"Food {food_count}: Base - {item.get_food_item()}, Toppings - {', '.join(item.get_toppings())}, "
                    f"Price - ${item_price:.2f}"
                )
            total += item_price

        # calculating the total price
        tax = total * self.tax_rate
        total_with_tax = total + tax
        receipt.append(f"\nSubtotal: ${total:.2f}")
        receipt.append(f"Tax: ${tax:.2f}")
        receipt.append(f"Total: ${total_with_tax:.2f}")
        return "\n".join(receipt)
    
    def add_item(self, item):
        if isinstance(item, (Drink, Food)):
            self._items.append(item)
        else:
            raise TypeError("Only Drink or Food objects can be added to the order.")
        
# gathering data from order_data in order to create the actual order 
def create_order(order_data):
    order = Order()

    for item_data in order_data:
        if item_data.get("type") == "Drink":
            drink = Drink()
            try:
                drink.set_base(item_data["base"])
                drink.set_size(item_data["size"])
                for flavor in item_data.get("flavors", []):
                    drink.add_flavor(flavor)
                order.add_item(drink)
            except ValueError as e:
                return {"error": str(e)}
        elif item_data.get("type") == "Food":
            food = Food()
            try:
                food.set_food_item(item_data["food_item"])
                for topping in item_data.get("toppings", []):
                    food.add_topping(topping)
                order.add_item(food)
            except ValueError as e:
                return {"error": str(e)}

    return {"receipt": order.get_receipt()}

# testing the code by creating an order 
order_data = [
    {"type": "Drink", "base": "Water", "size": "Small", "flavors": ["Lemon", "Mint"]},
    {"type": "Drink", "base": "Pokeacola", "size": "Mega", "flavors": ["Cherry"]},
    {"type": "Food", "food_item": "Hotdog", "toppings": ["Caramel Sauce", "Ketchup", "Mustard"]},
    {"type": "Food", "food_item": "Ice Cream", "toppings": ["Cherry", "Nacho Cheese", "Bacon Bits"]},
]

result = create_order(order_data)

if "error" in result:
    print("Error:", result["error"])
else:
    print(result["receipt"])