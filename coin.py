import json

try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"Coins": 0}
    with open("data.json", "w") as file:
        json.dump(data, file)

while True:
    print("\n1. Add coins")
    print("2. view coins")
    print("3. Quit")

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        amount = int(input("\nEnter amount: "))
        data["Coins"] += amount
        with open("data.json", "w") as file:
            json.dump(data, file)
    elif choice == 2:
        print(f"\nYou have {data['Coins']} coins.")
    elif choice == 3:
        print("Thank you for playing!")
        break