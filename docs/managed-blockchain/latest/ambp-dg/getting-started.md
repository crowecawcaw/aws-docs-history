Amazon Managed Blockchain (AMB) Access Polygon is in preview release and is subject to change.

# Getting started with Amazon Managed Blockchain (AMB) Access Polygon

Get started with Amazon Managed Blockchain (AMB) Access Polygon by using the information and procedures in this
section.

###### Topics

- [Create an IAM policy to access the Polygon
  blockchain network](#getting-started-next-steps "#getting-started-next-steps")
- [Make Polygon remote procedure call (RPC) requests on the AMB Access RPC editor using the AWS Management Console](#gs-console-polygon "#gs-console-polygon")
- [Make AMB Access Polygon JSON-RPC requests in
  awscurl by using the AWS CLI](#awscurl-polygon-rpc-requests "#awscurl-polygon-rpc-requests")
- [Make Polygon JSON-RPC requests in Node.js](#nodejs-polygon-rpc-requests "#nodejs-polygon-rpc-requests")

## Create an IAM policy to access the Polygon

blockchain network

To access the public endpoint for the Polygon Mainnet to make JSON-RPC calls, you must have
user credentials (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`) that
have the appropriate IAM permissions for Amazon Managed Blockchain (AMB) Access Polygon. In a terminal with the AWS CLI
installed, run the following command to create an IAM policy to access both Polygon
endpoints:

```
cat <<EOT > ~/amb-polygon-access-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid" : "`AMBPolygonAccessPolicy`",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:`InvokeRpcPolygon*`"
            ],
            "Resource": "*"
        }
    ]
}
EOT
aws iam create-policy --policy-name AmazonManagedBlockchainPolygonAccess --policy-document file://$HOME/amb-polygon-access-policy.json

```

###### Note

The previous example gives you access to all available Polygon networks. To get
access to a specific endpoint, use the following `Action` command:

- `"managedblockchain:InvokeRpcPolygonMainnet"`

After you create the policy, attach that policy to your IAM user’s role for it to take
effect. In the AWS Management Console, navigate to the IAM service, and attach the policy
`AmazonManagedBlockchainPolygonAccess` to the role assigned to your IAM user.

## Make Polygon remote procedure call (RPC) requests on the AMB Access RPC editor using the AWS Management Console

You can edit, configure, and submit remote procedure calls (RPCs) on the AWS Management Console using
AMB Access Polygon. With these RPCs, you can read data and write transactions on the Polygon
network, including retrieving data and submitting transactions to the Polygon network.

The following example shows how to get information about the _latest_
block by using `eth_getBlockByNumber` RPC. Change the highlighted variables to
your own inputs or choose one of the **RPC methods** listed and enter in
the relevant inputs required.

1. Open the Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **RPC editor**.
3. In the **Request** section, choose
   `POLYGON_MAINNET` as the
   **`Blockchain Network`**.
4. Choose `eth_getBlockByNumber` as the
   **RPC method**.
5. Enter `latest` as the **`Block
number`** and choose
   `False` as the **Full transaction
   flag**.
6. Then, choose **Submit RPC**.
7. You get the results of the `latest` block in the **Response**
   section. You can then copy the full raw transactions for further analysis or to use in
   business logic for your applications.

For more information, see the [RPCs supported by AMB Access Polygon](polygon-api.md "polygon-api.md")

## Make AMB Access Polygon JSON-RPC requests in

`awscurl` by using the AWS CLI

Sign requests with your IAM user credentials by using [Signature Version 4 (SigV4)](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in
order to make Polygon JSON-RPC requests to the AMB Access Polygon endpoints. The [`awscurl`](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") command line tool can
help you sign requests to AWS services using SigV4. For more information, see the [awscurl README.md](https://github.com/okigan/awscurl#readme "https://github.com/okigan/awscurl#readme").

Install `awscurl` by using the method appropriate to your operating system. On
macOS, HomeBrew is the recommended application:

```
brew install awscurl
```

If you have already installed and configured the AWS CLI, your IAM user credentials and the
default AWS Region are set in your environment and have access to `awscurl`.
Using `awscurl`, submit a request to the Polygon _Mainnet_ by
invoking the `eth_getBlockByNumber` RPC. This call accepts a string parameter
corresponding to the block number for which you want to retrieve information.

The following command retrieves the block data from the Polygon Mainnet by using
the block number in the `params` array to select the specific block for which to
retrieve the headers.

```
awscurl -X POST -d '{ "jsonrpc": "2.0", "id": "`eth_getBlockByNumber-curltest"`, "method":"`eth_getBlockByNumber`", "params":["`latest`", `false`] }' --service managedblockchain https://`mainnet`.polygon.managedblockchain.`us-east-1`.amazonaws.com -k
```

###### Tip

You can also make this same request using `curl` and the AMB Access token based access feature using `Accessor`
tokens. For more information, see [Creating and managing Accessor tokens for token-based access to
make AMB Access Polygon requests](polygon-tokens.md "polygon-tokens.md").

```
curl -X POST -d '{"jsonrpc":"2.0", "id": "`eth_getBlockByNumber-curltest"`, "method":"`eth_getBlockByNumber`", "params":["`latest`", `false`] }' 'https://`mainnet`.polygon.managedblockchain.`us-east-1`.amazonaws.com?billingtoken=`your-billing-token`'

```

The response from either command returns information about the _latest_ block. See the
following example for illustrative purposes:

```
{"error":null,"id":"eth_getBlockByNumber-curltest","jsonrpc":"1.0",
      "result":{"baseFeePerGas":"0x873bf591e","difficulty":"0x18",
      "extraData":"0xd78301000683626f7288676f312e32312e32856c696e757800000000000000009a\
      423a58511085d90eaf15201a612af21ccbf1e9f8350455adaba0d27eff0ecc4133e8cd255888304cc\
      67176a33b451277c2c3c1a6a6482d2ec25ee1573e8ba000",
      "gasLimit":"0x1c9c380","gasUsed":"0x14ca04d",
      "hash":"0x1ee390533a3abc3c8e1306cc1690a1d28d913d27b437c74c761e1a49********;",
      "nonce":"0x0000000000000000","number":"0x2f0ec4d",
      "parentHash":"0x27d47bc2c47a6d329eb8aa62c1353f60e138fb0c596e3e8e9425de163afd6dec",
      "receiptsRoot":"0x394da96025e51cc69bbe3644bc4e1302942c2a6ca6bf0cf241a5724c74c063fd",
      "sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      "size":"0xbd6b",
      "stateRoot":"0x7ca9363cfe9baf4d1c0dca3159461b2cca8604394e69b30af05d7d5c1beea6c3",
      "timestamp":"0x653ff542",
      "totalDifficulty":"0x33eb01dd","transactions":[...],
      "transactionsRoot":"0xda1602c66ffd746dd470e90a47488114a9d00f600ab598466ecc0f3340b24e0c",
      "uncles":[]}}
```

## Make Polygon JSON-RPC requests in Node.js

You can invoke Polygon JSON-RPCs by submitting signed requests using HTTPS to access the
Polygon _Mainnet_ network using the [native https module in Node.js](https://nodejs.org/api/https.html "https://nodejs.org/api/https.html"), or you can
use a third-party library such as [AXIOS](https://axios-http.com "https://axios-http.com"). The
following _Node.js_ examples show you how to make Polygon JSON-RPC requests
to the AMB Access Polygon endpoint using both [Signature Version 4 (SigV4)](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") and
[token-based access](polygon-tokens.md "polygon-tokens.md"). The first example sends a transaction from one address to
another and the following example requests transaction details and balance information from
the blockchain.

To run this example Node.js script, apply the following prerequisites:

1. You must have node version manager (nvm) and Node.js installed on
   your machine. You can find installation instructions for your OS [here](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm").
2. Use the `node --version` command and confirm that you are using _Node
   version 18_ or higher. If required, you can use the `nvm install
v18.12.0` command, followed by the `nvm use v18.12.0` command, to
   install _version 18_, the _LTS_ version of
   Node.
3. The environment variables `AWS_ACCESS_KEY_ID` and
   `AWS_SECRET_ACCESS_KEY` must contain the credentials that are
   associated with your account. .

Export these variables as strings on your client by using the following commands. Replace
the values in _red_ in the following strings with appropriate
values from your IAM user account.

```
export AWS_ACCESS_KEY_ID="`AKIAIOSFODNN7EXAMPLE`"
export AWS_SECRET_ACCESS_KEY="`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`"
```

After you complete all prerequisites, copy the following files
into a directory in your local environment by using your preferred code editor:

_package.json_

```
{
  "name": "polygon-rpc",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "ethers": "^6.8.1",
    "@aws-crypto/sha256-js": "^5.2.0",
    "@aws-sdk/credential-provider-node": "^3.360.0",
    "@aws-sdk/protocol-http": "^3.357.0",
    "@aws-sdk/signature-v4": "^3.357.0",
    "axios": "^1.6.2"
  }
}
```

_dispatch-evm-rpc.js_

```
const axios = require("axios");
const SHA256 = require("@aws-crypto/sha256-js").Sha256;
const defaultProvider = require("@aws-sdk/credential-provider-node").defaultProvider;
const HttpRequest = require("@aws-sdk/protocol-http").HttpRequest;
const SignatureV4 = require("@aws-sdk/signature-v4").SignatureV4;

