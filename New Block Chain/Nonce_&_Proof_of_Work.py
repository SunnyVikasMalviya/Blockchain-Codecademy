# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:38:23 2018

@author: Sunny
"""

#Nonce & Proof of Work

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
data = str(nonce) + str(new_transactions)
proof = sha256(data.encode()).hexdigest()
# printing proof
print(proof)
  
# finding a proof that has 2 leading zeros
while proof[0: difficulty] != str('0' * difficulty) : 
    #line 26 checks whether the first 'difficulty' i.e. 2 here, characters of \
    #proof are zeroes or not
  nonce += 1
  data = str(nonce) + str(new_transactions)
  proof = sha256(data.encode()).hexdigest()
else :
  final_proof = proof  

# printing final proof that was found
print(final_proof)