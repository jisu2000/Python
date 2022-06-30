n=int(input("Enter the size of the List\n"))
i=0
list=[]
listnew=[]
while(i<n):
    x=int(input("Enter the number\n"))
    list.append(x)
    if(x%2!=0):
        listnew.append(x)
    i=i+1
print("The list you have entered is",list)
print("The list with all odd number is",listnew)

