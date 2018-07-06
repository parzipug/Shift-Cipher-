import time
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
partial1 = " "
partial2 = " "
newalphabet = " "

msg = input("Enter secret message here >>>").lower()
newmsg = ' '
key = int(input("Enter shift amount >>>"))


if key == 0:
    newalphabet = alphabet

elif key > 0:
    partial1 = alphabet[:key]
    partial2 = alphabet[key:]
    newalphabet = partial2 + partial1

else:
    partial1 = alphabet[ : (26 + key) ]
    partial2 = alphabet[ (26 + key) : ]
    newalphabet = partial2 + partial1


for x in range(0, len(msg)):
    index = alphabet.find(msg[x])

    if index < 0:
        newmsg += msg[x]
    else:
        newmsg += newalphabet[index]

        
print("<<<Here is your encoded shifted message!>>>")
print(newmsg)
