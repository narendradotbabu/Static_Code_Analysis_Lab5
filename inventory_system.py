

import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    
    if logs is None:
        logs = []
    if not isinstance(item, (str, int)):
        logging.error("Invalid item type: %s", type(item))
        return
    if not isinstance(qty, (int, float)):
        logging.error("Invalid quantity type: %s", type(qty))
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %s (Qty: %s)", item, qty)


def remove_item(item, qty):
    
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        logging.warning("Attempted to remove a non-existing item: %s", e)
    except (TypeError, ValueError) as e:
        logging.error("Unexpected error while removing item: %s", e)


def get_qty(item):
    
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
  
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        stock_data.clear()
        stock_data.update(data)
        logging.info("Inventory data loaded successfully from %s", file)
    except FileNotFoundError:
        logging.warning("File not found: %s. Starting with empty stock.", file)
    except json.JSONDecodeError as e:
        logging.error("JSON decode error: %s", e)


def save_data(file="inventory.json"):
    
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Inventory data saved to %s", file)


def print_data():
   
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
   
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
   
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Eval removed for safety!")


if __name__ == "__main__":
    main()
