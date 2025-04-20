# 🚲 Bike Rental System 🚴‍♂️

Welcome to the **Bike Rental System**! This is a simple command-line application where users can check the available bikes in stock, rent bikes, or return them.

---

## 📝 Overview

The **Bike Rental System** simulates the process of renting bikes from a bike shop. The system:

- Displays the number of available bikes in the shop.
- Allows users to rent bikes (costs 100 Rs per bike).
- Allows users to return bikes to the shop.
- Tracks the remaining stock of bikes after each transaction.

---

## ⚙️ Features

- **Display Available Bikes**: View how many bikes are available for rent.
- **Rent a Bike**: Rent bikes at 100 Rs per bike.
- **Return a Bike**: Return bikes to the shop and update the stock.
- **Exit**: Exit the system.

---

## 💻 How to Run

1. Clone or download the repository to your local machine.
2. Run the Python script `bike_rental_system.py` in your terminal.
   - Ensure you have **Python** installed on your machine.
3. Follow the on-screen instructions to interact with the system.

---

## 🖥️ Code Explanation

### Classes

#### `BikeShop`
- **Attributes**:
  - `stock`: Tracks the number of bikes available in the shop.
- **Methods**:
  - `display_bike()`: Displays the current number of bikes available for rent.
  - `rent_bike(qty)`: Handles the bike rental process, updating stock and calculating total cost.
  - `return_bike(qty)`: Updates the bike stock when bikes are returned.

### Main Program
- Prompts the user to select an option from the menu and handles their input.
- Interacts with the `BikeShop` class to rent and return bikes.

---

## 🚀 Future Enhancements

- Add user authentication to track rentals and returns.
- Store rental history (e.g., bikes rented and returned by the user).
- Implement a maximum rental limit per user.

---

## 🔄 License

This project is open-source and available under the **MIT License**.

---

## 🧑‍💻 Made with ❤️ by Anshi Agarwal

Feel free to use and modify this project for your own learning or personal use. Enjoy renting bikes! 😄
