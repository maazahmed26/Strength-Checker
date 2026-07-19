import random
import string

#ask the user for password strength
length = int(input("Enter the password length: "))

#ask for special characters
special = input("Do you want special characters? (Y/N): ")

#characters to use
characters = string.ascii_letters + string.digits

#add special characters if user chooses Y
if special.upper() == "Y" :
    characters += string.punctuation


#generate password 
password = ""

for i in range(length):
    password += random.choice(characters)

#display the password
print("\n Generated Password: ",password)


