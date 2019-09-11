fhandle=open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):continue
    word=line.split()
    print(word[2])