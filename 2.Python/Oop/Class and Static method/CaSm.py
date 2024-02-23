import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, id: str, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        items = None
        try:
            with open("D:\\Study\\MyCode\\2.Python\\Oop\\Class and Static method\\items.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile) 
                items = list(reader)   
                # Process CSV data here
                print("Successfully read items.csv!")
        except FileNotFoundError:
            print("Error: File 'items.csv' not found. Please check the file path and permissions.")

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
                id=item.get('id')
            )

    @staticmethod
    def is_interger(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"('{self.name}', '{self.price}', '{self.quantity}', '{self.id}')"

# print(Item.is_interger(7.0))


Item.instantiate_from_csv()
print("\nAll Items:")
items = [f"Item {item}" for item in Item.all]
print(*items, sep="\n")
