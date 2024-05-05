l=[]
element={}
n=input("enter the no of element: ")
n=int(n)
print("Enter elements: ")
for i in range(n):
    l.append(input())
print(l)
for i in l:
    if i in element:
        element[i]+=1
    else:
        element[i]=1

print(element)

