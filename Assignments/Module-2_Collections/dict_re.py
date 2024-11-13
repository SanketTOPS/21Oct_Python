stdata={'id':1,'name':'sanket','city':'rajkot'}
"""print(stdata)

print(stdata['city'])
print(stdata.get("name"))
print(stdata.keys())
print(stdata.values())
print(len(stdata))"""

# ------------------------- #
#print(stdata)
"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

# ------------------------- #
print(stdata)
stdata["sub"]="Python" #Insert a new pair
stdata["id"]=2 #Update a value
#stdata.pop('city')
#stdata.clear()
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)
