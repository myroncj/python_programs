print('Enter 10 numbers:')
p=[]
for i in range(0,10):
	p.append(int(input("")))
q =[x for x in p if (x % 2 == 0)]
print('The even numbers entered are:')
for i in range(0,len(q)):
	print(int(q[i]))