# ByteBites UML Class Diagram (Draft)

## Customer
| Attribute        | Type   |
|------------------|--------|
| name             | str    |
| purchase_history | list   |

## MenuItem
| Attribute  | Type   |
|------------|--------|
| name       | str    |
| price      | float  |
| category   | str    |
| popularity | float  |

## Menu
| Attribute | Type |
|-----------|------|
| items     | list |

| Method              | Returns      |
|---------------------|--------------|
| add_item(item)      | None         |
| filter_by_category()| list         |
| sort_by_popularity()| list         |

## Order
| Attribute | Type |
|-----------|------|
| customer  | Customer |
| items     | list |

| Method            | Returns |
|-------------------|---------|
| add_item(item)    | None    |
| calculate_total() | float   |

## Relationships
- A Customer can have many Orders
- An Order contains many MenuItems
- A Menu contains many MenuItems