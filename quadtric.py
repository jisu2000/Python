import math

def quad(a,b,c):
    dis=b*b-4*a*c
    sqrt_val=math.sqrt(abs(dis))
    if(dis>0):
        print("Real and Different roots")
        print((-b+sqrt_val)/(2*a))
        print((-b-sqrt_val)/(2*a))
    elif(dis==0):
        print('Real and same roots')
        print(-b/(2*a))
    else:
        print('Complex Roots')
        print(-b/(2*a), "+i",sqrt_val)
        print(-b/(2*a), "-i" ,sqrt_val)
quad(-1,-2,3)