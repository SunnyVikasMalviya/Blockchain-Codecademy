# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:10:37 2018

@author: Sunny
"""

transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, \
           transaction5, transaction6]

# add your code below

my_transaction = {
  'amount' : '200',
  'sender' : 'A',
  'receiver' : 'B' 
}
mempool.append(my_transaction)

block_transactions = [transaction1, transaction3, transaction4]

