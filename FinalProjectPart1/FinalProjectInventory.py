# 2095022
# EMAD ABBASI
# THIS IS PART 2 OF THE PROJECT WHERE WE GENERATE INVENTORY RELATED CODE FOR THE FIRST PART
import csv
from datetime import datetime


class InventoryItem:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

    @classmethod
    def from_manufacturer_list_row(cls, row):
        item_id, manufacturer, item_type, *damaged = row
        return cls(item_id, manufacturer, item_type, None, None, bool(damaged and damaged[0].lower() == 'damaged'))

    def update_price(self, price):
        self.price = float(price)

    def update_service_date(self, service_date):
        self.service_date = datetime.strptime(service_date, '%m/%d/%Y')


def read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))


manufacturer_list = read_csv('ManufacturerList.csv')
price_list = read_csv('PriceList.csv')
service_dates_list = read_csv('ServiceDatesList.csv')

item_dict = {row[0]: InventoryItem.from_manufacturer_list_row(row) for row in manufacturer_list}

for row in price_list:
    item_id, price = row
    if item_id in item_dict:
        item_dict[item_id].update_price(price)

for row in service_dates_list:
    item_id, service_date = row
    if item_id in item_dict:
        item_dict[item_id].update_service_date(service_date)


def find_best_item(manufacturer, item_type, include_damaged):
    items = [item for item in item_dict.values() if
             item.manufacturer.strip().lower() == manufacturer.lower() and item.item_type.strip().lower() == item_type.lower()]
    if include_damaged:
        valid_items = [item for item in items if item.damaged and item.service_date > datetime.now()]
    else:
        valid_items = [item for item in items if not item.damaged and item.service_date > datetime.now()]

    max_price = -1
    best_item = None
    for item in valid_items:
        if item.price > max_price:
            max_price = item.price
            best_item = item
    return best_item


def find_alternative_item(item):
    alternative_items = [i for i in item_dict.values() if
                         i.item_type.lower() == item.item_type.strip().lower() and i.manufacturer.lower() != item.manufacturer.strip().lower() and not i.damaged and i.service_date > datetime.now()]

    alternative_item = None
    for i in alternative_items:
        if item.item_type.lower() == i.item_type.lower() and item.manufacturer.lower() != i.manufacturer.lower() and abs(
                item.price - i.price) / item.price <= 2:
            alternative_item = i
    return alternative_item


while True:
    manufacturer = ""
    item_type = ""
    include_damaged = False
    damaged_input = ""

    try:
        manufacturer, item_type = input(
            "Enter the manufacturer & item type with , as the delimeter (splitting character) between the two values. Enter 'q' to quit: ").split(",")
        damaged_input = input("Should damaged items be included (Y/N): ")
    except ValueError:
        if manufacturer.lower() == 'q':
            print("Exiting the system")
            break
        else:
            print("Invalid Command Entered. Please enter MANUFACTURER;ITEM TYPE to search.")
            continue

    manufacturer = manufacturer.strip()
    item_type = item_type.strip()

    if damaged_input.lower() == "y":
        include_damaged = True

    best_item = find_best_item(manufacturer, item_type, include_damaged)
    if best_item is None:
        print("No such item in inventory")
    else:
        print(
            f"Your item is:  {best_item.item_id}, {best_item.manufacturer}, {best_item.item_type}, ${best_item.price}")
        alternative_item = find_alternative_item(best_item)
        if alternative_item is not None:
            print(
                f"You may, also, consider: {alternative_item.item_id}, {alternative_item.manufacturer}, {alternative_item.item_type}, ${alternative_item.price}")