def show_menu():
    print("\n===== SHOPPING LIST =====")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Clear List")
    print("5. Exit")


def add_item(shopping_list, prices, quantities):
    item = input("Enter item name: ")

    if item == "":
        print("Item name cannot be empty.")
    else:
        try:
            price = float(input("Enter item price: Rs. "))
            quantity = int(input("Enter quantity: "))

            shopping_list.append(item)
            prices.append(price)
            quantities.append(quantity)

            print(f"{item} has been added to your shopping list!")

        except ValueError:
            print("Please enter valid values.")


def view_list(shopping_list, prices, quantities):
    if len(shopping_list) == 0:
        print("Your shopping list is empty.")
    else:
        print("\n===== YOUR SHOPPING LIST =====")

        total = 0

        for count, (item, price, quantity) in enumerate(
                zip(shopping_list, prices, quantities), start=1):

            subtotal = price * quantity
            total += subtotal

            print(
                f"{count}. {item} | Qty: {quantity} | "
                f"Price: Rs. {price:.2f} | Subtotal: Rs. {subtotal:.2f}"
            )

        print(f"\nTotal items: {len(shopping_list)}")
        print(f"Current Total: Rs. {total:.2f}")


def remove_item(shopping_list, prices, quantities):
    if len(shopping_list) == 0:
        print("Your shopping list is empty.")
    else:
        view_list(shopping_list, prices, quantities)

        try:
            number = int(input("Enter the item number to remove: "))

            if 1 <= number <= len(shopping_list):
                removed = shopping_list.pop(number - 1)
                prices.pop(number - 1)
                quantities.pop(number - 1)

                print(f"{removed} has been removed.")
            else:
                print("Invalid item number.")

        except ValueError:
            print("Please enter a valid number.")


def clear_list(shopping_list, prices, quantities):
    shopping_list.clear()
    prices.clear()
    quantities.clear()

    print("Your shopping list has been cleared.")


shopping_list = []
prices = []
quantities = []

print("Welcome to your Shopping List!")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_item(shopping_list, prices, quantities)

    elif choice == "2":
        view_list(shopping_list, prices, quantities)

    elif choice == "3":
        remove_item(shopping_list, prices, quantities)

    elif choice == "4":
        clear_list(shopping_list, prices, quantities)

    elif choice == "5":

        print("\n========== SHOPPING RECEIPT ==========")
        print(f"{'Item':<15}{'Qty':<8}{'Price':<12}{'Subtotal'}")
        print("-" * 50)

        total_cost = 0

        for item, price, quantity in zip(shopping_list, prices, quantities):
            subtotal = price * quantity
            total_cost += subtotal

            print(f"{item:<15}{quantity:<8}{price:<12.2f}{subtotal:.2f}")

        print("-" * 50)
        print(f"Total Items : {len(shopping_list)}")
        print(f"Grand Total : Rs. {total_cost:.2f}")
        print("=" * 50)

        amount_paid = 0

        while amount_paid < total_cost:

            try:
                payment = float(input("Enter payment: Rs. "))

                if payment <= 0:
                    print("Payment must be greater than zero.")
                    continue

                amount_paid += payment

                if amount_paid < total_cost:
                    remaining = total_cost - amount_paid
                    print(f"Remaining Amount: Rs. {remaining:.2f}")

                elif amount_paid == total_cost:
                    print("Payment received successfully!")
                    print("Thank you for shopping!")

                else:
                    change = amount_paid - total_cost
                    print("Payment received successfully!")
                    print(f"Change: Rs. {change:.2f}")
                    print("Thank you for shopping!")

            except ValueError:
                print("Please enter a valid amount.")

        break

    else:
        print("Invalid option. Please choose 1, 2, 3, 4, or 5.")




#_______________________________________That's all for now_____________________________________