l=[]

n=int(input("enter the no of tuples: "))
for i in range(n):
    flag=[]
    for j in range(2):
        flag.append(int(input("Enter a no: ")))
    l.append(tuple(flag))
        
print(l)
l = sorted(l, key=lambda x: x[-1])

print("Sorted list of tuples:", l)



    
