import sys
x=10
for i in range(0,6):
	for j in range(0,i):
		sys.stdout.write('*')
		x+=1
	print('')
'''if x>=10:  #not required
	exit()'''