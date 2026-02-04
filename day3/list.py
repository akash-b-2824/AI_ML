x=[ "Apples", "Bananas", "Carrots", "Dates"]
print("contents of x:")
for i in x:
    print(i)
print(10*"*")
x.append("eggs")
print("after adding eggs:",x)
x.remove("Bananas")
print("after remove:",x)
x.sort()
print('sorted list:')
print(x)
print(10*"*")
for i in x:
    print(i)