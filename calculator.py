class calculator:
	
	def __init__(self,qw,qa):
		self.num1= qw
		self.num2= qa
	def add(self):
		print(self.num2+self.num1)
	def sub(self):
		print(self.num1-self.num2)
    
    
operation1 = calculator(120,13)
operation2 = calculator(130,13)
print(operation1.add())