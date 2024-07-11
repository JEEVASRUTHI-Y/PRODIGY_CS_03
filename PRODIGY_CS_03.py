import string
import sys
password=input("Enter the password to check it's complexity: ")
uppercase=[]
lowercase=[]
digits=[]
special=[]
for c in password:
    if c in string.ascii_uppercase:
        uppercase.append(1)
    else:
        uppercase.append(0)
for c in password:
    if c in string.ascii_lowercase:
        lowercase.append(1)
    else:
        lowercase.append(0)
for c in password:
    if c in string.digits:
        digits.append(1)
    else:
        digits.append(0)
for c in password:
    if c in string.punctuation:
        special.append(1)
    else:
        special.append(0)
uppercase=any(uppercase)
lowercase=any(lowercase)
special=any(special)
digits=any(digits)

l=len(password)
strength=0
characters=[uppercase,lowercase,special,digits]
filereader = open("passwords.txt","r")
f=filereader.read().splitlines()

if(password in f):
    print("Password is found in the common list.Strength:0")
    sys.exit()
if l>8:
    strength=strength+1
if l>16:
    strength=strength+1
if l>24:
    strength=strength+1
    
    
if sum(characters)>1:
    strength=strength+1
if sum(characters)>2:
    strength=strength+1
if sum(characters)>3:
    strength=strength+1

if strength<=2:
    print("The password is quite weak!,And It's Strength is:",strength)
elif strength==3:
    print("The password is moderate and It's strength is ",strength)
elif strength>3 and strength<5:
    print("The password is strong,It's strength is ",strength)