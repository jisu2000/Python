n=int(input("Enter The number of Integers:\n"))
sum=0
i=1
while(i<=n):
    num=int(input("Enter the Integer no\n"))
    
    sum=sum+num
    i=i+1
print('The Average of ',n,' Integer is',sum/n)
