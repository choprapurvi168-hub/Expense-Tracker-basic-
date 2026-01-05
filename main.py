expenses = []

print("Welcome ")

while True:
    print("-----MENU-----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter your choice(1-4):"))

    if choice == 1:
        date = input("Enter date (YYYY-MM-DD):")
        category = input("Enter category (eg. Food, Travel, Shopping...) : ")
        description = input("Enter description:")
        amount = input("Enter amount")
        expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount  }
        expenses.append(expense)

        print("\n Expense Added Successfully!")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded")
        else:
            print("All Expenses:")
            count = 1
            for exp in expenses:
                print(f" Expense {count} -> Date: {exp["date"]}, Category: {exp["category"]}, Description: {exp["description"]}, Amount: {exp["amount"]}")
            count += 1
            
    elif choice == 3:

        total = sum(float(exp["amount"]) for exp in expenses)
        print("Total Spending =", total)

    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break
          
    else:
        print("Invalid Choice. try again!") 
