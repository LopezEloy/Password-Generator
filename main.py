import random #Import the random library

#Getting User input for PW details
pwSize = int(input("How long should this password be? Give a value: "))
pwLet = int(input("How many letters?: "))
pwDig = int(input("How many digits: "))
pwSym = int(input("How many symbols?: "))

print(f"Generating a password of length {pwSize} with {pwLet} letter(s), {pwDig} digit(s), and {pwSym} symbol(s)")

#Keep track of random generated individual passwords in arrays
totLet, totDig, totSym, totPW = [], [], [], []

#Creating for loops to randomize letters, digits, and symbols
for x in range(0, pwLet):
    uLetter=chr(random.randint(65,90)) #Generate a random Uppercase letter
    lLetter=chr(random.randint(97,122)) #Generate a random lowercase letter
    letters = uLetter or lLetter
    totLet.append(letters)

for x in range(0, pwDig):
    digit1 = chr(random.randint(48,57)) #Generate a random digit
    totDig.append(digit1)

for x in range(0, pwSym):
    symbol1 = chr(random.randint(33,38)) #Generate a random symbol
    totSym.append(symbol1)

#Joining all created letters, digits, and symbols
totPW = totSym + totDig + totLet

a = list(totPW)
random.shuffle(a)
print(''.join(a))
