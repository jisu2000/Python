def factors(num):
    i=1
    count=0
    while(i<=num):
        if(num%i==0):
            count=count+1
        i=i+1
    return count
n=int(input("Enter The number\n"))
if(factors(n)<=2):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
