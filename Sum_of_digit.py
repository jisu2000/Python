num=int(input("Enter the number\n"))
n=num
sum=0
while(num!=0):
    rev=num%10
    sum=sum+rev
    num=num//10
print("The Sum of the digit of",n,"is",sum)
