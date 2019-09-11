import re
fhandle=open('regex_sum_255254.txt')
numberlist=list()
count=0
for line in fhandle:
    numbers=re.findall('[0-9]+',line)
    if not numbers:continue
    for num in numbers:
        numberlist.append(int(num))
        count+=1

print ('There are',count,'values with a sum =',sum(numberlist))