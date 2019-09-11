fname = input("Enter file name: ")
fhandle = open(fname)
c=0.0;s=0.0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        line=line.rstrip()
        li=line.find(': ')
        t=float(line[li+1:])
        c+=1
        s+=t
print('Average spam confidence:',s/c)
