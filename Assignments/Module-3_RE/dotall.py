import re

mystr="This is Python!"

x=re.findall('Py..on',mystr)
print(x)

if x:
    print("Success")
else:
    print("Error!")