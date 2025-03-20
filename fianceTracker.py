import json
from datetime import datetime

class PersonalFinanceTracker:
    def __init__(self):
        self.data = {"income": [], "expenses": [], "savings_goal": 0}
        self.load_data()
    
    def load_data(self):
        try:
            with open("finance_data.json", "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.save_data()
    
    def save_data(self):
        with open("finance_data.json", "w") as file:
            json.dump(self.data, file, indent=4)
    
    def add_income(self, source, amount):
        self.data["income"].append({"source": source, "amount": amount, "date": str(datetime.now().date())})
        self.save_data()
    
    def add_expense(self, category, amount):
        self.data["expenses"].append({"category": category, "amount": amount, "date": str(datetime.now().date())})
        self.save_data()
    
    def set_savings_goal(self, amount):
        self.data["savings_goal"] = amount
        self.save_data()
    
    def generate_report(self):
        total_income = sum(item["amount"] for item in self.data["income"])
        total_expenses = sum(item["amount"] for item in self.data["expenses"])
        savings = total_income - total_expenses
        goal_status = "Reached" if savings >= self.data["savings_goal"] else "Not Reached"
        
        report = f"""
        Personal Finance Report ({datetime.now().strftime('%B %Y')})
        -------------------------------------------------
        Total Income: ${total_income:.2f}
        Total Expenses: ${total_expenses:.2f}
        Net Savings: ${savings:.2f}
        Savings Goal: ${self.data['savings_goal']:.2f} ({goal_status})
        """
        print(report)
    
if __name__ == "__main__":
    tracker = PersonalFinanceTracker()
    tracker.add_income("Salary", 5000)
    tracker.add_expense("Rent", 1450)
    tracker.add_expense("Food", 500)
    tracker.set_savings_goal(1000)
    tracker.generate_report()