// define a signer object with AWS service name, credentials, and region
const signer = new SignatureV4({
  credentials: defaultProvider(),
  service: "managedblockchain",
  region: "`us-east-1`",
  sha256: SHA256,
});
const rpcRequest = async (rpcEndpoint, rpc) => {

  // parse the URL into its component parts (e.g. host, path)
  let url = new URL(rpcEndpoint);

  // create an HTTP Request object
  const req = new HttpRequest({
    hostname: url.hostname.toString(),
    path: url.pathname.toString(),
    body: JSON.stringify(rpc),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept-Encoding": "gzip",
      host: url.hostname,
    },
  });

  // use AWS SignatureV4 utility to sign the request, extract headers and body
  const signedRequest = await signer.sign(req, { signingDate: new Date() });

  try {
    //make the request using axios
    const response = await axios({
      ...signedRequest,
      url: url,
      data: req.body,
    });
    return response.data;
  } catch (error) {
    console.error("Something went wrong: ", error);
  }
};

module.exports = { rpcRequest: rpcRequest };
```

_sendTx.js_

###### Warning

The following code uses a hardcoded private key to generate a wallet Signer using
`Ethers.js` for the sake of demonstration only. Do not use this code in
production environments, as it has real funds and poses a security risk.

If needed, contact your account team to advise on wallet and Signer best
practices.

```
const ethers = require("ethers");

