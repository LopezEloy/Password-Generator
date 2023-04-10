import random #Import the random library

#Below is based on ASCII Code
uLetter=chr(random.randint(65,90)) #Generate a random Uppercase letter
lLetter=chr(random.randint(97,122)) #Generate a random lowercase letter
digit1=chr(random.randint(48,57)) #Generate a random digit

#Keep track of random generated individual passwords
totSym = []
totDig = []
totChar = []

#Ouput
pwSize = int(input("How long should this password be? Give a value: "))
pwSym = int(input("How many symbols?: "))
pwDig = int(input("How many digits: "))
pwChar = int(input("How many characters?: "))

print(f"Generating a password of length {pwSize} with {pwSym} symbol(s), {pwDig} digit(s), and {pwChar} character(s)")

for x in range(0, pwSym):
    symbol1 = chr(random.randint(33,38)) #Generate a random symbol
    totSym.append(symbol1)
print(totSym)

print(''.join(totSym))
