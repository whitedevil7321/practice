number=int(input("Enter Number:"))
ar=[]
sum1=0
for i in range(1,number):
    if number%i==0:
        ar.append(i)

for i in range(len(ar)):
    sum1=sum1+ar[i]
if(sum1==number):
    print(number,"is Perfect Number")
else:
    print(number,"is not a Perfect Number")
print("And the sum of all it's divisors is:",sum1)    
