class Drink: 
    bases = ["Water", "Sbrite", "Pokeacola", "Mr.Salt", "Hill Fog", "Leaf Wine"]
    flavors = ["Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", "Lime"]

    def __init__(self):
            self.base = []
            self.flavors = []

    def get_base(self):
            return self.base
        
    def get_flavors(self):
            return list(self.flavors)
        
        
    def set_base(self, base):
            base = base.title()
            if base in self.bases:
                self.base = base
            else:
                raise ValueError(f"\nInvalid base. Valid options are: {', '.join(self.bases)}\n")
            
    def add_flavor(self, flavor):
        flavor = flavor.title() 
        if flavor in Drink.flavors:
            if flavor not in self.flavors:
                self.flavors.append(flavor)
            else:
                raise ValueError(f"The flavor {flavor} has already been added.")
        else:
            raise ValueError(f"\nInvalid flavor. Valid options are: {', '.join(Drink.flavors)}\n")
            
    def set_flavors(self, flavors):
        if not all(flavor in self.flavors for flavor in flavors):
            raise ValueError(f"One or more flavors are invalid. Valid options are: {', '.join(self.flavors)}")
        self.flavors = flavors



class Order: 
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items
    
    def get_receipt(self):
        receipt = []
        for index, drink in enumerate(self._items, start=1):
            receipt.append(f"Drink {index}: Base - {drink.get_base()}, Flavors - {', '.join(drink.get_flavors())}")
        return "\n".join(receipt)
    
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise TypeError("Only Drink objects can be added to the order.")

if __name__ == "__main__":
    order = Order()

    while True: 
        print ("Welcome to the Drink Order System!\n")
        drink = Drink()

        print(f"Available bases: {', '.join(Drink.bases)}")
        base = input("Please select a base: ").strip()
        try:
            drink.set_base(base)
        except ValueError as e:
            print(e)
            continue

        print(f"\nAvailable flavors: {', '.join(Drink.flavors)}")
        while True:
            flavor = input("Please select a flavor (or Enter to finish): ").strip()
            if not flavor:
                break
            try:
                drink.add_flavor(flavor)
            except ValueError as e:
                print(e)
        
        order.add_item(drink)
        print("\nDrink added to order!")

        another = input("Would you like to add another drink? (y/n): ").strip().lower()
        if another  != 'y':
            break

    print("\nYour order summary:")
    print(order.get_receipt())