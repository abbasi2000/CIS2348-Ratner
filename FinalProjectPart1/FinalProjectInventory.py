# 2095022
# EMAD ABBASI
# THIS IS PART 1 OF THE PROJECT WHERE WE GENERATE INVENTORY RELATED CODE FOR THE FIRST PART
import csv
from datetime import datetime


def read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))


def sort_by_manufacturer(items):
    return items[1]['manufacturer']


def sort_by_item_id(items):
    return items[0]


def sort_by_service_date(items):
    return items[1]['service_date']


def sort_by_price_desc(items):
    return -items[1]['price']


manufacturer_list = read_csv('ManufacturerList.csv')
price_list = read_csv('PriceList.csv')
service_dates_list = read_csv('ServiceDatesList.csv')

item_dict = {}

for row in manufacturer_list:
    item_id, manufacturer, item_type, *damaged = row
    item_dict[item_id] = {
        'manufacturer': manufacturer,
        'item_type': item_type,
        'damaged': bool(damaged and damaged[0].lower() == 'damaged')
    }

for row in price_list:
    item_id, price = row
    if item_id in item_dict:
        item_dict[item_id]['price'] = float(price)

for row in service_dates_list:
    item_id, service_date = row
    if item_id in item_dict:
        item_dict[item_id]['service_date'] = datetime.strptime(service_date, '%m/%d/%Y')

# FullInventory.csv
with open('FullInventory.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['item_id', 'manufacturer', 'item_type', 'price', 'service_date', 'damaged']
    writer.writerow(header)
    for item_id, item in sorted(item_dict.items(), key=sort_by_manufacturer):
        row = [
            item_id,
            item['manufacturer'],
            item['item_type'],
            item['price'],
            item['service_date'].strftime('%m/%d/%Y'),
            'damaged' if item['damaged'] else ''
        ]
        writer.writerow(row)

# Item type inventory list
item_types = set(item['item_type'] for item in item_dict.values())
for item_type in item_types:
    file_name = f'{item_type}Inventory.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        header = ['item_id', 'manufacturer', 'price', 'service_date', 'damaged']
        writer.writerow(header)
        for item_id, item in sorted(item_dict.items(), key=sort_by_item_id):
            if item['item_type'] == item_type:
                row = [
                    item_id,
                    item['manufacturer'],
                    item['price'],
                    item['service_date'].strftime('%m/%d/%Y'),
                    'damaged' if item['damaged'] else ''
                ]
                writer.writerow(row)

# PastServiceDateInventory.csv
today = datetime.now()
with open('PastServiceDateInventory.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['item_id', 'manufacturer', 'item_type', 'price', 'service_date', 'damaged']
    writer.writerow(header)
    for item_id, item in sorted(item_dict.items(), key=sort_by_service_date):
        if item['service_date'] < today:
            row = [item_id, item['manufacturer'],
                   item['item_type'],
                   item['price'],
                   item['service_date'].strftime('%m/%d/%Y'),
                   'damaged' if item['damaged'] else ''
                   ]
            writer.writerow(row)

# DamagedInventory.csv
with open('DamagedInventory.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['item_id', 'manufacturer', 'item_type', 'price', 'service_date']
    writer.writerow(header)
    for item_id, item in sorted(item_dict.items(), key=sort_by_price_desc):
        if item['damaged']:
            row = [item_id, item['manufacturer'],
                   item['item_type'],
                   item['price'],
                   item['service_date'].strftime('%m/%d/%Y')
                   ]
            writer.writerow(row)
