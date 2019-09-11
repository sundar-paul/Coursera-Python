name=input("Enter the file name: ")
fhandle=open(name+'.txt')


counts=dict()
for line in fhandle:
    if not line.startswith('From:'):continue
    words=line.split()
    counts[words[1]]=counts.get(words[1],0)+1

bigcount=None
bigword=None
for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigword=k
        bigcount=v

print(bigword,bigcount)