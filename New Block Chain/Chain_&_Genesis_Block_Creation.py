# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:32:57 2018

@author: Sunny
"""

#Creating the chain and the genesis block

#imports the Block class from block.py
from block import Block

class Blockchain:
    #Function to initialize the chain
    def __init__(self):
        #List that contains all the verified transactions
      self.chain = []            
      #List that contains all the unverified transactions
      self.all_transactions = []
      self.genesis_block()     #Creating the genesis block
      
    #Function to create the genesis block    
    def genesis_block(self):
      self.transactions = []
      self.previous_hash = 0
      Block(self.transactions, self.previous_hash)
      self.chain.append(Block)
      