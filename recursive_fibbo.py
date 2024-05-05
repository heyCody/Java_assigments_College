def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)

n=int(input("enter the num: "))
for i in range(n):
    print(fibbo(i))
