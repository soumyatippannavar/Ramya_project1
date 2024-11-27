def isPalindrome(s):
    revers = s[::-1]
    return revers

s = "malayalam"
ans = isPalindrome(s)

if ans == s:
    print("Yes")
else:
    print("No")

def pal():
    str = "maling"
    print(str[::-1])
    print(''.join(reversed(str)))
    print(str.join("BC"))
pal()

def reverse():
    s="RAMYA"
    p=''
    for i in range(len(s)-1,-1,-1):
        p=p+s[i]
    print(p)
reverse()


def eve():
   list=[2,5,1,10,6,12]
   max=list[0]
   for i in list:
       if i>max:
           max=i
   return max

print("max vaue:",eve())

for i in range(2,3):
    print(i)

def printNos(n):
    if n <= 10:
        printNos(n + 1)
        print(n, end=' ')
# Driver code
n = 1
printNos(n)