# Personal Expense Calculator

name = input("Enter your name: ")
Monthly_income  = int(input("Enter your Monthly income : "))
Rent = int(input("Enter your Rent: "))
Food_expenses = int(input("Enter your Food expenses: "))
Travel_expenses = int(input("Enter your Travel expenses: "))
Entertainment_expenses = int(input("Enter your Entertainment expenses: "))
Other_expenses = int(input("Enter your Other expenses: "))
Total_expenses = Rent + Food_expenses + Travel_expenses + Entertainment_expenses + Other_expenses 
Remaining_money = Monthly_income - Total_expenses
Saving_percentage = (Remaining_money/Monthly_income)*100

print("===== MONTHLY EXPENSE REPORT ===== ")
print("Name:",name)
print("Monthly Income:",Monthly_income)
print(f"Total expenses: ₹{Total_expenses}")
print(f"Remaining money: ₹{Remaining_money}")
print(f"Saving percentage: {Saving_percentage}%")