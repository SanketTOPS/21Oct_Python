import re

mystr="This is Python!4566"

#x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[0-9]',mystr)
x=re.findall('[A-Za-z]',mystr)
print(x)

if x:
    print("Success")
else:
    print("Error!")