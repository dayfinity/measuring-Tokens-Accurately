import random
from datetime import datetime

from web3 import Web3
from eth_account import Account

URL = "https://rpc.example.org"
PRIVATE = "YOUR_PRIVATE_KEY"

node = Web3(
    Web3.HTTPProvider(URL)
)

user = Account.from_key(
    PRIVATE
)

gas_value = random.randint(
    118000,
    123000
)

payload = {
    "from": user.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": gas_value,
    "gasPrice": node.to_wei(
        4,
        "gwei"
    ),
    "nonce": node.eth.get_transaction_count(
        user.address
    ),
    "chainId": 1,
}

signed = user.sign_transaction(
    payload
)

raw = signed.raw_transaction.hex()

details = {
    "tim
