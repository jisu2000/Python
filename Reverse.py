n=int(input("Enter The Number\n"))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The number after has been reversed is",rev)
