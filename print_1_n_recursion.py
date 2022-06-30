def printnum(n):
    if(n==0):
        print(n)
        return
    printnum(n-1)
    print(n)
num=int(input("Enter the Number upto you want to print\n"))
printnum(num)
