def findmax(l):
    i=0
    max=l[i]
    n=len(l)
    while(i<n):
        if(l[i]>max):
            max=l[i]
        i=i+1
    return max
 
n=int(input("Enter the size of the list\n"))
i=0
list=[]
while(i<n):
    x=int(input("Enter the number\n"))
    list.append(x)
    i=i+1
print('The list is',list)
print("The maximum of the list is",findmax(list))




    
