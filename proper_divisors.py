on=int(input("enter a num: "))
m=int(input("enter a num: "))
sum1=0
for i in range(1,n):
    if n%i==0:
        sum1=sum1+i

sum2=0
for j in range(1,m):
    if m%j==0:
        sum2=sum2+j

if sum1==m and sum2==n:
    print("amicable")
else:
    print("not amicable")
