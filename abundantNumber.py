number=int(input("Enter the Number to check wheather it is Abundant or NOT:"))

k=[]

for i in range(1,number):
    if number%i==0:
        k.append(i)
        
if sum(k)>number:
    print("The Number is Abundant Number")
else:
    print("The Number is Not a Abundant Number")
print(k)        
