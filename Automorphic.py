number=int(input("Enter Number:"))
temp=number
count=0
revno=""
revno1=""
while temp!=0:
    digit=temp%10
    revno+=str(digit)
    count+=1
    temp=temp//10
    
square=number*number 
s=square
while count !=0:
    digit1=s%10
    revno1+=str(digit1)
    count-=1
    s=s//10
  

if(revno==revno1):
    print("The Number",number,"is Automorphic")
else:
    print("The Number",number,"is not Automorphic")
'''
print(revno)
print(revno1)'''
