class Store:
    def _init_(self):
        self.items = {
            "apple": 0.5,
            "banana": 0.3,
            "chocolate": 2.0,
            "water": 1.0,
        }
        self.cart = {}
        self.total = 0.0

    def show_menu(self):
        print("\n---- Available Items ----")
        for item, price in self.items.items():
            print(f"{item.capitalize()}: ${price:.2f}")
        print("------------------------")

    def run(self):
        while True:
            print("\n=== Store App ===")
            print("1. Buy Item")
            print("2. View Cart")
            print("3. Remove from Cart")
            print("4. Make Purchase")
            print("5. About Us")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.show_menu()
                item = input("Enter the item name: ").lower()
                quantity = int(input("Enter the quantity: "))
                if item in self.items and quantity > 0:
                    if item in self.cart:
                        self.cart[item] += quantity
                    else:
                        self.cart[item] = quantity
                    self.total += self.items[item] * quantity
                    print(f"{quantity} {item.capitalize()} added to cart.")
                else:
                    print("Invalid item or quantity. Please try again.")

            elif choice == "2":
                if not self.cart:
                    print("Your cart is empty.")
                else:
                    print("\n---- Your Cart ----")
                    for item, quantity in self.cart.items():
                        print(f"{item.capitalize()}: {quantity}")
                    print("------------------")
                    print(f"Total: ${self.total:.2f}")

            elif choice == "3":
                if not self.cart:
                    print("Your cart is empty.")
                else:
                    self.show_menu()
                    item = input("Enter the item name to remove: ").lower()
                    quantity = int(input("Enter the quantity to remove: "))
                    if item in self.cart and quantity > 0:
                        if quantity >= self.cart[item]:
                            self.total -= self.items[item] * self.cart[item]
                            del self.cart[item]
                        else:
                            self.cart[item] -= quantity
                            self.total -= self.items[item] * quantity
                        print(f"{quantity} {item.capitalize()} removed from cart.")
                    else:
                        print("Item not found in the cart or invalid quantity. Please try again.")

            elif choice == "4":
                if not self.cart:
                    print("Your cart is empty. Add items before making a purchase.")
                else:
                    print("Purchase successful! Thank you for shopping with us.")
                    self.cart.clear()
                    self.total = 0.0

            elif choice == "5":
                print("\n---- About Us ----")
                print("Welcome to our store!")
                print("We offer a variety of products for your needs.")
                print("Happy shopping!")
                print("------------------")

            elif choice == "6":
                print("Exiting the app. Thank you for visiting!")
                break

            else:
                print("Invalid choice. Please try again.")


if _name_ == "_main_":
    store = Store()
    store.run()