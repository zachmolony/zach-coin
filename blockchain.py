# written by zachmolony 16/08/18

import hashlib

class Block:
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash

    # get hash method which hashes entire Block info
    def get_hash(self):
        # get binary representation of the header
        header.binary = (str(self.previous_block_hash) +
                        str(self.data) +
                        str(self.timestamp)).encode()

        # run through encrpyion twice to ensure that the hash is not changed
        inner_hash = hashlib.sha256(header_binary).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
