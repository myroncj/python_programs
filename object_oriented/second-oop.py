'''
Create a class and create functions in it
the functions should add, subtract, divide and multiply
can be done by using parameters or without parameters
'''

class calculator:
	def __init__(self):
		self.a = int(input('Enter Num1:'))
		self.b = int(input('Enter Num2:'))

	def add(self):
		return self.a+self.b

	def sub(self):
		return self.a-self.b

	def mul(self):
		return self.a*self.b

	def div(self):
		return self.a/self.b


ob1=calculator()

while(1):
	print('\nEnter\n 1 for addition \n 2 for subtraction\n 3 for multipliocation\n 4 for division\n 5 to exit')
	ch=int(input('Enter your choice:'))	

	
	if(ch==1):
		res = ob1.add()
		print(res)
	elif(ch==2):
		res = ob1.sub()
		print(res)
	elif(ch==3):
		res = ob1.mul()
		print(res)
	elif(ch==4):
		res = ob1.div()
		print(res)
	elif(ch==5):
		exit(0)
	else:
		print('Choice is invalid!')
