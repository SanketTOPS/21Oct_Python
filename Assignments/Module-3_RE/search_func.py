import re

mystr="This is Python!"

x=re.search('Python',mystr)
print(x)

if x:
    print("Success!")
else:
    print("Error!")