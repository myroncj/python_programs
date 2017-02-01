#first list has 5 words

#create a second list which will map the lenghts each of the words in the firs list.

#Display the lenght of the longest word in the lsit

#Accept a  number and display all words whoz lenght is greater than that number

'''x=['I','am','in','Christ','University']
ind = 0
y=[]
for i in x:
    y[ind].append(len(x[ind]))
    ind += 1
print(y)'''

lenghts=[]

horsemen = ["war", "famine", "pestilence", "death"]

for i in range(len(horsemen)):
    lenghts.append(len(horsemen[i]))

print(lenghts)

num=int(input('Enter a number:'))

for i in range(len(lenghts)):
	if(lenghts[i]>num):
		print(horsemen[i])