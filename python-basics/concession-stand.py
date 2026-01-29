# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "fries": 2.30,
        "popcorn": 4.50,
        "chips": 1.99,
        "soda": 2.00,
        "lemonade": 3.50,
        "coke": 4.00}

cart = []
total = 0
print("-------Menu------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----------------")
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is ${total:.2f}")


