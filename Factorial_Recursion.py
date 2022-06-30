def fact(n):
    if(n==1):
        return n
    return n*fact(n-1)
num=int(input("Enter the number\n"))
print("The factorial of",num,"is",fact(num))
