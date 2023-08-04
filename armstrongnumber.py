number=int(input("Enter Number:"))
temp=number
temppp=number
kk=0
counter=0

while temppp>0:
    digit=temppp % 10
 
    temppp=temppp//10
    counter+=1



while temp>0:
    digit=temp % 10
    kk+=digit**counter
    temp=temp//10
    
print(kk)
    
