with open("journal.txt", "r") as file:
    content = file.read()
    print(content)
name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {goal}\n")
print("Your goal has been saved to journal.txt")