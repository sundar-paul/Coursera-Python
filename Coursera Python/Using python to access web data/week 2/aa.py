import re
x='My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9].+',x)
print(y)
y=re.findall('[aeiou]+',x)
print(y) 
n=23535767
print([int(d) for d in str(n)])
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)