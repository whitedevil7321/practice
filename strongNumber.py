number=int(input("Enter The Number to check for the strong number:"))
ar=[]
n=0
def fact(n):
    sum1=1
    for i in range(1,n+1):
        sum1=sum1*i
    return sum1    
for i in range(1,number+1):
    ar.append(fact(i))
print(ar)

sum2=0
for i in range(len(ar)):
    sum2=sum2+ar[i]
    
if(sum2==number):
    print("Number is storng number")
else:
    print("Number not is storng number")
