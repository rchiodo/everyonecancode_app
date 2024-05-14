todo_list = []

while True:
    print()
    print()
    print("To-do list:")
    item_number = 0
    for todo in todo_list:
        print(f"{item_number} - {todo}")
        item_number += 1 
    
    print()
    print("Actions:")
    print("A - Add to-do item")
    print("R - Remove to-do item")
    print("X - Exit")

    choice = input("Enter your choice (A, X, or R):")
    choice = choice.upper()

    if choice == "A":
        todo = input("Enter the to-do item: ")
        todo_list.append(todo)
        continue

    if choice == "R":
        todo = int(input("Enter the number of the to-do item to remove:"))
        todo_list.pop(todo)
        continue

    if choice == "X":
        break
    
    print("Invalid choice " + choice)
    


