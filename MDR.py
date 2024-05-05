
def MDR(n):
    p=1
    while n>0:
        r=n%10
        p*=r
        n//=10
    global count
    count=count+1
    if len(str(p))!=1:
        return MDR(p)


n=int(input("ENter a num: "))
print(MDR(n))
print(count)
