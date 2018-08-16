# written by zachmolony 16/08/18

import datetime

#import the class from block.py
from block import Block

# creating linked list as the chain of blocks
block_chain = [Block.create_genesis_block()] # initialising with the genesis block

# print hash of genesis
print("hash: {}".format(block_chain[-1].hash()))

# var for blockchain len
num_blocks_to_add = 10

# for loop for adding blocks to the list
for i in range(1, num_blocks_to_add+1):
    # add block with previous block hash
    block_chain.append(Block((block_chain[-1]).hash(), "data", datetime.datetime.now()))
    print("Block #{} created.".format(i))
    print("Block #{} hash: {}".format(i, block_chain[i].hash()))
