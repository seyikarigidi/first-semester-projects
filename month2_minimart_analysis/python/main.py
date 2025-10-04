# Entry point for the MiniMart data reporting system

import json
from utils import (
    load_orders,
    list_products,
    place_order,
    view_orders,
    convert_prices_to_eur,
)
from report_generator import generate_report, save_report

def show_menu():
    print("\n= Welome to MiniMart Sales System")
    print("1. View Products")
    print("2. Place Order")
    print("3. View Orders")
    print("4. Convert Prices to EUR (with conversion discounts)")
    print("5. Generate & Save Report")
    print("6. Exit")

def pretty_print_orders(orders):
    if not orders:
        print("No orders yet.")
        return
    for i, o in enumerate(orders, start=1):
        print(f"{i}. {o['customer']} | {o['product']} x{o['quantity']} | ${o['total_usd']:.2f} | Discount: {o['discount_pct']*100:.0f}% | Large: {o['is_large']}")

def main():
    # Load persisted orders
    load_orders()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("\nProducts")
            for p in list_products():
                print(f"{p['id']}. {p['name']} - ${p['price']:.2f}")
        elif choice == "2":
            customer = input("Enter customer name: ").strip()
            try:
                product_id = int(input("Enter product ID: ").strip())
                quantity = int(input("Enter quantity: ").strip())
            except ValueError:
                print("Invalid input: product ID and quantity must be integers.")
                continue
            order = place_order(customer, product_id, quantity)
            if order is None:
                print("Invalid product ID. Order not placed.")
            else:
                print("Order placed successfully:")
                print(json.dumps(order, indent=4))
                if order["is_large"]:
                    print("⚠️ Large order flagged (> $100).")
        elif choice == "3":
            print("\nOrders")
            pretty_print_orders(view_orders())
        elif choice == "4":
            print("\nConverted Prices (EUR)")
            converted = convert_prices_to_eur()
            for c in converted:
                note = " (discount applied)" if c["discount_applied"] else ""
                print(f"{c['id']}. {c['name']} - €{c['price_eur']:.2f}{note}")
        elif choice == "5":
            orders = view_orders()
            report = generate_report(orders)
            print("\nReport")
            print(json.dumps(report, indent=4))
            save_report(report)
            print("Report saved to report.json")
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
