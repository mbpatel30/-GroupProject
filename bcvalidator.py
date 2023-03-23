#!/usr/bin/env python3 
#Name: Member 1 - Kirandeep Singh               
#      Member 2 - Mishwa Patel    
#      Member 3 - Meet Patel
#Date: 2023/03/23

import hashlib

# This is going to define a particular block class in order to store each block in our blockchain
class Block:
    def __init__(self, previous_block_hash, data, RN, current_block_hash):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.random_number = RN
        self.current_block_hash = current_block_hash

# Now what it will do is it will read the data of blockchain from the text file we created 
with open('blockchain_data.txt', 'r') as f:
    blockchain_data = f.readlines()

# Creating an empty file list
blockchain = []

# It will help in to loop through each line and would eventually create a new block
for line in blockchain_data:
    previous_block_hash = line[4:68]
    data = line[8:68]
    random_number_str = line[72:80].strip() # Leading or else trailing whitespace would be removed
    if random_number_str == "":
        RN = None
    else:
        RN = int(random_number_str)
    current_block_hash = line[85:].strip()

    block = Block(previous_block_hash, data, RN, current_block_hash)
    blockchain.append(block)


# Validating each block
for i, block in enumerate(blockchain):
    if i == 0:  # This would be the condition where the first block doesn't have any previous block to verify
        if block.previous_block_hash != "None":
            print("This is an invalid block hash which is previous one for this block", i+1)
            exit()
    else:
        PB = blockchain[i-1]
        previous_block_hash = hashlib.sha256(previous_block.data.encode() + str(previous_block.random_number).encode() + previous_block.current_block_hash.encode()).hexdigest()
        if block.previous_block_hash != previous_block_hash:
            print("This is an invalid block hash which is previous for this block", i+1)
            exit()
    for digit in str(block.random_number):
        if digit not in block.current_block_hash:
            print("This is an invalid random number for this block", i+1)
            exit()
    current_block_hash = hashlib.sha256(block.data.encode() + str(block.random_number).encode() + block.previous_block_hash.encode()).hexdigest()
    if block.current_block_hash != current_block_hash:
        print("This would be an invalid current block for this block", i+1)
        exit()

print("This Blockchain is validated")

