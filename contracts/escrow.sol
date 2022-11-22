pragma solidity 0.8.17;

/* Escrow contract

This contract implements an escrow account for holding funds until
a transfer has been confirmed. It defines the buyer and seller accounts
and allows the buyer to confirm receipt, releasing the deposit.
*/

contract Escrow { 
    address payable buyer;
    address payable seller;

    uint            amount;
    bool    public  payed = false;

    constructor (address payable _buyer, address payable _seller, uint _amount) { 
        buyer = _buyer;
        seller = _seller;
        amount = _amount;
    }

    function confirm_receipt() public {
        if (msg.sender == buyer)
            seller.transfer(amount);
    }

    function deposit() payable public {
        if (msg.sender == buyer && msg.value == amount)
            payed = true;
    }

}