# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:30:39 2018

@author: Sunny
"""
#Using the hash function sha256

# import sha256
from hashlib import sha256

# text to hash
text = 'I am excited to learn about blockchain!'

#SHA256 is a function used to make a hash of data
#It takes the data in an encoded format
hash_result = sha256(text.encode())

# print result
print(hash_result.hexdigest())    
#hexdigest() is used to extract the encoded value of the hash_result
#without the hexdigest() you will get a string that displays the object type of
#hash_result 
print(hash_result)


