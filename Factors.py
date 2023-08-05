number=int(input("Enter Number:"))
ar=[]
sum1=0
for i in range(1,number):
    if number%i==0:
        ar.append(i)
print("Factor's of a",number,"is",ar)
