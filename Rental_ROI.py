# Welcome to the ROI calculator
class Itemtype:                      # store all items in a class 
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Income:                  # Income class to calculate income
    def __init__(self):
        self.total_income = 0
        self.income_items = []

    def get_values(self):
        for item in self.income_items:
            self.total_income += item.value
        print(f"The total value is {self.total_income}")


    def get_income(self):
        rental_prompt = int(input("What is the rental income? "))
        rental_income = Itemtype("Rental income", rental_prompt)
        self.income_items.append(rental_income)

    # laundry, storage, misc
        laundry = 0
        storage = 0 
        misc = 0

    def print_total_income(self):
        print(f"The total monthly rental income is ${self.total_income}")


class Expenses:                  # expense class to calculate expenses
    def __init__(self):
        self.total_expenses = 0
        self.expense_items = []
    
    def get_values(self):
        for item in self.expense_items:
            self.total_expenses += item.value
        print(f"The total value is {self.total_expenses}")

    def get_expenses(self):
        tax_prompt = int(input("What are the taxes? "))
        tax_expense = Itemtype("Taxes", tax_prompt)
        self.expense_items.append(tax_expense)
    # vars taxes, insurance, water_sewer, garbage, electric, gas, hoa_fees, lawn_snow, vacancy, repairs, capex, prop_management, mortage


class Cash_Return():
    def __init__(self, total_income, total_expenses):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.total_monthly_cashflow = 0
        self.total_annual_cashflow = 0
        self.total_investment = 0
        self.cash_on_cash_return = 0
        self.cash_return_list = []

    def get_total_monthly_cashflow(self):
        self.total_monthly_cashflow += self.total_income
        self.total_monthly_cashflow -= self.total_expenses 
        print(f"The total monthly cashflow is {self.total_monthly_cashflow}")

    def get_total_annual_cashflow(self):
        self.total_annual_cashflow = self.total_monthly_cashflow * 12
        print(f"The total annual cashflow is {self.total_annual_cashflow}")

    def get_total_investment_value(self):
        for item in self.cash_return_list:
            self.total_investment += item.value
        print(f"The total investment is {self.total_investment}")

    def get_total_investment(self):
        down_payment_prompt = int(input("What is the down payment? "))
        down_payment = Itemtype("Down payment", down_payment_prompt)
        self.cash_return_list.append(down_payment)

    # vars: closing_costs, rehab_budget, misc_other

    # cash on cash return: FINAL NUMBER
    # annnual cash flow / total investment = x / x100
    def get_cash_on_cash_return(self):
        self.cash_on_cash_return = (self.total_annual_cashflow/self.total_investment)
        print(f"Cash on cash ROI = {self.cash_on_cash_return}")

# * * * * * * * * * * * * * * * * *
def main():
    # Welcome the user
    print("""
    Welcome to the ROI calculator! 
    Today we will be calcuating the return on investment for a property!
    We will ask for the following values in terms of dollar ($) amount per month
    """)

    # Initialize classes 
    income = Income()
    expense = Expenses()

    # Get income from the user, save the item.value to total_income and print total income for the user
    income.get_income()
    income.get_values()

    # Get expenses from the user, save the item.value to total_expenses and print total income for the user
    expense.get_expenses()
    expense.get_values()

    # Now to calculate the final values 
    cashed = Cash_Return(income.total_income, expense.total_expenses)

    # Calculating total annual cashflow 
    cashed.get_total_monthly_cashflow()
    cashed.get_total_annual_cashflow()

    # Calcuating total investment
    cashed.get_total_investment()
    cashed.get_total_investment_value()

    # Final number
    cashed.get_cash_on_cash_return()



main()