list=[]
j=1
sum=0
n=int(input("Enter the size of List\n"))
while(j<=n):
    x=int(input("Enter the number\n"))
    list.append(x)
    sum=sum+x
    j=j+1
print('The list is',list)
print("the sum of the list is",sum)

