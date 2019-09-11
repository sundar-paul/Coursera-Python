fhandle=open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):continue
    word=line.split()
    email=word[1]
    url=email.split('@')
    if url[1]=='uct.ac.za':
        print(url[1])