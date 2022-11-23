from log4python.Log4python import log
log = log("logger")

import json
from web3 import Web3
import streamlit as st

#
# Create contract.
#
def handle_create_contract():
    # Load smart contract 
    abi = json.loads('[{"inputs":[{"internalType":"address payable","name":"_buyer","type":"address"},{"internalType":"address payable","name":"_seller","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"confirm_receipt","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"payed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]')
    bytecode = '60806040526000600360006101000a81548160ff02191690831515021790555034801561002b57600080fd5b50604051610420380380610420833981810160405281019061004d9190610176565b826000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806002819055505050506101c9565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061010d826100e2565b9050919050565b61011d81610102565b811461012857600080fd5b50565b60008151905061013a81610114565b92915050565b6000819050919050565b61015381610140565b811461015e57600080fd5b50565b6000815190506101708161014a565b92915050565b60008060006060848603121561018f5761018e6100dd565b5b600061019d8682870161012b565b93505060206101ae8682870161012b565b92505060406101bf86828701610161565b9150509250925092565b610248806101d86000396000f3fe6080604052600436106100345760003560e01c806312d9a1b91461003957806356e4bc1f14610050578063d0e30db01461007b575b600080fd5b34801561004557600080fd5b5061004e610085565b005b34801561005c57600080fd5b5061006561014a565b60405161007291906101f7565b60405180910390f35b61008361015d565b005b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146100dd57600080fd5b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc6002549081150290604051600060405180830381858888f19350505050158015610147573d6000803e3d6000fd5b50565b600360009054906101000a900460ff1681565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146101b557600080fd5b60025434036101da576001600360006101000a81548160ff0219169083151502179055505b565b60008115159050919050565b6101f1816101dc565b82525050565b600060208201905061020c60008301846101e8565b9291505056fea2646970667358221220eee72a6bf4a61190d4c1f71d0cd6c9338d3ed99fd81c537c5b2aacf4e64ef6f164736f6c63430008110033'
    Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

    # Create smart contract
    print(buyerAddress)
    print(sellerAddress)
    print(propertyId)
    tx_hash = Greeter.constructor(
        buyerAddress, sellerAddress, price).transact({'from': buyerAddress})

    # # Get transaction receipt
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(tx_receipt)

    # Get reference to smart contract
    st.session_state.contract = web3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=abi
    )

# 
# Deposit the funds.
#
def handle_deposit_funds():
    print('handle_deposit_funds')
    st.session_state.contract.functions.deposit().transact(
        {'from': buyerAddress, 
         'to': sellerAddress, 
         'value': web3.toWei(price,'ether')})

# 
# Confirm Receipt.
#
def handle_confirm_receipt():
    print('handle_confirm_receipt')
    st.session_state.contract.functions.confirm_receipt().transact(
        {'from': buyerAddress, 
         'to': sellerAddress})

# Connect to Ganache blockchain
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Init smart contract
# contract = init_smartcontract(web3)

# 
# UI for Escrow Smart Contract
#
st.write("# Escrow Smart Contract")

buyerAddress = st.text_input('Buyer Address', 'Enter Buyer Address', key='txt_buyer_addr')
sellerAddress = st.text_input('Seller Address', 'Enter Seller Address', key='txt_seller_addr')
propertyId = st.number_input('Property ID', value=0, key='txt_property_id')
price = st.number_input('Price', value=0, key='txt_price')

st.button('Create Contract', on_click=handle_create_contract)

st.button('Deposit Funds', on_click=handle_deposit_funds)

st.button('Confirm Receipt', on_click=handle_confirm_receipt)


st.write(buyerAddress)
st.write(sellerAddress)
st.write(price)


