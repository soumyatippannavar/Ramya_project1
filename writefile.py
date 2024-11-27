#file = open('Reading.txt','r')
#print(file.read(2))
#while True:

    # read by character
    #char = file.read(1)
    #if not char:
        #break

    #print(char)

#file.close()

file2=open('Reading.txt','r')
count=0
#print(file2.readline())
#for i in file2:  #for counting number of  line
for i in file2.readline(2):#counting charcter in file
    #print(file2.readline())
    #print(i,end='')
     count+=1
print(count)
#print(i)

file3=open('Reading.txt','r')
while 1:

    # read by character
    char = file3.read(1)
    if not char:
        break
    print(char)