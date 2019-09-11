import xml.etree.ElementTree as ET
data='''<person>
    <name>Chuck</name>
    <phone type='int1'>
        +1 734 303 4456
    </phone>
    <email hide='yes'/>
</person>'''

tree=ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('Email: ',tree.find('email').get('hide'))