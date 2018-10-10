# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:50:02 2018

@author: Sunny
"""

#Generating the block hash

from datetime import datetime
from hashlib import sha256

class Block:
    #Initializing the block
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    #calling the generate_hash() to get the hash of the self block
    self.hash = self.generate_hash()
    
    #Displaying the block
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
    #Generating the Hash for the block
  def generate_hash(self):
    #block_contents is a string variable that stores the information of the\
    #block
    block_contents = str(self.timestamp) + str(self.transactions) + \
    str(self.nonce) + str(self.previous_hash)
    #block_hash contains the hash of the block
    #sha256 is a hash function
    #it takes encoded string argument
    block_hash = sha256(block_contents.encode())
    #hexdigest() is used to extract the hash value of the variable else it\
    #would just return the address of the variable
    return block_hash.hexdigest()