from models import Customer, MenuItem, Menu, Order


# --- Setup Helpers ---

def make_menu():
    """Creates a reusable menu with sample items."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 9.99, "Entrees", 4.8))
    menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.5))
    menu.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.2))
    menu.add_item(MenuItem("Water", 1.00, "Drinks", 3.0))
    menu.add_item(MenuItem("Fries", 3.49, "Entrees", 4.0))
    return menu


def make_customer():
    """Creates a reusable customer."""
    return Customer("Alice")


# --- Order Total Tests ---

def test_order_total_with_multiple_items():
    """Verify that adding multiple items calculates the correct total."""
    customer = make_customer()
    order = Order(customer)
    order.add_item(MenuItem("Spicy Burger", 9.99, "Entrees", 4.8))
    order.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.5))
    assert round(order.calculate_total(), 2) == 12.48


def test_order_total_is_zero_when_empty():
    """Verify that an empty order returns a total of $0."""
    customer = make_customer()
    order = Order(customer)
    assert order.calculate_total() == 0


def test_order_total_with_single_item():
    """Verify that a single item order returns that item's price."""
    customer = make_customer()
    order = Order(customer)
    order.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.2))
    assert round(order.calculate_total(), 2) == 4.99


# --- Filter Tests ---

def test_filter_by_category_returns_correct_items():
    """Verify that filtering Drinks returns only drink items."""
    menu = make_menu()
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)


def test_filter_by_nonexistent_category_returns_empty():
    """Verify that filtering a category with no matches returns an empty list."""
    menu = make_menu()
    result = menu.filter_by_category("Sushi")
    assert result == []


def test_filter_does_not_affect_original_menu():
    """Verify that filtering doesn't remove items from the menu."""
    menu = make_menu()
    menu.filter_by_category("Drinks")
    assert len(menu.items) == 5


# --- Sorting Tests ---

def test_sort_by_popularity_descending():
    """Verify that items are sorted from most to least popular."""
    menu = make_menu()
    sorted_items = menu.sort_by_popularity()
    popularities = [item.popularity for item in sorted_items]
    assert popularities == sorted(popularities, reverse=True)


def test_sort_does_not_affect_original_menu():
    """Verify that sorting doesn't change the original menu order."""
    menu = make_menu()
    original_first = menu.items[0].name
    menu.sort_by_popularity()
    assert menu.items[0].name == original_first


# --- Customer Tests ---

def test_customer_history_updates_after_order():
    """Verify that adding an order to history saves it correctly."""
    customer = make_customer()
    order = Order(customer)
    order.add_item(MenuItem("Fries", 3.49, "Entrees", 4.0))
    customer.add_to_history(order)
    assert len(customer.purchase_history) == 1


def test_customer_starts_with_empty_history():
    """Verify that a new customer has no purchase history."""
    customer = make_customer()
    assert customer.purchase_history == []