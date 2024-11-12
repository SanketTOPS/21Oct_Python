"""stdata=[]
n=int(input("Enter number of students:"))

for i in range(n):
    nm=input("Enter a name:")
    stdata.append(nm)

#print(stdata)
print(set(stdata))"""


myset=set()
n=int(input("Enter number of students:"))

for i in range(n):
    nm=input("Enter a name:")
    myset.add(nm)

print(myset)
