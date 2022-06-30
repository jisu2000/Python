n=int(input("Enter the number of Real number\n"))
i=p=1
while(i<=n):
    num=int(input("Enter the Number\n"))
    p=p*num
    i=i+1
print("Geometric mean of inputted number is",p**(1/n))
