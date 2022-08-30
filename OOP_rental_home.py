
class biggerPockets():

	def __init__(self, income, expenses, cash_flow, ROI, total_investment):
		self.income = income
		self.expenses = expenses
		self.cash_flow = cash_flow
		self.ROI = ROI
		self.total_investment = total_investment
		
	def cashFlow(self, cash_flow):
		cash_flow == self.income - self.expenses
		return cash_flow
		
	def ROI(self, ROI, total_investment, cash_flow):
		ROI = (total_investment/(cash_flow*12)) * 100
		return ROI 
			
	def good_investment(self,ROI):
		if ROI > 0:
			print("This is probably a good investment")
		


hamilton_property = biggerPockets(2000, 1390, total_investment=50000, cash_flow="", ROI="", )
beverly_property = biggerPockets(4000, 3200, total_investment=100000, cash_flow="", ROI="")
