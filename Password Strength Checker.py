import re
password = input("Enter your password: ")

score= 0

#length check
if len(password) >=8:
    score +=1

#uppercase letter     
    if re.search(r"[A-Z]", password):
        score +=1

#lowercase letter
    if re.search(r"[a-z]", password):
        score +=1

#number
    if re.search(r"[0-9]", password):
        score +=1

#special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score +=1

#result
    if score <=2:
        print("\n Weak password")
    elif score==3 or score==4:
        print("\n Medium password")
    else:
        print("\n Strong password")

