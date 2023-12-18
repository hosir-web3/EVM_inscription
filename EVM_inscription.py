from web3 import Web3

# Enter your private key here
private_key = ''

# Chose chain, uncomment the target chain below
# rpc_link = 'https://eth-mainnet.g.alchemy.com/v2/Q1q4tFJe4hUf4iOJWM7SMW7Dtn2iwCvP'# ETH
#rpc_link = 'https://bsc-dataseed3.binance.org/' #BSC
rpc_link = 'https://polygon-mainnet.g.alchemy.com/v2/hrLvjZ3LRWuPItG9LuYsZQcRU_XtvRmX' # polygon
# rpc_link = 'https://oktc-mainnet.public.blastapi.io' #OKT

# Enter the repeat times of inscriptions
no_to_mint = 1

# Enter the data to inscribe
# 0x is not required
hex_data = "646174613a2c7b2270223a226c74632d3230222c226f70223a226d696e74222c227469636b223a2266616972222c22616d74223a22353030227d"

# Enter the price factor to the current gas fee
# 1 means to use the current gas fee
price_factor = 1

for i in range(no_to_mint):
    print(f"Mint ")
    w3 = Web3(Web3.HTTPProvider(rpc_link))
    if not w3.is_connected():
        raise ConnectionError("Failed to connect to node")
    sender_account = w3.eth.account.from_key(private_key)
    sender_address = sender_account.address
    print(sender_address)
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

    print(txn_receipt)