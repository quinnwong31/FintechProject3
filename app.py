import json
from web3 import Web3
import streamlit as st

contract = ''

# 
# Initialize the smart contract. 
#
def init_smartcontract(web3):
    # Set default account for paying gas fees
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Load smart contract 
    abi = json.loads('')  # TODO - Need to compile escrow.sol
    bytecode = '' # TODO - Need to compile escrow.sol
    Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

    # Create smart contract
    tx_hash = Greeter.constructor().transact()

    # Get transaction receipt
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    # print(tx_receipt)

    # Get reference to smart contract
    contract = web3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=abi
    )

    return contract

# Connect to Ganache blockchain
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Init smart contract
# TODO - Uncomment once we implement escrow.sol
# contract = init_smartcontract(web3)

# 
# UI for Escrow Smart Contract
#
st.write("# Escrow Smart Contract")

buyerAddress = st.text_input('Buyer Address', 'Enter Buyer Address')
sellerAddress = st.text_input('Seller Address', 'Enter Seller Address')
agentAddress = st.text_input('Agent Address', 'Enter Agent Address')
propertyId = st.text_input('Property ID', 'Enter Property ID')
price = st.text_input('Price', 'Enter Price')

# Set buyer's address
# TODO - Uncomment once we implement escrow.sol
# tx_hash = contract.functions.setBuyerAddress(buyerAddress).transact()
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Set seller's address
# TODO - Uncomment once we implement escrow.sol
# tx_hash = contract.functions.setSellerAddress(sellerAddress).transact()
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Set agent address
# TODO - Uncomment once we implement escrow.sol
# tx_hash = contract.functions.setAgentAddress(agentAddress).transact()
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Set property Id address
# TODO - Uncomment once we implement escrow.sol
# tx_hash = contract.functions.setPropertyId(propertyId).transact()
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)


