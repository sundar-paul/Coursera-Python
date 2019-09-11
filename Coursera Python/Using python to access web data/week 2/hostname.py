import re
data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

#atpos=data.find('@')
#sppos=data.find(' ',atpos)
#print(data[atpos+1:sppos])

y=re.findall('^From .*@([^ ]*)',data)
print(y)