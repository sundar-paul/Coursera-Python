name=input("Enter the file name: ")
fhandle=open(name+'.txt')


counts=dict()
for line in fhandle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigword=k 
        bigcount=v

print(bigword,bigcount)