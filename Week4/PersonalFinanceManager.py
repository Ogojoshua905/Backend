class Personal:
    income = 0 #class Atrribute
    expenses = {}
    welcome = "Welcome! This is just a server-side finance monitor. Hope you continue using our product after releasing it globally."

    def __init__(self, savings):
        self.savings = savings #instance Methods

    def update_expenses(self, e_name, amount): #Instance Method: Method that has self attached to it. 
        self.expenses[e_name] = amount

    def update_income(self, income):
        self.income += int(income)

    def view_finance_monitor(self):
        total_expenses = sum(self.expenses.values())
        result = self.income - total_expenses
        
        if result < 0:
            print("You are a very bad spender. Try to get Street orientation.")
            for e_name, amount in self.expenses.items():
                print("==" * 8)
                print(f"Expense name: {e_name}")
                print(f"Amount: ${amount}")
                print("==" * 8)
        else:
            print("Congratulations! You are Considerate even in This Tinubu Regime.")
            print(f"Total Income: ${self.income}")
            print(f"Total Expenses: ${total_expenses}")
            print(f"Remaining Balance: ${result}")

    def store_income(self):
        income = int(input("What's your income for the month: $"))
        self.update_income(income)
        
        while True:
            command = input("Enter your expense name or 'done' if you are finished: ")
            
            if command != "done":
                e_name = command
                amount = int(input("Enter your expense amount: $"))
                self.update_expenses(e_name, amount)
                print(f"Thanks for using our software. Your expense '{e_name}' of ${amount} has been recorded.")
            elif command == 'done':
                self.view_finance_monitor()
                break
            else:
                print("Invalid command. Please try again.")

pfm = Personal(savings=0)
print(pfm.welcome)
print(pfm.store_income())
