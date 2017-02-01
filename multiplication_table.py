'''
#Program with while loops
i=1
j=1
x=input('Upto What:')
y=input('Limit:')
while(j<=int(x)):
	i=1
	while(i<=int(y)):
		print(j,'\tX\t',i,'\t=\t',int(j)*int(i))
		i+=1
	j+=1
print('\n\n')
'''

#Program with for loops
x=int(input('Upto What:'))
y=int(input('Limit:'))
for i in range(1,x+1):     #Usually we start with 0 in for loop but in this case we have to use 1
	for j in range(1,y+1):
		print(i,' X ',j,' = ',i*j)
	print('')
'''	print('')
print('  /\  ')
print('_,||,,')
print(' \  /')
print('  || ')
'''