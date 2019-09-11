import urllib.request,urllib.parse,urllib.error
import json
import ssl

serviceurl='http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address=input('Entr Location - ')
    if len(address)<1:break
    url=serviceurl+urllib.parse.urlencode({'address':address})
    print('Retriving...',url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrived',len(data),'characters')
    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('======Failed to Retrive Data======')
        print(data)
        continue
    print(json.dumps(js,indent=4))
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print('lat: ',lat,'lng: ',lng)

    location=js['results'][0]['formatted_address']
    print(location)