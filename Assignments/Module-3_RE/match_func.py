import re

mystr="This is Python!"

x=re.match('This',mystr)
print(x)

if x:
    print("Success!")
else:
    print("Error!")