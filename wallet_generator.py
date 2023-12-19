from web3 import Web3
import os

def generate_wallets(num_wallets, file_path):
    w3 = Web3()
    
    with open(file_path, 'w') as file:
        for _ in range(num_wallets):
            # Generate a new account
            account = w3.eth.account.create()
            address = account.address
            private_key = account._private_key.hex()
            
            # Write the address and private key to the file
            file.write(f'Address: {address}, Private Key: {private_key}\n')

if __name__ == "__main__":
    num_wallets_to_generate = 5  # Change this to the number of wallets you want to generate
    output_file_path = 'wallets.txt'  # The path to the output file
    
    generate_wallets(num_wallets_to_generate, output_file_path)
    print(f'{num_wallets_to_generate} wallets have been generated and saved to {output_file_path}')
