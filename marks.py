'''
x1 = input('Enter marks of subject 1:\n')
x2 = input('Enter marks of subject 2:\n')
x3 = input('Enter marks of subject 3:\n')
x4 = input('Enter marks of subject 4:\n')
x5 = input('Enter marks of subject 5:\n')

sum = (int(x1)+int(x2)+int(x3)+int(x4)+int(x5))

avg = (int(sum))/5

print('The total marks are:',sum)
print('The Average marks are:',avg)
'''

x1 = int(input('Enter marks of subject 1:\n'))
x2 = int(input('Enter marks of subject 2:\n'))
x3 = int(input('Enter marks of subject 3:\n'))
x4 = int(input('Enter marks of subject 4:\n'))
x5 = int(input('Enter marks of subject 5:\n'))

sum = (x1+x2+x3+x4+x5)

avg = (int(sum))/5

print('The total marks are:',sum)
print('The Average marks are:',avg)