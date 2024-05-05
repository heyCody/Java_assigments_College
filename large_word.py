def long_word(words):
    for i in words:
        maxi=0
        if len(i)>maxi:
            maxi=len(i)
            k=i
    return (maxi,k)

n=int(input("enter num of words"))
words=[]
for i in range(n):
    words.append(input("enter: "))
..
print(long_word(words))
