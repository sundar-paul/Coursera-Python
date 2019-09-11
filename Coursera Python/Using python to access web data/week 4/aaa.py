import urllib.request,urllib.parse,urllib.error

fhandle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count=dict()
for line in fhandle:
    words=line.decode().split()
    for word in words:
        count[word]=count.get(word,0)+1
print(count)