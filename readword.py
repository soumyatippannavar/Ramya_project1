with open('Reading.txt','r') as file:
	# reading each line
	for line in file:
		print(line)

		# reading each word
		for word in line.split(" "):

			# displaying the words
			print(word)
#print("------")

#file = open('Reading.txt','r')
#for i in file:   #read mode
  #print(file.readline(i))

#file1 = open("writing.txt",'w')  #write mode
#for i in file:
	#file1.write(i)
#file1.write("\nhello")
#print(file1.read(5))

#print(file1.read())
#print(file1.readline())
#os.remove("Reading.txt")

l1 = [7, 3, 1, 2, 9, 0, 6, 4, 5]

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] <= l1[j]:
            # temporary variable
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
print("Sorted List", l1)
print(l1[-2])

list=["asbd","adadda","abc"]
emp=[]
dic={}
for i in list:
    dic[i]=len(i)
    emp.append(len(i))
else:
    #print(list)
    print(dic)
    print("index at value",emp.index(max(emp)))
count=0
with open('Reading.txt','r') as file:
    print(file.readlines())
