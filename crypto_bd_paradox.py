import random
import math
import string

def randomString(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))

needet=math.sqrt(2**48)
lenOfString=math.ceil(math.log(needet,len(string.ascii_letters+string.hexdigits)))*5
calculated_hashes={}

while len(calculated_hashes) < needet:
    x=randomString(int(lenOfString))
    if x not in calculated_hashes.keys():
        calculated_hashes[x] = x

print(len(calculated_hashes))

while 1:
    x=randomString(int(lenOfString))
    if x in calculated_hashes.keys():
        print("FOUND COLLISON: " + calculated)
        break
