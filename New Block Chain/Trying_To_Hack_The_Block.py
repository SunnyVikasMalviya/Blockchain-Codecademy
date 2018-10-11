# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:17:50 2018

@author: Sunny
"""

#Trying to hack into the block chain

from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

#creating a new block chain
my_blockchain = Blockchain()

#adding a new block to the block chain
my_blockchain.add_block(new_transactions)

#printing the block chain
my_blockchain.print_blocks()

#Changing the data of a block at the position 1
my_blockchain.chain[1].transactions = "fake_transactions"

#Checking whether the block chain is still valid
my_blockchain.validate_chain()