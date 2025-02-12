# A bike rental system
# display available bikes and request a bike for rent(100 Rs->1qty) then exit

class BikeShop:
    def __init__(self, stock):
        self.stock = stock  # Initial stock of bikes

    def display_bike(self):
        """Display available bikes in stock."""
        print(f"\n🚲 Total Bikes Available: {self.stock}")

    def rent_bike(self, qty):
        """Handles bike rental process."""
        if qty <= 0:
            print("⚠️ Please enter a **positive number** greater than zero!")
        elif qty > self.stock:
            print(f"❌ Sorry! Only {self.stock} bike(s) available. Enter a lower quantity.")
        else:
            cost = qty * 100  # 100 Rs per bike
            self.stock -= qty  # Deduct bikes from stock
            print(f"\n✅ You have successfully rented {qty} bike(s).")
            print(f"💰 Total Price: **{cost} Rs**")
            print(f"📉 Bikes remaining: {self.stock}")

    def return_bike(self, qty):
        """Handles bike return process."""
        if qty <= 0:
            print("⚠️ Please enter a valid number of bikes to return!")
        else:
            self.stock += qty  # Increase bike stock
            print(f"\n🔄 You returned {qty} bike(s).")
            print(f"🚲 Updated stock: {self.stock}")

# Create a BikeShop object with 100 bikes
shop = BikeShop(100)

while True:
    try:
        user_choice = int(input('''
🚴‍♂️ **Bike Rental System** 🚴‍♀️

1️⃣ Display Available Bikes
2️⃣ Rent a Bike
3️⃣ Return a Bike
4️⃣ Exit

👉 **Enter your choice:** '''))

        if user_choice == 1:
            shop.display_bike()

        elif user_choice == 2:
            qty = int(input("🔢 **Enter the number of bikes you want to rent:** "))
            shop.rent_bike(qty)

        elif user_choice == 3:
            qty = int(input("🔄 **Enter the number of bikes you want to return:** "))
            shop.return_bike(qty)

        elif user_choice == 4:
            print("\n🙏 **Thank you for using our Bike Rental System! Have a great day! 🚀**")
            break

        else:
            print("⚠️ **Invalid choice! Please enter 1, 2, 3, or 4.**")

    except ValueError:
        print("⚠️ **Please enter a valid numeric choice!**")
