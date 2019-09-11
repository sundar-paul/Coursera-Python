fname = input("Enter file name: ")
fh = open(fname+'.txt')
c=0
for line in fh:
     line = line.rstrip()
     if line.startswith('From ') :
         word=line.split()
         print (word[1])
         c+=1
print('There were',c,'lines in the file with From as the first word')