import Web3 from "web3";
import "./App.css";
import React from "react";
import { Button, Container, Form } from "react-bootstrap";

function App() {
  const [accounts, setAccounts] = React.useState([]);
  const [buyerAddress, setBuyerAddress] = React.useState("");
  const [sellerAddress, setSellerAddress] = React.useState("");
  const [propertyId, setPropertyId] = React.useState("");
  const [price, setPrice] = React.useState("");
  const [escrowContract, setEscrowContract] = React.useState(null);

  // Smart contract configurations
  const ganacheUrl = "http://127.0.0.1:7545";
  const web3 = new Web3(new Web3.providers.HttpProvider(ganacheUrl));
  const abi = JSON.parse(
    '[{"inputs":[{"internalType":"address payable","name":"_buyer","type":"address"},{"internalType":"address payable","name":"_seller","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"confirm_receipt","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"payed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
  );
  const bytecode =
    "60806040526000600360006101000a81548160ff02191690831515021790555034801561002b57600080fd5b50604051610420380380610420833981810160405281019061004d9190610176565b826000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806002819055505050506101c9565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061010d826100e2565b9050919050565b61011d81610102565b811461012857600080fd5b50565b60008151905061013a81610114565b92915050565b6000819050919050565b61015381610140565b811461015e57600080fd5b50565b6000815190506101708161014a565b92915050565b60008060006060848603121561018f5761018e6100dd565b5b600061019d8682870161012b565b93505060206101ae8682870161012b565b92505060406101bf86828701610161565b9150509250925092565b610248806101d86000396000f3fe6080604052600436106100345760003560e01c806312d9a1b91461003957806356e4bc1f14610050578063d0e30db01461007b575b600080fd5b34801561004557600080fd5b5061004e610085565b005b34801561005c57600080fd5b5061006561014a565b60405161007291906101f7565b60405180910390f35b61008361015d565b005b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146100dd57600080fd5b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc6002549081150290604051600060405180830381858888f19350505050158015610147573d6000803e3d6000fd5b50565b600360009054906101000a900460ff1681565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146101b557600080fd5b60025434036101da576001600360006101000a81548160ff0219169083151502179055505b565b60008115159050919050565b6101f1816101dc565b82525050565b600060208201905061020c60008301846101e8565b9291505056fea2646970667358221220eee72a6bf4a61190d4c1f71d0cd6c9338d3ed99fd81c537c5b2aacf4e64ef6f164736f6c63430008110033";

  /**
   * Initialize the list of accounts to display in the buyer and seller dropdowns.
   */
  React.useEffect(() => {
    const init = async () => {
      const accounts = await web3.eth.getAccounts();
      setAccounts(accounts);
    };
    init();
  }, []);

  /**
   * Create the smart contract.
   */
  const handleCreateContract = () => {
    console.log("Creating the smart contract...");

    const contract = new web3.eth.Contract(abi);
    console.log("Created contract...", contract);

    contract
      .deploy({
        data: bytecode,
        arguments: [buyerAddress, sellerAddress, price],
      })
      .send({
        from: buyerAddress,
        gas: 1500000,
      })
      .then((newContractInstance) => {
        contract.options.address = newContractInstance.options.address;
        setEscrowContract(contract);
      });
  };

  /**
   * Event handler for the "Deposit Funds" button.
   */
  const handleDepositFunds = () => {
    console.log("Depositing the funds...");

    escrowContract.methods
      .deposit()
      .send({
        from: buyerAddress,
        to: sellerAddress,
        value: Web3.utils.toWei(price, "ether"),
      })
      .then((tx) => {
        console.log("The funds have been deposited.", tx);
      });
  };

  /**
   * Event handler for the "Confirm Receipt" button.
   */
  const handleConfirmReceipt = () => {
    console.log("Confirm the receipt...");

    escrowContract.methods
      .confirm_receipt()
      .send({
        from: buyerAddress,
        to: sellerAddress,
      })
      .then((tx) => {
        console.log("The receipt has been confirmed.", tx);
      });
  };

  return (
    <div className="App">
      <Container>
        <Form>
          <h2>Smart Contract with React and Web3.js</h2>
          <br />
          <br />
          <Form.Group>
            <Form.Label>Buyer Address</Form.Label>
            <Form.Select
              id="buyerAddress"
              onChange={(e) => {
                setBuyerAddress(e.currentTarget.value);
              }}
            >
              <option value="-1">Select Buyer</option>
              {accounts &&
                accounts.map((value) => <option value={value}>{value}</option>)}
            </Form.Select>
          </Form.Group>
          <Form.Group>
            <Form.Label>Seller Address</Form.Label>
            <Form.Select
              id="sellerAddress"
              // value={accounts}
              onChange={(e) => {
                setSellerAddress(e.currentTarget.value);
              }}
            >
              <option value="-1">Select Seller</option>
              {accounts &&
                accounts.map((value) => <option value={value}>{value}</option>)}
            </Form.Select>
          </Form.Group>
          <Form.Group>
            <Form.Label>Property ID</Form.Label>
            <Form.Control
              id="propertyId"
              type="text"
              placeholder="Enter property ID"
              onChange={(e) => {
                setPropertyId(e.target.value);
              }}
            ></Form.Control>
          </Form.Group>
          <Form.Group>
            <Form.Label>Price</Form.Label>
            <Form.Control
              id="price"
              type="text"
              placeholder="Enter price in Ether"
              onChange={(e) => {
                setPrice(e.target.value);
              }}
            ></Form.Control>
          </Form.Group>
          <br />
          <br />
          <Form.Group>
            <Button
              className="btn btn-primary me-3"
              onClick={handleCreateContract}
            >
              Create Contract
            </Button>
            <Button
              className="btn btn-primary me-3"
              onClick={handleDepositFunds}
            >
              Deposit Funds
            </Button>
            <Button
              className="btn btn-primary me-3"
              onClick={handleConfirmReceipt}
            >
              Confirm Receipt
            </Button>
          </Form.Group>
        </Form>
      </Container>
    </div>
  );
}

export default App;
