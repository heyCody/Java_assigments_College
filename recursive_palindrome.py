def palin(n,temp):
    if n==0:
        return temp
    else:
        temp=(temp*10)+(n%10)
        return palin(n//10,temp)

try:
    n=int(input("enter: "))
    if n<0:
        raise ValueError
except ValueError:
    print("hello")
else:
    temp=palin(n,0)
    if temp==n:
        print("palindrome")
