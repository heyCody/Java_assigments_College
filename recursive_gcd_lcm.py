def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    if b==0:
        return a
    else:
        return a*b/gcd(a,b)

def lcm1(a,b):
    t=a%b
    if t==0:
        return a
    else:
        return a*lcm1(b,t)//t
    
a=int(input("enter a num: "))
b=int(input("enter a num: "))
print(gcd(a,b))
print(lcm(a,b))
print(lcm1(a,b))

