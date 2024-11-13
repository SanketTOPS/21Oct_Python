"""stdata={}

n=int(input("Enter number of pairs:"))

for i in range(n):
    k=input("Enter your key:")
    v=input("Enter your value:")
    stdata[k]=v

print(stdata)"""

# -------------------------------- #
stdata={}

keys=['id','name','sub']

for i in keys:
    v=input(f"Enter your value for {i}:")
    stdata[i]=v

print(stdata)