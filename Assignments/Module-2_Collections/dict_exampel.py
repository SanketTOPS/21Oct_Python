stdata={'id':101,'name':'sanket','sub':'python'}
"""print(stdata)
print(stdata['name'])
print(stdata.get('sub'))
print(stdata.keys())
print(stdata.values())
print(len(stdata))"""


# --------------------------- #
print(stdata)

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

stdata['id']=102 #value change
print(stdata)