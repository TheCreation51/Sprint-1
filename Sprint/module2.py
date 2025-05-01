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

class Order: 
    tax_rate = 0.0725
    
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items
    
    def get_receipt(self):
        receipt = []
        total = 0
        for index, drink in enumerate(self._items, start=1):
            drink_price = drink.calculate_price()
            total += drink_price
            receipt.append(
                f"Drink {index}: Base - {drink.get_base()}, Size - {drink.get_size()}, "
                f"Flavors - {', '.join(drink.get_flavors())}, Price - ${drink_price:.2f}"
            )
        # calculating the total price

        tax = total * self.tax_rate
        total_with_tax = total + tax
        receipt.append(f"\nSubtotal: ${total:.2f}")
        receipt.append(f"Tax: ${tax:.2f}")
        receipt.append(f"Total: ${total_with_tax:.2f}")
        return "\n".join(receipt)
    
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise TypeError("Only Drink objects can be added to the order.")
        
# gathering data from order_data in order to create the actual order 
def create_order(order_data):
    
    order = Order()

    for drink_data in order_data:
        drink = Drink()
        try:
            drink.set_base(drink_data["base"])
            drink.set_size(drink_data["size"])
            for flavor in drink_data.get("flavors", []):
                drink.add_flavor(flavor)
            order.add_item(drink)
        except ValueError as e:
            return {"error": str(e)}

    return {"receipt": order.get_receipt()}

# testing the code by creating an order 
order_data = [
    {"base": "Water", "size": "SHaha", "flavors": ["Lemon", "Mint",]},
    {"base": "Pokeacola", "size": "Mega", "flavors": ["Cherry"]},
    {"base": "Pokeacola", "size": "Mega", "flavors": ["Strawberry","Mint", "Lime"]},
]

result = create_order(order_data)

if "error" in result:
    print("Error:", result["error"])
else:
    print(result["receipt"])