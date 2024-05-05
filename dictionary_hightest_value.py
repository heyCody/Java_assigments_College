d = {}
d1={}
n=int(input("enter the no of inputs: "))
for i in range(n):
    key = input("Enter key: ")
    value= int(input("Enter value: "))

    d[key] = value

for i in range(3):
    if not d:  # Check if the dictionary is empty
        break   # Break out of the loop if the dictionary is empty
    max_key = max(d, key=d.get)  # Find the key with the maximum value
    max_value = d.pop(max_key)   # Remove the key-value pair with the maximum value
    d1[max_key] = max_value      # Store the key-value pair in the new dictionary

print(d1)
