# Utility functions for data conversion and filtering

import json
import os


BASE_DIR = os.path.dirname(__file__)
ORDERS_FILE = os.path.join(BASE_DIR, "orders.json")

# Product catalog
products = [
    {"id": 1, "name": "Bread", "price": 20.0},
    {"id": 2, "name": "Milk", "price": 15.0},
    {"id": 3, "name": "Eggs", "price": 10.0},
    {"id": 4, "name": "Apples", "price": 5.0},
    {"id": 5, "name": "Rice", "price": 50.0},
]

orders = []

def load_orders():
    """Load orders from ORDERS_FILE into the global orders list."""
    global orders
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as f:
            try:
                orders = json.load(f)
            except json.JSONDecodeError:
                orders = []
    else:
        orders = []


def save_orders():
    """Save the global orders list to ORDERS_FILE."""
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)

def get_product_by_id(product_id):
    return next((p for p in products if p["id"] == product_id), None)

def place_order(customer, product_id, quantity):
    product = get_product_by_id(product_id)
    if not product:
        return None

    price = product["price"]
    subtotal = price * quantity

    # Quantity discount: 10% off if buying more than 10 units
    discount_pct = 0.10 if quantity > 10 else 0.0
    discount_amount = subtotal * discount_pct
    total_usd = round(subtotal - discount_amount, 2)

    is_large = total_usd > 100.0

    order = {
        "customer": customer,
        "product": product["name"],
        "product_id": product_id,
        "quantity": quantity,
        "unit_price_usd": round(price, 2),
        "discount_pct": round(discount_pct, 2),
        "discount_amount": round(discount_amount, 2),
        "total_usd": total_usd,
        "is_large": is_large,
    }

    orders.append(order)
    save_orders()
    return order


def convert_prices_to_eur(rate=0.9):
    """
    Convert product catalog prices to EUR.
    Also apply a conditional discount on converted unit price:
      - If converted unit price > 3 EUR, apply a 5% discount to that converted price. Returns a list of dicts: {"id","name","price_eur","discount_applied"}
    """
    converted = []
    for p in products:
        price_eur = round(p["price"] * rate, 2)
        discount_applied = False
        if price_eur > 3.0:
            price_eur = round(price_eur * 0.95, 2)  # 5% discount
            discount_applied = True
        converted.append({
            "id": p["id"],
            "name": p["name"],
            "price_eur": price_eur,
            "discount_applied": discount_applied
        })
    return converted


def list_products():
    return products


def view_orders():
    return orders
