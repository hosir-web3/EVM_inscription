from web3 import Web3
from hexbytes import HexBytes
import time

# Enter your private key here, 0x is not required
private_key = '' 

# Chose chain, uncomment the target chain below
# rpc_link = 'https://eth-mainnet.g.alchemy.com/v2/Q1q4tFJe4hUf4iOJWM7SMW7Dtn2iwCvP'# ETH
# rpc_link = 'https://bsc-dataseed3.binance.org/' #BSC
# rpc_link = 'https://oktc-mainnet.public.blastapi.io' #OKT
# rpc_link = 'https://api.avax.network/ext/bc/C/rpc' #AVAX
rpc_link = 'https://rpc-1.bevm.io' # BEVM

# Enter the repeat times of inscriptions
no_to_mint = 10 # number of inscription to send for each iteration
repeat_times = 5 # number of iterations

# Enter the data to inscribe
# 0x is not required
hex_data = ""

# Enter the price factor to the current gas fee
# 1 means to use the current gas fee
# it should be greater than 1
price_factor = 1.1

# connect to the node
w3 = Web3(Web3.HTTPProvider(rpc_link))
if not w3.is_connected():
    raise ConnectionError("Failed to connect to node")

# initialization
sender_account = w3.eth.account.from_key(private_key)
sender_address = sender_account.address
chain_id = w3.eth.chain_id

# last nonce of this account, used to compute the transaction count
initial_nonce = w3.eth.get_transaction_count(sender_address) 
print(f"starting nonce is {initial_nonce}")

for i in range(repeat_times):
    try:
        print(f"Repeating time: {i+1}")
        gas_price = w3.eth.gas_price # get the recent price
        start_nonce = w3.eth.get_transaction_count(sender_address) # last nonce of this account
        if i != 0 and start_nonce != last_nonce:
            # if it is not the first time, it is possible the transaction of last time is not packaged
            # the price should not be lower than the last time
            gas_price = max(int(gas_price*price_factor), int(last_gas_price*price_factor))

        print(f"{start_nonce - initial_nonce} inscriptions have been inscribed.")

        # send transaction
        for j in range(no_to_mint):
            nonce = start_nonce + j
            transaction = {
                'to': sender_address,
                'value': 0,
                'gas': 23000,
                'gasPrice': gas_price,
                'nonce': nonce,
                'data': hex_data,
                'chainId': chain_id
            }

            signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
            txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"txn_hash: {txn_hash.hex()}, nonce: {nonce}")
    except Exception as e:
        print(e)
    # get information for next iteration
    last_nonce = start_nonce + no_to_mint
    last_block = w3.eth.get_block_number()
    last_gas_price = gas_price
    while (last_block == w3.eth.get_block_number()):
        # waiting for a new block to be packaged
        time.sleep(3)