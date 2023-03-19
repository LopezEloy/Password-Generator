import random #Import the random library

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Below is based on ASCII Code
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random lowercase letter
digit1=chr(random.randint(48,57)) #Generate a random digit
symbol1=chr(random.randint(33,38)) #Generate a random symbol

#Generate password using all the characters, in random order
password = uppercaseLetter1 + lowercaseLetter2 + digit1 + symbol1
password = shuffle(password)

#Ouput
print(password)
