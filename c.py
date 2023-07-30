a=int(input("Enter a number :- "))
b=a
sum=0
while a!=0:
 r=a%10
 sum=sum+r**3
 a=int(a/10)
if sum==b:
 print("the entered number is armstrong number")
else:
 print("the entered number is not armstrong number")