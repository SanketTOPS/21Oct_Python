import re

mystr="This is Python!154646484"

#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
x=re.findall('74$',mystr)
print(x)

if x:
    print("Success")
else:
    print("Error!")
