name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name+'.txt')
d=dict()
count = 0
for line in handle:
    
    if not line.startswith('From'):continue
        
    line=line.split()
    
    if line[0]=='From':
        
        line =  line[5].split(':')
        
        for hrs in line[0].split():
            
            if hrs not in d:
                
                d[hrs]=1
            else:
                d[hrs]+=1
                
for key,value in sorted(d.items()):
    print (key,value)