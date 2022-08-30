# income:

# rental income ** Main source = $2,000/mth
# laundry income
# total_mth_income = 2,000

# Expenses:

# Taxes - 150
# Insurance - 100
# Utilities - 0
# 	Electric
# 	water
# 	sewer
# 	gas
# HOA - 0
# Lawncare/Snow - 0
# Vacancy - 100
# repairs - 100
# Capex - 100
# Property Managment - 200
# Mortgage - 860

# Total_expenses = 1610

# Cash_Flow:

# Cash_Flow = income - Expenses
# 390 = 2000 - 1610

# ROI:

# Down_Payment: 40,000
# Closing_Costs: 3,000
# Rehab_Budget: 7,000
# Misc_other: 0

# Total_investment == 50,000


# Annual_Cash_Flow = 4,680 / Total_investment == 50,000 == 9.36%

# cash on Cash ROI == 9.36% 

from cProfile import run
from http.client import CannotSendHeader
from multiprocessing.pool import RUN


class bigger_pockets():


    def __init__(self, rental_income, expenses, cash_flow, ROI):
        self.rental_income = rental_income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.ROI = ROI
        
    def rental_income(self):
        self.rental_income = input("What is the monthly rental income for the property? ")
        
    def expenses(self, taxes, insurance, repairs, capex, prop_man, mortgage):
        self.taxes = input("what is the monthly taxes for the property?: ")
        self.insurance = input(" What is the monthly isurance for this property?: ")
        self.repairs = input(" How much are you saving for repairs monthly?: ")
        self.capex = input(" How much are you saving for CapEx monthly?: ")
        self.prop_man = input(" How much does your property manager cost monthly?: ")
        self.mortgage = input(" How much are you spedning on the mortgage monthly? ")
        self.expenses = taxes + insurance + repairs + capex + prop_man + mortgage
        
    def cash_flow(self):
        self.cash_flow = self.rental_income - self.expenses 
        
    def ROI(self, annual_cash_flow, total_investment):
        self.annual_cash_flow = self.annual_cash_flow  * 12
        self.total_investment = input("How much total investment did you spend on this property?: ")
        self.ROI = (self.annual_cash_flow/self.total_investment) * 100

        print("The cash on cash ROI is \n")
        print(self.ROI + '%')

my_rental_property = bigger_pockets([], [], [], [])          
            
def run():
    while True:
        response =  input('What data would you like to input? quit/income/expenses/cash flow or ROI ')
        if response.lower() == 'quit':
            my_rental_property.bigger_pockets()
            print("Day is over")
            break
        elif response.lower() == 'income':
            my_rental_property.rental_income()
        elif response.lower() == 'expenses':
            my_rental_property.expenses()
        elif response.lower() == 'cash flow':
            my_rental_property.cash_flow()
        elif response.lower() == 'ROI':
            my_rental_property.ROI()
        else:
            print("Choose one of the correct commands ")

            
run()