//set AMB Access Polygon endpoint using token based access (TBA)
let token = "`your-billing-token`"
let url = `https://`mainnet`.polygon.managedblockchain.`us-east-1`.amazonaws.com?billingtoken=${token}`;

//prevent batch RPCs
let options = {
  batchMaxCount: 1,
};

//create JSON RPC provider with AMB Access endpoint and options
let provider = new ethers.JsonRpcProvider(url, null, options);

let sendTx = async (to) => {
  //create an instance of the Wallet class with a private key
  //DO NOT USE A WALLET YOU USE ON MAINNET, NEVER USE A RAW PRIVATE KEY IN PROD
  let pk = "`wallet-private-key`";
  let signer = new ethers.Wallet(pk, provider);

  //use this wallet to send a transaction of POL from one address to another
  const tx = await signer.sendTransaction({
    to: to,
    value: ethers.parseUnits("`0.0001`", "`ether`"),
  });

  console.log(tx);
};

sendTx("`recipent-address`");
```

_readTx.js_

```
let rpcRequest = require("./dispatch-evm-rpc").rpcRequest;
let ethers = require("ethers");

let getTxDetails = async (txHash) => {
  //set url to a Signature Version 4 endpoint for AMB Access
  let url = "https://`mainnet`.polygon.managedblockchain.`us-east-1`.amazonaws.com";

  //set RPC request body to get transaction details
  let getTransactionByHash = {
    id: "`1`",
    jsonrpc: "2.0",
    method: "`eth_getTransactionByHash`",
    params: [`txHash]`,
  };

  //make RPC request for transaction details
  let txDetails = await rpcRequest(url, getTransactionByHash);

  //set RPC request body to get recipient user balance
  let getBalance = {
    id: "2",
    jsonrpc: "2.0",
    method: "`eth_getBalance`",
    params: `[txDetails.result.to, "latest"]`,
  };

  //make RPC request for recipient user balance
  let recipientBalance = await rpcRequest(url, `getBalance`);

  console.log("TX DETAILS: ", txDetails.result, "BALANCE: ", ethers.formatEther(recipientBalance.result));
};

getTxDetails("`your-transaction-id`");


```

Once these files are saved to your directory, install the
dependencies that are required to run the code using the
following command:

```
npm install
```

### Send a transaction in Node.js

The preceding example sends the native Polygon Mainnet token (POL) from one address to
another by signing a transaction and broadcasting it to the Polygon Mainnet using AMB Access Polygon.
To do this, use the `sendTx.js` script, which uses `Ethers.js`, a
popular library for interacting with Ethereum and Ethereum-compatible blockchains like
Polygon. You need to replace three variables in the code where _highlighted in
red_, including the `billingToken` for your
_Accessor_ token for [token based access](polygon-tokens.md "polygon-tokens.md"),
the _private key_ with which you sign the transaction, and the
_recipient's address_ that receives the POL.

###### Tip

We recommended that you create a fresh private key (wallet) for this purpose rather than reusing
an existing wallet to eliminate the risk of losing funds. You can use the Ethers library’s Wallet class method
createRandom() to generate a wallet to test with. Additionally, if you need to request POL from the Polygon Mainnet,
you can use the public POL faucet to request a small amount to use for testing.

Once you have your `billingToken`, a funded wallet’s _private key_, and the
recipient's address added to the code, you run the following code to sign a transaction for _.0001_ POL
to be sent from your address to another and broadcast it to Polygon Mainnet invoking the `eth_sendRawTransaction` JSON-RPC using the AMB Access Polygon.

```
node sendTx.js
```

The response received back resembles the following:

```
TransactionResponse {
provider: JsonRpcProvider {},
blockNumber: null,
blockHash: null,
index: undefined,
hash: '0x8d7538b4841261c5120c0a4dd66359e8ee189e7d1d34ac646a1d9923********',
type: 2,
to: '0xd2bb4f4f1BdC4CB54f715C249Fc5a991********',
from: '0xcf2C679AC6cb7de09Bf6BB6042ecCF05********',
nonce: 2,
gasLimit: 21000n,
gasPrice: undefined,
maxPriorityFeePerGas: 16569518669n,
maxFeePerGas: 16569518685n,
data: '0x',
value: 100000000000000n,
chainId: 80001n,
signature: Signature {
r: "0x1b90ad9e9e4e005904562d50e904f9db10430a18b45931c059960ede337238ee",
s: "0x7df3c930a964fd07fed4a59f60b4ee896ffc7df4ea41b0facfe82b470db448b7",
yParity: 0,
networkV: null
},
accessList: []
}

```

The response constitutes the transaction receipt. Save the value of the property
`hash`. This is the identifier for the transaction you just submitted to the
blockchain. You use this property in the read transaction example to get additional details
about this transaction from the Polygon Mainnet.

Note that the `blockNumber` and `blockHash` are `null`
in the response. This is because the transaction has not yet been recorded in a block on the
Polygon network. Note that these values are defined later and you might see them when you
request the transaction details in the following section.

### Read a transaction in Node.js

In this section, you request the transaction details for the previously submitted
transaction and retrieve the POL balance for the recipient address using read requests to
the Polygon Mainnet using AMB Access Polygon. In the `readTx.js` file, replace the variable
labeled `your-transaction-id` with the
`hash` you saved from the response from running the code in the previous
section.

This code uses a utility, `dispatch-evm-rpc.js`, which signs HTTPS requests to
AMB Access Polygon with the requisite [Signature Version 4 (SigV4)](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md")
modules from the AWS SDK and sends requests using the widely used HTTP client, [AXIOS](https://axios-http.com "https://axios-http.com").

The response received back resembles the following:

```
TX DETAILS: {
blockHash: '0x59433e0096c783acab0659175460bb3c919545ac14e737d7465b3ddc********',
blockNumber: '0x28b4059',
from: '0xcf2c679ac6cb7de09bf6bb6042eccf05b7fa1394',
gas: '0x5208',
gasPrice: '0x3db9eca5d',
maxPriorityFeePerGas: '0x3db9eca4d',
maxFeePerGas: '0x3db9eca5d',
hash: '0x8d7538b4841261c5120c0a4dd66359e8ee189e7d1d34ac646a1d9923********',
input: '0x',
nonce: '0x2',
to: '0xd2bb4f4f1bdc4cb54f715c249fc5a991********',
transactionIndex: '0x0',
value: '0x5af3107a4000',
type: '0x2',
accessList: [],
chainId: '0x13881',
v: '0x0',
r: '0x1b90ad9e9e4e005904562d50e904f9db10430a18b45931c059960ede337238ee',
s: '0x7df3c930a964fd07fed4a59f60b4ee896ffc7df4ea41b0facfe82b470db448b7'
} BALANCE: 0.0003

```

The response represents the transaction details. Note that the `blockHash` and
`blockNumber` are now likely defined. This indicates that the transaction has
been recorded in a block. If these values are still `null`, wait a few minutes,
then run the code again to check if your transaction has been included in a block. Lastly,
the hexadecimal representation of the recipient address balance
_(0x110d9316ec000)_ is converted to decimal using Ethers’
`formatEther()` method, which converts the hex to decimal and shifts decimal
places by _18 (10^18)_ to give the true balance in POL.

###### Tip

While the preceding code examples illustrate how to use Node.js, Ethers, and Axios to utilize
a few of the supported JSON-RPCs on AMB Access Polygon, you can modify the examples and write other
code to build your applications on Polygon using this service. For a full list of
supported JSON-RPCs on AMB Access Polygon, see [Managed Blockchain API and the JSON-RPCs supported with AMB Access Polygon](polygon-api.md "polygon-api.md").
