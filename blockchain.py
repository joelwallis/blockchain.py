class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Creates the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
