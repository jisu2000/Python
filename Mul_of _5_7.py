n=int(input("Enter the Number\n"))
if(n%5==0 and n%7==0):
    print(n,"is multiple of 5 and 7 both")
elif(n%5==0 and n%7!=0):
    print(n,"is multiple of 5 but not multiple of 7")
elif(n%5!=0 and n%7==0):
    print(n,"is multiple of 7 but not multiple of 5")
else:
    print(n,"is neighter multiple of 5 nor 7")
