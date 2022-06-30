def Linearsearch(l,t):
    i=0
    key=0
    ind=0
    n=len(l)
    while(i<n):
        if(l[i]==t):
            key=1
            ind=i
            break
        i=i+1
    if(key==1):
        print(t,"is present in",ind,"index")
    else:
        print(t,"does not exist in the list")

n=int(input("Enter the Size of the List\n"))
j=0
list=[]
while(j<n):
    x=int(input("Enter the number\n"))
    list.append(x)
    j=j+1
target=int(input("Enter the number the you want to search\n"))
Linearsearch(list,target)
