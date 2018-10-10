# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:23:04 2018

@author: Sunny
"""
#Creating a block Class

# import datetime library
from datetime import datetime
# print current date and time
print(datetime.now())

class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = 0
    self.timestamp = datetime.now()