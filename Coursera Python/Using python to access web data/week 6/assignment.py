import urllib.request
import json
import ssl
url = ' http://py4e-data.dr-chuck.net/comments_255259.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=4))

count=0
sum=0

for i in js['comments']:
    count = count+1
    sum = sum + i['count']

print('Count: ',count)
print('Sum: ',sum)