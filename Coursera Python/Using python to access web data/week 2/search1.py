import re
name=input('Enter File Name: ')
fhandle=open(name+'.txt')
numlist=list()
for line in fhandle:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff)!=1:continue
    print(stuff)
    num=float(stuff[0])
    numlist.append(num)
print('Maximum: ',max(numlist))