import matplotlib.pyplot as plt

def histogram(alist,m):
	blist=[]
	for i in range(0,m):
		count=0
		for j in alist:
			if(i==j):
				count+=1
		blist.append(count)
	print(blist)
	print(sum(blist))
	plt.plot(blist)
	plt.ylabel('Occurences')
	plt.xlabel('Elements')
	plt.show()

m = int(input('Enter m:'))

alist=[]
for x in range(0,m):
	n=int(input(''))
	alist.append(n)

print(alist)
histogram(alist,m)