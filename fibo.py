def fibonacci(x):
	if(x==1):
		return 1
	else:
		return fibonacci(x-1)+fibonacci(x-2)

print('--Fibonacci Number Generator--')
num=int(input('Enter the number of elements to generate:'))
print(fibonacci(num))