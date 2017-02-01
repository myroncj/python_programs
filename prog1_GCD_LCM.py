def hcf(i, j):
  if i > j:
    small = j
  else:
    small = i
  for x in range(1,small + 1):
    if((i % x == 0) and (j % x == 0)):
      hcf = x
  return hcf

def lcm(i, j):
  if i > j:
    large = i
  else:
    large = j
  while(True):
    if((large % i == 0) and (large % j == 0)):
      lcm = large
      break
    large += 1
  return lcm

print('1--HCF')
print('2--LCM')
ch=int(input('Enter your choice:'))
if(ch==1):
  num1=int(input('Enter the first number:'))
  num2=int(input('Enter the second number:'))
  res1=hcf(num1,num2)
  print('The Highest Common Factor of',num1,'and',num2,'is',int(res1))
elif(ch==2):
  num1=int(input('Enter the first number:'))
  num2=int(input('Enter the second number:'))
  res2=lcm(num1,num2)
  print('The Least Common Multiple of',num1,'and',num2,'is',int(res2))
else:
  print('Invalid Choice!')    