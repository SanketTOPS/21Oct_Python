mob=input("Enter your mobile number:")

if mob.isdigit() and len(mob)==10:
    print("Yes...Matching done")
else:
    print("Error!")