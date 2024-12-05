import re

mystr="This is Python!5864564"

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B64',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall('\d',mystr)
x=re.findall('\D',mystr)
print(x)

if x:
    print("Success")
else:
    print("Error!")