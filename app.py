from log4python.Log4python import log
log = log("logger")

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
    abi = json.loads('[{"constant":true,"inputs":[],"name":"seller","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_propertyId","type":"uint256"}],"name":"setPropertyId","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"payee","type":"address"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"buyer","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"propertyOwners","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_price","type":"uint256"}],"name":"setPrice","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_buyer","type":"address"}],"name":"setBuyer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_agent","type":"address"}],"name":"setAgent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_seller","type":"address"}],"name":"setSeller","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"propertyId","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"payee","type":"address"}],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"agent","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')  
    bytecode = '608060405234801561001057600080fd5b506108d7806100206000396000f3fe6080604052600436106100dd5760003560e01c8063a3f09ad61161007f578063ee7a3b8e11610059578063ee7a3b8e146103da578063f340fa0114610405578063f5ff5c7614610449578063fc7e286d146104a0576100dd565b8063a3f09ad6146102e7578063bcf685ed14610338578063e99d286614610389576100dd565b80637150d8ae116100bb5780637150d8ae146101c5578063771c6f071461021c57806391b7f5ed14610281578063a035b1fe146102bc576100dd565b806308551a53146100e2578063228b310c1461013957806351cff8d914610174575b600080fd5b3480156100ee57600080fd5b506100f7610505565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561014557600080fd5b506101726004803603602081101561015c57600080fd5b810190808035906020019092919050505061052b565b005b34801561018057600080fd5b506101c36004803603602081101561019757600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610535565b005b3480156101d157600080fd5b506101da610665565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561022857600080fd5b5061026b6004803603602081101561023f57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061068a565b6040518082815260200191505060405180910390f35b34801561028d57600080fd5b506102ba600480360360208110156102a457600080fd5b81019080803590602001909291905050506106a2565b005b3480156102c857600080fd5b506102d16106ac565b6040518082815260200191505060405180910390f35b3480156102f357600080fd5b506103366004803603602081101561030a57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506106b2565b005b34801561034457600080fd5b506103876004803603602081101561035b57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506106f5565b005b34801561039557600080fd5b506103d8600480360360208110156103ac57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610739565b005b3480156103e657600080fd5b506103ef61077d565b6040518082815260200191505060405180910390f35b6104476004803603602081101561041b57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610783565b005b34801561045557600080fd5b5061045e61086d565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156104ac57600080fd5b506104ef600480360360208110156104c357600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610893565b6040518082815260200191505060405180910390f35b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b8060038190555050565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561059157600080fd5b6000600660008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490506000600660008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051600060405180830381858888f19350505050158015610660573d6000803e3d6000fd5b505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60056020528060005260406000206000915090505481565b8060048190555050565b60045481565b806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b80600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b80600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60035481565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156107df57600080fd5b600034905080600660008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205401600660008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505050565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6006602052806000526040600020600091509050548156fea165627a7a72305820d9ec3649ad02997c3dde9774c16c0e8ec0c5129fff65e2740fde6f498e3b40a50029' 
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
contract = init_smartcontract(web3)

# 
# UI for Escrow Smart Contract
#
st.write("# Escrow Smart Contract")

buyerAddress = st.text_input('Buyer Address', 'Enter Buyer Address')
log.info('Buyer address: ' + buyerAddress)

sellerAddress = st.text_input('Seller Address', 'Enter Seller Address')
log.info('Seller address: ' + sellerAddress)

agentAddress = st.text_input('Agent Address', 'Enter Agent Address')
log.info('Agent address: ' + agentAddress)

propertyId = st.text_input('Property ID', 'Enter Property ID')
log.info('Property ID: ' + propertyId)

price = st.text_input('Price', 'Enter Price')
log.info('Price: ' + price)

# Set buyer's address
log.info("Set buyer's address...")
tx_hash = contract.functions.setBuyer(buyerAddress).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
log.info('Buyer tx_receipt: ' + tx_receipt)

# Set seller's address
log.info("Set seller's address...")
tx_hash = contract.functions.setSeller(sellerAddress).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
log.info('Seller tx_receipt: ' + tx_receipt)

# Set agent address
log.info("Set agent's address...")
tx_hash = contract.functions.setAgent(agentAddress).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
log.info('Agent tx_receipt: ' + tx_receipt)

# Set property Id address
log.info("Set property's address...")
tx_hash = contract.functions.setPropertyId(propertyId).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
log.info('PropertyID tx_receipt: ' + tx_receipt)


