c={'c':10,'a':23,'b':9}
tmp=list()
for k,v in c.items():
    tmp.append( (v,k) )
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)