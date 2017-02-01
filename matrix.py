x=[[1,2,3,4,5],
   [6,7,8,9,10]]

print(x[0][1]) #for printing the dimension of the matrix
print(x[1][1])

for i in x:
	print(i) #print all the contents of the matrix

for i in x: #for printing the entire matrix
	for j in i:  # i in x and j in i 
		print(j)
	print(' Next Row ')
print('')
print('--Mahalo--')
print('')