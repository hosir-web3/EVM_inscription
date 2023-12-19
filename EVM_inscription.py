from web3 import Web3
from hexbytes import HexBytes

# Enter your private key here
private_key = ''

# Chose chain, uncomment the target chain below
# rpc_link = 'https://eth-mainnet.g.alchemy.com/v2/Q1q4tFJe4hUf4iOJWM7SMW7Dtn2iwCvP'# ETH
#rpc_link = 'https://bsc-dataseed3.binance.org/' #BSC
rpc_link = 'https://polygon-mainnet.g.alchemy.com/v2/hrLvjZ3LRWuPItG9LuYsZQcRU_XtvRmX' # polygon
# rpc_link = 'https://oktc-mainnet.public.blastapi.io' #OKT
# rpc_link = 'https://api.avax.network/ext/bc/C/rpc' #AVAX

# Enter the repeat times of inscriptions
no_to_mint = 3

# Enter the data to inscribe
# 0x is not required
hex_data = "93c8ac01bae28307f2c017c134998e92951a66c80c1ad30f8125390c46476eaa"

# Enter the price factor to the current gas fee
# 1 means to use the current gas fee
price_factor = 1

w3 = Web3(Web3.HTTPProvider(rpc_link))
if not w3.is_connected():
    raise ConnectionError("Failed to connect to node")

for i in range(no_to_mint):
    print(f"The inscription being engraved is: {i+1}")
    sender_account = w3.eth.account.from_key(private_key)
    sender_address = sender_account.address
    chain_id = w3.eth.chain_id
    gas_price = w3.eth.gas_price

    transaction = {
        'to': sender_address,
        'value': 0,  # Value is 0 ETH
        'gas': 100000,
        'gasPrice': int(gas_price*price_factor),
        'nonce': w3.eth.get_transaction_count(sender_address),
        'data': hex_data,
        'chainId': chain_id
    }

    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    tx_hash = txn_receipt.transactionHash.hex()

    print(f"The inscription {i+1} is completed, transaction hash is {tx_hash}.")