import glob
import re
import numpy as np
import string
import random

f = open('text.txt', 'r')
data = f.read()

for i in range(5):
	index =int(np.random.rand()*len(data))
	times =int(np.random.rand()*3) ## A same charactor appears 3 times...
	#print(index)
	#print(data[index])
	chars=chr(random.randint(0x800,0xFFFF))## I don't know how adress range is assigned as Japanese in Unicode... 
	print(chars)
	data= data[0:index-1] +(chars*times) + data[index:len(data)]

print(data)





f.close()

