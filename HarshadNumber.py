number=int(input("Enter the Number to check wheather it is Harshad or NOT:"))
temp=number
ar=[]
while temp!=0:
    digit=temp%10
    ar.append(digit)
    temp=temp//10
    
sum1=sum(ar)
if number%sum(ar)==0:
    print("The Number is Harshad Number")
else:
    print("The Number is Not a Harshad Number")
print(ar)    
