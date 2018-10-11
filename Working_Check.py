# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:46:41 2018

@author: Sunny
"""

#Working Check

from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
#local_blockchain.print_blocks()   #For Debugging
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(fake_transactions)
local_blockchain.add_block(block_three_transactions)

local_blockchain.print_blocks()
print(local_blockchain.validate_chain())
