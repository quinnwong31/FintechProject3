pragma solidity ^0.5.0;
contract Escrow { 

    // buyer's address
    address public buyer;

    // seller's address
    address public payable seller;

    // agent's address
    address public agent;

    // propertyId
    uint public propertyId;

    // price 
    uint public price;

    // Constructor
    function Escrow() public { 
        // TODO
    }

    // Implement setters and getters

    // Implement deposit
    function deposit(address payee) public payable { 
       // uint256 amount = msg.value
    }

    // Implement withdraw
    function withdraw() public { 
        
    }
}