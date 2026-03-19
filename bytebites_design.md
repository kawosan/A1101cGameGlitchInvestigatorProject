# ByteBites Final UML Class Diagram

## Class Diagram

+---------------------------+
|         Customer          |
+---------------------------+
| - name: str               |
| - purchase_history: list  |
+---------------------------+
| + add_to_history(order)   |
+---------------------------+

+---------------------------+
|         MenuItem          |
+---------------------------+
| - name: str               |
| - price: float            |
| - category: str           |
| - popularity: float       |
+---------------------------+

+---------------------------+
|           Menu            |
+---------------------------+
| - items: list             |
+---------------------------+
| + add_item(item)          |
| + filter_by_category(cat) |
| + sort_by_popularity()    |
+---------------------------+

+---------------------------+
|           Order           |
+---------------------------+
| - customer: Customer      |
| - items: list             |
+---------------------------+
| + add_item(item)          |
| + calculate_total()       |
+---------------------------+

## Relationships

- Customer --> Order        : A customer places one or more orders
- Order --> MenuItem        : An order contains one or more menu items
- Menu --> MenuItem         : A menu holds a collection of menu items

## Design Notes

- Menu and Order both hold lists of MenuItems but serve different purposes:
    Menu = the full catalog (filtering/sorting)
    Order = a single transaction (totaling)
- Customer stores past orders in purchase_history
- No external libraries needed — plain Python only