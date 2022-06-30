def binarysearch(l,t,start,end):
    start=0
    end=len(l)-1
    while(start<=end):
        mid=start+(end-start)//2
        if(l[mid]==t):
            return mid
        elif(t<l[mid]):
            end=mid-1
        else:
            start=mid+1
    return-1
list=[]
n=int(input("Enter the size of the List\n"))
i=0
while(i<n):
    x=int(input("Enter the Element\n"))
    list.append(x)
    i=i+1
print("The list is ",list)
target=int(input("Enter the number You want to Search\n"))
find=binarysearch(list,target,0,n-1)
if(find==-1):
    print(target,"does not exist")
else:
    print(target,"is present in",find,"index")