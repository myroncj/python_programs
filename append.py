import copy

mylist=[]
listb=[]
print(mylist)
mylist.append(5) #adding new elements
mylist.append(4)
mylist.append(3)
mylist.append(2)
mylist.append(1)
print(mylist)
mylist.sort() #sorting the list
print(mylist)
#listb=mylist #copying the list
listb=copy.copy(mylist) #copy function....need to import copy ^^^
print(listb)
listb.extend([10,9,8,7,6]) #add multiple elemets at a time
listb.sort()
print(listb)
print(len(listb))#count elements in the list
listb.insert(5,10) #insert values at a position --insert(position,value)
print(listb)
print(listb.count(10)) #count the number of occurrences of an element --count(element)
lenght1=(len(set(listb))) #will count the unique elements only once
print(lenght1)
print(listb.index(10)) #to find index of the element
listb.pop(10) #pop out elements
print(listb)
'''for i in range(11):
	print(list[i].value)
'''