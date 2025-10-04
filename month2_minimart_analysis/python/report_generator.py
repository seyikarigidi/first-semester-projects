# Code to generate dictionary summary reports
import json
import os
from collections import Counter

BASE_DIR = os.path.dirname(__file__)
REPORT_FILE = os.path.join(BASE_DIR, "report.json")


def generate_report(orders):
    if not orders:
        return {"message": "No orders available."}

    total_products_sold = sum(o.get("quantity", 0) for o in orders)

    product_counts = Counter(o.get("product") for o in orders)
    most_popular = product_counts.most_common(1)[0][0] if product_counts else None

    revenue_per_customer = {}
    for o in orders:
        revenue_per_customer[o["customer"]] = revenue_per_customer.get(o["customer"], 0) + o.get("total_usd", 0)

    report = {
        "total_products_sold": total_products_sold,
        "most_popular_product": most_popular,
        "revenue_per_customer": revenue_per_customer,
    }
    return report


def save_report(report):
    """Save the report dict to report.json"""
    with open(REPORT_FILE, "w") as f:
        json.dump(report, f, indent=4)
