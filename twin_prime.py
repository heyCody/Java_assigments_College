def prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

for i in range(3,1000):
    if prime(i) and prime(i+2):
        print(i,i+2)
