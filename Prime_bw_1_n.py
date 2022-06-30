def printprime(num):
    count=0
    i=1
    while(i<=num):
        if(num%i==0):
            count=count+1
        i=i+1
    if(count<=2):
        print(num)
j=int(input("Enter the number you want to Start from\n"))
n=int(input("Enter the index you want to print upto:\n"))
while(j<=n):
    if(j==1):
        j=j+1
    printprime(j)
    j=j+1
    