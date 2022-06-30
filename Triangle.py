#Area of a Triangle

a=int(input("Enter the First Side\n"))
b=int(input("Enter the Second side\n"))
c=int(input("Enter the Third side\n"))
s=(a+b+c)/2
A=s*(s-a)*(s-b)*(s-c)
r=A**(1/2)
print("The area is ",r)
