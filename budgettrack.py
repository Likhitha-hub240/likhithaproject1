# budget_tracker.py
# Author: Likhitha JS

print("💰 Simple Budget Tracker 💰")
print("-----------------------------")

income = float(input("Enter total income: ₹"))
expense1 = float(input("Enter first expense: ₹"))
expense2 = float(input("Enter second expense: ₹"))
expense3 = float(input("Enter third expense: ₹"))

total_expense = expense1 + expense2 + expense3
balance = income - total_expense

print("\n----- Budget Summary -----")
print(f"Total Income: ₹{income}")
print(f"Total Expenses: ₹{total_expense}")
print(f"Remaining Balance: ₹{balance}")

if balance > 0:
    print("✅ You are within budget!")
else:
    print("⚠️ You have exceeded your budget!")
