import re
name=input('Enter File Name: ')
fhandle=open(name+'.txt')

for line in fhandle:
    if line.startswith('From'):
        print(re.findall('^From (\S+@\S+)',line))
sentence = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+?@\S+", sentence)
print(y)
