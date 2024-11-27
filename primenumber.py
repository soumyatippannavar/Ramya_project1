num = int(input("enter number"))
for i in range(2, num):
    if (num % i) == 0:
        print(num, "is not a prime number")
        break

else:
    print(num, "is a prime number")

x=2
y=8
prime_list = []
for i in range(x, y):
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

print(prime_list)

for i in range(6,0,-1):
    print(i)
