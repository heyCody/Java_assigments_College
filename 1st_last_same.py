l=[]
n=int(input("enter the no of string: "))
for i in range(n):
    l.append(input("Enter a string: "))
print(l)
count=0
for i in l:
    if (i[0]==i[-1]):
        count=count+1

print(count)
