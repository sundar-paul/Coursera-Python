import urllib.request
import xml.etree.ElementTree as ET
    
url=input("Enter -")
content=urllib.request.urlopen(url).read()


tree=ET.fromstring(content)
lst=tree.findall('comments/comment')
c=0
sum=0
for i in lst:
    x=int(i.find('count').text)
    c+=1
    sum+=x

print('Count: ',c)
print('Sum: ',sum)