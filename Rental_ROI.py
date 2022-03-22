class Itemtype:                      # store all items in a class 
    id_counter = 0

    def __init__(self, type, value):
        self.id = Itemtype.id_counter
        self.id_counter += 1
        self.type = type
        self.value = value

    def __str__(self):
        formatted_item = (f"{self.type}: {self.value}")
        return formatted_item

    def __repr__(self):
        formated_repr = (f"< Item {self.type} | {self.value}")
        return formated_repr

class Income:                  # Income class to calculate income
    def __init__(self):
        self.total_income = 0
        self.income_items = []

    def get_values(self):
        for item in self.income_items:
            self.total_income += item.value

    def get_income(self):
        # Rental income
        rental_prompt = float(input("What is the rental income? "))
        rental_income = Itemtype("Rental income", rental_prompt)
        self.income_items.append(rental_income)
        # Laundry or storage: 
        laundry_or_storage = input("Do you have any laundry or storage income? (y/n) ")
        while laundry_or_storage not in {'y', 'n'}:
            laundry_or_storage = input("Sorry we missed that... Do you have any laundry or storage income? (y/n) ")
        if laundry_or_storage.lower() == "y":
            # Laundry 
            laundry_prompt = float(input("What is the laundry income? (Enter 0 if none) "))
            laundry_income = Itemtype("Laundry income", laundry_prompt)
            self.income_items.append(laundry_income)
            # Storage 
            storage_prompt = float(input("What is the storage income? (Enter 0 if none) "))
            storage_income = Itemtype("Storage income", storage_prompt)
            self.income_items.append(storage_income)
        else:
            print("Awesome! Let's move on to miscellaneous") 
        misc_check = input("Do you have any miscellaneous income? (y/n) ")
        while misc_check not in {'y', 'n'}:
            misc_check = input("Sorry we missed that... Do you have any miscellaneous income? (y/n)")
        if misc_check.lower() == 'y':
            misc_prompt = float(input("What is the miscellaneous income? "))
            misc_income = Itemtype("Misc incomee", misc_prompt)
            self.income_items.append(misc_income)
        else:
            print("Sounds good!")

    def print_total_income(self):
        print(f"The total monthly rental income is ${self.total_income}")

    def print_income_items(self):
        for item in self.income_items:
            print(f"{item.type}: {item.value}")

    # add item ID to check like post


class Expenses:                  # expense class to calculate expenses
    def __init__(self):
        self.total_expenses = 0
        self.expense_items = []
    
    def get_values(self):
        for item in self.expense_items:
            self.total_expenses += item.value

    def get_expenses(self):
        tax_prompt = float(input("What are the taxes on the property? "))
        tax_expense = Itemtype("Taxes", tax_prompt)
        self.expense_items.append(tax_expense)

        insurance_prompt = float(input("What is the insurance cost? "))
        insurance_expense = Itemtype("Insurance Expense", insurance_prompt)
        self.expense_items.append(insurance_expense)


        water_sewer_garbage = input("Do you have water, sewer, or garage expenses? (y/n) ")
        while water_sewer_garbage not in {'y', 'n'}:
             water_sewer_garbage = input(" Please enter again. Do you have water, sewer, or garbage expenses? (y/n) ")
        if water_sewer_garbage == 'y':
            water_prompt = float(input("What are the water expenses? Enter 0 if none "))
            water_expense = Itemtype("Water Expense", water_prompt)
            self.expense_items.append(water_expense)

            sewer_prompt = float(input("What are the sewer expenses? Enter 0 if none "))
            sewer_expense = Itemtype("Sewer Expense", sewer_prompt)
            self.expense_items.append(sewer_expense)

            garbage_prompt = float(input("What are the garbage expenses? Enter 0 if none "))
            garbage_expense = Itemtype("Garbage Expense", garbage_prompt)
            self.expense_items.append(garbage_expense)

        else:
            print("Great!")

        electric_gas = input("Do you have electric or gas expenses? (y/n) ")
        while electric_gas not in {'y', 'n'}:
             electric_gas = input(" Please enter again. Do you have electric or gas expenses? (y/n) ")
        if electric_gas == 'y':
            electric_prompt = float(input("What are the electric expenses? Enter 0 if none "))
            electric_expense = Itemtype("Electric Expense", electric_prompt)
            self.expense_items.append(electric_expense)

            gas_prompt = float(input("What are the gas expenses? Enter 0 if none"))
            gas_expense = Itemtype("Gas Expense", gas_prompt)
            self.expense_items.append(gas_expense)

        hoa_lawn_snow = input("Do you have HOE fees, or lawn and snow expenses? (y/n) ")
        while hoa_lawn_snow not in {'y', 'n'}:
             hoa_lawn_snow = input(" Please enter again. Do you have HOE fees, or lawn and snow expenses? (y/n) ")
        if hoa_lawn_snow == 'y':
            hoa_prompt = float(input("What are the HOA fees? Enter 0 if none "))
            hoa_expense = Itemtype("HOA Expense", hoa_prompt)
            self.expense_items.append(hoa_expense)

            lawn_prompt = float(input("What are the lawn expenses? Enter 0 if none"))
            lawn_expense = Itemtype("Lawn Expense", lawn_prompt)
            self.expense_items.append(lawn_expense)

            snow_prompt = float(input("What are the snow expenses? Enter 0 if none"))
            snow_expense = Itemtype("Snow Expense", snow_prompt)
            self.expense_items.append(snow_expense)

        vacancy_prompt = float(input("What is the vancancy expense? "))
        vacancy_expense = Itemtype("Vacancy Expense", vacancy_prompt)
        self.expense_items.append(vacancy_expense)

        capex_prompt = float(input("What is the CapEx expense? "))
        capex_expense = Itemtype("CapEx Expense", capex_prompt)
        self.expense_items.append(capex_expense)

        prop_m_prompt = float(input("What is the Property Management expense? "))
        prop_management_expense = Itemtype("Property Management Expense", prop_m_prompt)
        self.expense_items.append(prop_management_expense)

        mortgage_prompt = float(input("What is the Mortgage expense? "))
        mortgage_expense = Itemtype("Mortgage Expense", mortgage_prompt)
        self.expense_items.append(mortgage_expense)
        

    def print_total_expenses(self):
        print(f"The total monthly rental expenses are ${self.total_expenses}")

    def print_expense_items(self):
        for items in self.expense_items:
            print(f"{items.type}: {items.value}")

