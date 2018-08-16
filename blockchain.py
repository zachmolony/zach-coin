# written by zachmolony 16/08/18

import datetime

#import the class from block.py
from block import Block

# creating linked list as the chain of blocks
block_chain = [Block.create_genesis_block()] # initialising with the genesis block

# print hash of genesis
print("hash: {}".format(block_chain[-1].hash()))

