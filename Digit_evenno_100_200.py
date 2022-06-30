def total(num):
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum+rem
        num=num//10
    return sum
i=100
while(i<=200):
    if(total(i)%2==0):
        print(i)
    i=i+1




    