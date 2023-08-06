number1=int(input("Enter the number 1:"))
number2=int(input("Enter the number 2:"))
k=[]

for i in range(1,number1):
    if number1%i==0:
        k.append(i)
        
if sum(k)>number1:
    print("The number1 is Abundant number1")
else:
    print("The number1 is Not a Abundant number1")
print(k)        



j=[]

for i in range(1,number2):
    if number2%i==0:
        j.append(i)
        
if sum(j)>number1:
    print("The number2 is Abundant number1")
else:
    print("The number2 is Not a Abundant number1")
print(j)



if number1%sum(k)==number2%sum(j):
    print("Friendly Pair")
else:
    print("Not a friendly pair")
