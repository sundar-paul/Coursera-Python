num=list()
while True:
    inp=input("Enter value: ")
    if inp=='done':break
    num.append(float(inp))
print(sum(num)/len(num))
