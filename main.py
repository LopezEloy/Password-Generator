import random #Import the random library

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Below is based on ASCII Code
uLetter=chr(random.randint(65,90)) #Generate a random Uppercase letter
lLetter=chr(random.randint(97,122)) #Generate a random lowercase letter
digit1=chr(random.randint(48,57)) #Generate a random digit
symbol1=chr(random.randint(33,38)) #Generate a random symbol

#Generate password using all the characters, in random order
password = uLetter or lLetter or digit1 or symbol1

#Ouput
pwSize = int(input("How long should this passord be? Give a value: "))
pwSym = int(input("How many symbols?: "))
pwDig = int(input("How many digits: "))
pwChar = int(input("How many characters?: "))

print(f"Generating a password of length {pwSize} with {pwSym} symbol(s), {pwDig} digit(s), and {pwChar} character(s)")

for x in range(pwSize):
    if x == pwSize: break
    print (password)

