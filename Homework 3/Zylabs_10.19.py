# 2095022
# EMAD ABBASI
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item.item_quantity = item_to_purchase.item_quantity
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
        option = input("Choose an option:\n")

        if option == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(item)
        elif option == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(item_name)
        elif option == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new quantity:\n"))
            item_to_modify = ItemToPurchase(item_name, item_quantity=item_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif option == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
        elif option == 'o':
            print("\nOUTPUT SHOPPING CART")
            shopping_cart.print_total()
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
