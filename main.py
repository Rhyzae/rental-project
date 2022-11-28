# Jayson Yin
# Nov. 27th 2022

# Create a program that will calculate the Return on Investment(ROI) for a rental property


    # Income
        # Rental income = $$$ per month
        # Storage income
        # ect.

        # Total income = All income combined
    
    # Expenses
        # (Are any of these included?) ask for input
        # Tax 
        # Insurance
        # Utilities
        # HOA
        # Repairs
        # CapEx
        # Property Management
        # Mortgage

        # Gather all expenses
    
    # Cashflow
        # Income - Expenses

    # Cash-on-Cash ROI
        # Down Payment
        # Closing Costs
        # Repair Budget
        # Misc.
        
        # Total investment = All combined

        # Annual cashflow = monthly cashflow * 12
        # Cash-on-Cash ROI = Annual cashflow / Total investment (will end up as a percentage)

# Gives a list of possible income and expense sources so that they can be changed if needed at a later point
income_sources = ['rental', 'storage', 'misc.']
expense_sources = ['tax', 'insurance', 'utilities', 'HOA', 'repairs', 'property management', 'mortgage', 'misc.']
investment_sources = ['down payment', 'closing costs', 'repairs', 'misc.']

def gather_income():
    print("\nIncome:\n")
    income = 0
    for source in income_sources:
        amount = int(input(f'What will be your monthly income for "{source}" '))
        income += amount
    return income

def gather_expenses():
    print("\nExpenses:\n")
    expenses = 0
    for source in expense_sources:
        amount = int(input(f'What will be your monthly expense for "{source}" '))
        expenses += amount
    return expenses

def gather_investment():
    print("\nInitial Investment:\n")
    investment = 0
    for source in investment_sources:
        amount = int(input(f'How much did you spend on "{source}" '))
        investment += amount
    return investment

def gather_cashflow(income, expenses):
    return income - expenses



def run():
    income = gather_income()
    expenses = gather_expenses()
    cashflow = gather_cashflow(income, expenses)
    investment = gather_investment()
    house1 = ROI(income, expenses, cashflow, investment)
    print(house1.returnOnInvestment())
    house1.showInfo()

# Creating a class to gather and save the information
class ROI():
    
    def __init__(self, income, expenses, cashflow, investment):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.investment = investment
    
    def returnOnInvestment(self):
        roi = ((self.cashflow * 12) / self.investment) * 100
        roi = round(roi, 2)
        return f"\nYour return on investment is {roi}%\n"
    
    def showInfo(self):
        print("\nThis is how we calculated it:")
        print(f"\tIncome: ${self.income}")
        print(f"\tExpenses: ${self.expenses}")
        print(f"\tCashflow ({self.income} - {self.expenses}): ${self.cashflow}")
        print("\nThen on to figuring out how good the investment is:")
        print(f"\tAnnual cashflow ({self.cashflow} * 12): ${self.cashflow * 12}")
        print(f"\t\nROI = ({self.cashflow * 12}/{self.investment})%")

run()
        

    



