class Income_Expenses:
    def __init__(self):
        self.total_income = 0
        self.total_income2 = 0
        self.income_items = []

    def get_values(self):
        for item in self.income_items:
            self.total_income2 += item.value
        print(f"The total value is {self.total_income2}")


    def get_income(self):
        rental_prompt = int(input("What is the rental income? "))
        rental_income = IncomeVal("Rental income", rental_prompt)
        self.total_income += rental_income.value
        self.income_items.append(rental_income)

    # laundry, storage, misc
        laundry = 0
        storage = 0 
        misc = 0

    def print_total_income(self):
        print(f"The total monthly rental income is ${self.total_income}")

class IncomeVal:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Expenses:
    def __init__(self):
        self.total_expenses = 0

    # vars taxes, insurance, water_sewer, garbage, electric, gas, hoa_fees, lawn_snow, vacancy, repairs, capex, prop_management, mortage
class ExpenseVal:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Cash_Return(Income_Expenses):
    def __init__(self):
        self.income_expense = Income_Expenses()
        self.total_monthly_cashflow = 0
        self.total_annual_cashflow = 0
        self.total_investment = 0
        self.cash_on_cash_return = 0

    def get_total_monthly_cashflow(self):
        self.total_monthly_cashflow += Income_Expenses.total_income
        self.total_monthly_cashflow -= self.total_expenses 
        print(f"The total monthly cashflow is {self.total_monthly_cashflow}")

    def get_total_annual_cashflow(self):
        self.total_annual_cashflow = self.total_monthly_cashflow * 12
        print(f"The total annual cashflow is {self.total_annual_cashflow}")

    def get_total_investment(self):
        self.total_investment += 0 # VAR

    # vars: down_payment, closing_costs, rehab_budget, misc_other


    # annnual cash flow / total investment = x / x100

    # cash on cash return: FINAL NUMBER

    def get_cash_on_cash_return(self):
        self.cash_on_cash_return = (self.total_annual_cashflow/self.total_investment)
        return f"Cash on cash ROI = {self.cash_on_cash_return}"


def main():
    income_expense = Income_Expenses()
    income_expense.get_income()
    income_expense.print_total_income()
    income_expense.get_values()

    # cash_return = Cash_Return()
    # cash_return.get_total_monthly_cashflow()
    total_monthly_cashflow = 0
    total_monthly_cashflow = (income_expense.total_income) * 12
    print(f'Total month cashflow is {total_monthly_cashflow}')



main()