# models.py
# ByteBites Core Classes:
# 1. Customer  - user with name and purchase history
# 2. MenuItem  - food item with name, price, category, popularity
# 3. Menu      - collection of MenuItems with filter/sort
# 4. Order     - selected items and total cost calculation

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_to_history(self, order):
        self.purchase_history.append(order)

    def __repr__(self):
        return f"Customer(name={self.name})"


class MenuItem:
    def __init__(self, name, price, category, popularity):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity

    def __repr__(self):
        return f"MenuItem(name={self.name}, price=${self.price}, category={self.category})"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity, reverse=True)

    def __repr__(self):
        return f"Menu({len(self.items)} items)"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def __repr__(self):
        return f"Order(customer={self.customer.name}, total=${self.calculate_total():.2f})"
    
    # --- Manual Check ---
if __name__ == "__main__":

    # --- Setup ---
    burger = MenuItem("Spicy Burger", 9.99, "Entrees", 4.8)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 3.5)
    cake = MenuItem("Chocolate Cake", 4.99, "Desserts", 4.2)
    water = MenuItem("Water", 1.00, "Drinks", 3.0)
    fries = MenuItem("Fries", 3.49, "Entrees", 4.0)

    menu = Menu()
    for item in [burger, soda, cake, water, fries]:
        menu.add_item(item)

    # --- Test Filtering ---
    print("=== Filter by Drinks ===")
    drinks = menu.filter_by_category("Drinks")
    for d in drinks:
        print(" ", d)

    print("\n=== Filter by Entrees ===")
    entrees = menu.filter_by_category("Entrees")
    for e in entrees:
        print(" ", e)

    print("\n=== Filter by nonexistent category ===")
    none = menu.filter_by_category("Sushi")
    print(" ", none)  # Should print []

    # --- Test Sorting ---
    print("\n=== Sort by Popularity ===")
    sorted_items = menu.sort_by_popularity()
    for item in sorted_items:
        print(f"  {item.name} - {item.popularity}")

    # --- Test Order Total ---
    print("\n=== Order Total ===")
    customer = Customer("Alice")
    order = Order(customer)
    order.add_item(burger)
    order.add_item(soda)
    print(f"  Expected: $12.48 | Got: ${order.calculate_total():.2f}")

    # --- Test Empty Order ---
    print("\n=== Empty Order ===")
    empty_order = Order(customer)
    print(f"  Expected: $0.00 | Got: ${empty_order.calculate_total():.2f}")

    # --- Test Customer History ---
    print("\n=== Customer History ===")
    customer.add_to_history(order)
    print(f"  {customer.name} has {len(customer.purchase_history)} order(s)")