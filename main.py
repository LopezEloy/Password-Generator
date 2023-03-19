import random #Import the random library

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Below is based on ASCII Code
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4
password = shuffle(password)

#Ouput
print(password)
