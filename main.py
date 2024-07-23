import hashlib
import time

class Block:
    def __init__(self, transactions, previous_hash=''):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.block_hash[:difficulty] != target:
            self.nonce += 1
            self.block_hash = self.calculate_hash()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.block_hash = self.calculate_hash()

    def __str__(self):
        return f"Block:\nTimestamp: {self.timestamp}\nTransactions: {self.transactions}\nPrevious Hash: {self.previous_hash}\nHash: {self.block_hash}\n"

class Blockchain:
    def __init__(self):
        self.blocks = []
        self.difficulty = 2  # Set difficulty level for mining

        # Create the genesis block
        genesis_block = Block(['Genesis Block'])
        genesis_block.mine_block(self.difficulty)
        self.blocks.append(genesis_block)

    def add_block(self, block):
        block.previous_hash = self.blocks[-1].block_hash
        block.mine_block(self.difficulty)
        self.blocks.append(block)

    def displayBlockchain(self):
        for block in self.blocks:
            print(block)

    def validation(self):
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]

            if current_block.block_hash != current_block.calculate_hash():
                print("Invalid block detected due to hash mismatch!")
                return False

            if current_block.previous_hash != previous_block.block_hash:
                print("Invalid block detected due to previous hash mismatch!")
                return False

        print("Blockchain is valid.")
        return True

    def updateBlockchain(self):
        for i in range(1, len(self.blocks)):
            self.blocks[i].previous_hash = self.blocks[i - 1].block_hash
            self.blocks[i].block_hash = self.blocks[i].calculate_hash()

def menu():
    # Create blockchain Object
    block_chain = Blockchain()
    blocks = []
    count = 0

    # This loop helps to perform different blockchain actions
    while True:
        print("----------")
        print("press 1 to add new transaction")
        print("press 2 to create new block")
        print("press 3 to display the Blockchain")
        print("press 4 to validate the Blockchain")
        print("press 5 to update the Blockchain")
        print("press 6 to exit this menu")
        a = input("Choose the above option: ")
        print()

        if a == '1':
            print("Select the block in which you want to insert Transaction: ")
            if count == 0:
                print("There is no Block in the Blockchain...")
                print("Create Block First...")
                continue
            else:
                for i in range(len(blocks)):
                    print(f"{i}  {blocks[i].block_hash}")
                a = int(input("Enter block number to add transaction in that block: "))
                if a >= count:
                    print("Invalid Block Number")
                    continue
                transaction = [input("Enter Transaction: ")]
                block_chain.blocks[a].add_transaction(transaction)
                print("Transaction added successfully...")
                block_chain.updateBlockchain()
            continue  # Ensure the loop continues after this option

        if a == '2':
            transaction = [input("Enter Transaction: ")]
            if count == 0:
                block = Block(transaction)
            else:
                block = Block(transaction, blocks[count - 1].block_hash)
            blocks.append(block)
            block_chain.add_block(block)
            count += 1
            continue  # Ensure the loop continues after this option

        if a == '3':
            block_chain.displayBlockchain()
            continue  # Ensure the loop continues after this option

        if a == '4':
            block_chain.validation()  # Corrected the typo here
            continue  # Ensure the loop continues after this option

        if a == '5':
            block_chain.updateBlockchain()
            continue  # Ensure the loop continues after this option

        if a == "6":
            exit(0)

def main():
    print("Welcome to my Blockchain Coin!!!")
    print()
    menu()

if __name__ == "__main__":
    main()
