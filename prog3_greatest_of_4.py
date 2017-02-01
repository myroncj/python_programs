num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
num4 = int(input("Enter Fourth Number: "))

if (num1 > num2) and (num1 > num3) and (num1 > num4):
   largest = num1
elif (num2 > num1) and (num2 > num3) and (num2 > num4):
   largest = num2
elif (num3 > num1) and (num3 > num2) and (num3 > num4):
   largest = num3
else:
   largest = num4

print("The largest number between",num1,",",num2,",",num3, "and",num4,"is",largest)