class Cash_Return():
    def __init__(self, total_income, total_expenses):
        self.total_income = total_income      # from income class
        self.total_expenses = total_expenses  # from expense class 
        self.total_monthly_cashflow = 0
        self.total_annual_cashflow = 0
        self.total_investment = 0
        self.cash_on_cash_return = 0
        self.cash_return_list = []

# Cashflow values from classes Income and Expense 
    def get_total_monthly_cashflow(self): # Separate from annual cashflow (flexibility in the future)
        self.total_monthly_cashflow += self.total_income
        self.total_monthly_cashflow -= self.total_expenses 

    def get_total_annual_cashflow(self):
        self.total_annual_cashflow = self.total_monthly_cashflow * 12

# Total investment prompts and adding item values to total_investments 
    def get_total_investment_value(self):
        for item in self.cash_return_list:
            self.total_investment += item.value

    def get_total_investment(self):
        down_payment_prompt = int(input("What is the down payment? "))
        down_payment = Itemtype("Down payment", down_payment_prompt)
        self.cash_return_list.append(down_payment)

        closing_prompt = int(input("What are the closing costs? "))
        closing_cost = Itemtype("Closing Cost", closing_prompt)
        self.cash_return_list.append(closing_cost)

        rehab_prompt = int(input("What is the cost of rehab? "))
        rehab_cost = Itemtype("Rehab Cost", rehab_prompt)
        self.cash_return_list.append(rehab_cost)

        misc_cost_prompt = int(input("What is the down payment? "))
        misc_cost = Itemtype("Misc Cost", misc_cost_prompt)
        self.cash_return_list.append(misc_cost)


# cash on cash return: annnual cash flow / total investment = x / x100
    def get_cash_on_cash_return(self):
        self.cash_on_cash_return = (self.total_annual_cashflow/self.total_investment) * 100
        # print(f"Cash on cash ROI = {self.cash_on_cash_return}%")

# print statements 
    def print_investment_total(self):
        for item in self.cash_return_list:
            print(f"{item.type}: {item.value}")
    
    def print_total(self):
        print(f"""
        Thank you for using my ROI calculator! 
        - - - - - - - - - - - - - - - - - - - - 
        Total Income: {self.total_income}
        Total Expenses: {self.total_expenses}
        -       -       -       -       -       -  
        Total Annual Cashflow: {self.total_annual_cashflow}
        Total Investment: {self.total_investment}
         -       -       -       -       -       - 
        
        The Total Cash on Cash Return on Investment is: {self.cash_on_cash_return}%
        """)

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
    income.print_total_income()
    print("Let's move onto expenses")

    # Get expenses from the user, save the item.value to total_expenses and print total income for the user
    expense.get_expenses()
    expense.get_values()
    expense.print_total_expenses()

    # Now to calculate the final values 
    cashed = Cash_Return(income.total_income, expense.total_expenses)

    # Calculating total annual cashflow 
    cashed.get_total_monthly_cashflow()
    cashed.get_total_annual_cashflow()

    # Calcuating total investment
    cashed.get_total_investment()
    cashed.get_total_investment_value()

    # Final number
    # Print out reciept 
    cashed.get_cash_on_cash_return()
    cashed.print_total()

    # ask if they want to check their income 
    double_check = input ("Something doesn't look right? \nEnter 'check' to view income or expenses OR 'q' to quit ").lower()
    while double_check not in {'check', 'q', 'quit'}:
        double_check = input ("Sorry we missed that... \nEnter 'check' to view income or expenses OR 'q' to quit ")
    
# ? Connect the items to id, display for user, and allow the user to select which one they would like to edit
    if double_check == 'check':
        income_expense_investment = input("What would you like to check? 1. Income 2.Expenses or 3. Total Investment ")
        while income_expense_investment not in {'1', '2', '3'}:
            income_expense_investment = input("Not a valid input \nWhat would you like to check? 1. Income 2.Expenses or 3. Total Investment")
        if income_expense_investment == '1':
            income.print_income_items()
        elif income_expense_investment == '2':
            expense.print_expense_items()
        elif income_expense_investment == '3':
            cashed.print_investment_total()
    else:
        print("Thank you! See you next time ")

    # Would like to eventually add it where they can save the property info to compare later 
    # Need to make sure the list wouldn't reset every time I run the program 

main()