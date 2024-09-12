"""
Author: Hisham Macaraya
Date: 2024-08-03
Program Topic: Object-Oriented Programming, Classes, Objects, Inheritance, Dictionary, Functions, Selections, Loops
Program Description: This program implements an Inventory Management System using dictionaries, functions, selections, and loops. 
The system keeps track of products, their quantities, and prices. It allows the user to add new products, update existing product 
information, view the inventory, and search for products.
"""

# Constants for menu choices
ADD_PRODUCT = '1'
UPDATE_PRODUCT = '2'
VIEW_INVENTORY = '3'
SEARCH_PRODUCT = '4'
EXIT = '5'

def display_menu():
    """Displays the menu options to the user."""
    print("Inventory Management System")
    print("1. Add New Product")
    print("2. Update Existing Product")
    print("3. View All Products")
    print("4. Search for a Product")
    print("5. Exit")

def add_product(inventory):
    """
    Adds a new product to the inventory.
    Args:
        inventory (dict): The inventory dictionary.
    Returns:
        dict: Updated inventory dictionary.
    """
    product_id = input("Enter Product ID: ")
    if product_id in inventory:
        print("Product ID already exists.")
        return inventory
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Product Quantity: "))
    price = float(input("Enter Product Price: "))
    inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
    print("Product added successfully.")
    return inventory

def update_product(inventory):
    """
    Updates an existing product in the inventory.
    Args:
        inventory (dict): The inventory dictionary.
    Returns:
        dict: Updated inventory dictionary.
    """
    product_id = input("Enter Product ID to update: ")
    if product_id not in inventory:
        print("Product ID not found.")
        return inventory
    name = input("Enter New Product Name: ")
    quantity = int(input("Enter New Product Quantity: "))
    price = float(input("Enter New Product Price: "))
    inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
    print("Product updated successfully.")
    return inventory

def view_inventory(inventory):
    """
    Displays all products in the inventory.
    Args:
        inventory (dict): The inventory dictionary.
    """
    if not inventory:
        print("No products in inventory.")
        return
    for product_id, details in inventory.items():
        print(f"Product ID: {product_id}")
        print(f"Name: {details['name']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Price: ${details['price']:.2f}")
        print("-" * 20)

def search_product(inventory):
    """
    Searches for a product in the inventory by its ID.
    Args:
        inventory (dict): The inventory dictionary.
    """
    product_id = input("Enter Product ID to search: ")
    if product_id not in inventory:
        print("Product ID not found.")
        return
    details = inventory[product_id]
    print(f"Product ID: {product_id}")
    print(f"Name: {details['name']}")
    print(f"Quantity: {details['quantity']}")
    print(f"Price: ${details['price']:.2f}")

def main():
    """Main function to run the Inventory Management System."""
    inventory = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == ADD_PRODUCT:
            inventory = add_product(inventory)
        elif choice == UPDATE_PRODUCT:
            inventory = update_product(inventory)
        elif choice == VIEW_INVENTORY:
            view_inventory(inventory)
        elif choice == SEARCH_PRODUCT:
            search_product(inventory)
        elif choice == EXIT:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()