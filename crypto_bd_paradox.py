import random
import math
import string
from Crypto.Hash import SHA256
import time



def randomString(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))

def hash(data):
    h=SHA256.new()
    h.update(data.encode("ASCII"))
    return h.hexdigest()[52:]

needet=math.sqrt(2**48)
lenOfString=math.ceil(math.log(needet,len(string.ascii_letters+string.hexdigits)))*5
calculated_hashes={}
'''
i=0
while len(calculated_hashes) < needet:
    x=randomString(int(lenOfString))
    hash_x=hash(x)
    if x in calculated_hashes.keys():
        print("FOUD COLLISION!!!")
        print("HASH: "+hash_x)
        print("VAL1: "+x)
        print("VAL2: "+calculated_hashes[hash_x])
        print("iterations: "+(str(i)))
        break
    else:
        calculated_hashes[hash_x]=x
        i+=1
'''
print(len(calculated_hashes))
i = 0
strat_time=time.time()
while 1:
    x=randomString(int(lenOfString))
    hash_x=hash(x)
    if hash_x in calculated_hashes.keys():
        print("FOUD COLLISION (in checker)!!!")
        print("HASH: "+hash_x)
        print("VAL1: "+x)
        print("VAL2: "+calculated_hashes[hash_x])
        print("iterations: "+(str(i)))
        print("pretekl: "+ str(time.time() - strat_time))
    calculated_hashes[hash_x]=x
    if(i % 1000000 == 0):
        print(str(i))
    i+=1
    
