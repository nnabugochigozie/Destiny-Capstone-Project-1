from datetime import date
today = date.today()        #To import the current date.

from pathlib import Path
file = Path(__file__).parent / "expenses.csv"   # For better access to the csv file.

def updatefile(amount, description): # Create and update a CSV file
     with open(file, "a") as f:
         f.write(f"{today}, {type}, {category}, {amount: .2f}, {description}\n")


currentBalance = 0          # Initialize the balance to be empty since the program is not yet in use.
list_of_expense_description = []    # List of expenses spent on.
list_of_expense_amount = []         # List of expenses spent.
list_of_income_description = []     # List of income areas.
list_of_income_amount = []          # List of income gained.

print("=== Personal Expense Tracker ===")
print("1. Add expense  2. Add income  3. View balance  4. Summary by category  5. Exit")

# TO LOOP THE LIST UNTIL THE USER PICKS OPTION FIVE (EXIT).
condition = False
while condition == False:
    try: # To avoid errors from invalid input data type
        print(" ")
        option = int(input("Choose an option: "))

    # TO ADD EXPENSES
        if option == 1:
            print(f"Date (YYYY-MM-DD): {today}")
            type = "Expense"
            category = input("Category (transport/food/data/rent/other): ")
            expense_amount = int(input("Amount (NGN): "))
            # Condition to check if amount is greater than balance.
            if expense_amount > currentBalance:
                print("You do not have enough to spend")
            elif expense_amount < 0:
                print("Amount must be positive")
            else:
                list_of_expense_amount.append(expense_amount) # To add to the expense amount list
                currentBalance -= expense_amount
                expense_description = input("Description: ")
                list_of_expense_description.append(category)  # To add to the expense description list
                updatefile(expense_amount, expense_description)
                print(f"Expense saved. Current balance: NGN {currentBalance: ,.2f}")

    # TO ADD INCOME
        elif option == 2:
            print(f"Date (YYYY-MM-DD): {today}")
            type = "Income"
            category = input("Category (salary/gift/allowance/other): ")
            income_amount = int(input("Amount (NGN): "))
            if income_amount < 0:
                print("Amount must be positive")
            else:
                list_of_income_amount.append(income_amount) # To add to the income amount list
                currentBalance += income_amount
                income_description = input("Description: ")
                list_of_income_description.append(category) # To add to the income description list
                updatefile(income_amount, income_description)
                print(f"Income saved. Current balance: NGN {currentBalance: ,.2f}")
                

    # TO VIEW BALANCE
        elif option == 3:
            print(f"Your current balance is: NGN{currentBalance: ,.2f}")

    # SUMMARY BY CATEGORY
        elif option == 4:
            # In the case of no prior expense definition

            print("-- Summary by Category --")
            for expense, amount in zip(list_of_expense_description, list_of_expense_amount):
                print(f"Expenses: {expense} - NGN {amount:,.2f}")
            for income, amount in zip(list_of_income_description, list_of_income_amount):
                print(f"Income: {income} - NGN {amount:,.2f}")
            print("-------------------------")
        
    # TO TERMINATE PROGRAM
        elif option == 5:
            print("Goodbye! Data saved to expenses.csv")
            condition = True

    # TO HANDLE INVALID OPTION INPUT
        else:
            print("Input must be an integer between 1 to 5")
    except ValueError: # Value error is for invalid input types.
        print("Ooops, that's not a number.")