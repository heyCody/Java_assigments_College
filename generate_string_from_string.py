s=input("enter: ")
s1=s2=" "
for i in range(len(s)):
    if s.count(s[i])>1:
        s1+=s[i]
    else:
        s2+=s[i]
print(s1)
print(s2)
