# Key concepts: Amazon Managed Blockchain (AMB) Access Ethereum

###### Note

This guide assumes that you're familiar with the concepts that are essential to Ethereum.
These concepts include nodes, dapps, transactions, gas, Ether, and others. Before you deploy a
node using AMB Access Ethereum and develop dapps, we recommend that you review the [Ethereum Development Documentation](https://ethereum.org/en/developers/docs/ "https://ethereum.org/en/developers/docs/") and
[Mastering
Ethereum](https://cypherpunks-core.github.io/ethereumbook/01what-is.html "https://cypherpunks-core.github.io/ethereumbook/01what-is.html").

You can use Amazon Managed Blockchain (AMB) Access Ethereum to quickly provision [Ethereum nodes](https://ethereum.org/en/developers/docs/nodes-and-clients/ "https://ethereum.org/en/developers/docs/nodes-and-clients/") and join
them to the public Ethereum _mainnet_ or popular public
_testnets_. Ethereum nodes on a network collectively store an Ethereum
blockchain state, verify transactions, and participate in consensus to change a blockchain
state.

You can use an Ethereum node to develop and use decentralized applications (dapps) that
interact with an Ethereum blockchain. The "backend" of a dapp is a _smart
contract_ that runs in a decentralized way across all the nodes that are joined to an
Ethereum network. Anyone that joined to the network can develop and deploy a smart contract that
adds functionality.

The "frontend" of a dapp can use Ethereum API operations and libraries, specifically the
JSON-RPC API or the Consensus API, to interact with the Ethereum network. You can use these
APIs to communicate with Ethereum node in Amazon Managed Blockchain (AMB). These APIs allow the dapp to read data and
write transactions. You can use the JSON-RPC API to query the smart contract data and submit
transactions to an Ethereum node on the AMB Access. You can use the Consensus API to query the Beacon
chain and its configuration. You can also use Consensus API to get the health of nodes on the Mainnet.

With Ethereum APIs in AMB Access, your "frontend" dapp can use an HTTP or WebSocket (JSON-RPC API only)
connection to make API calls. Only users in the AWS account that owns the node can make API
calls. Calls over HTTP and WebSocket connections are authenticated by using the [Signature Version 4 signing
process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").

###### Important

- Amazon Managed Blockchain (AMB) helps you provision Ethereum nodes. You are responsible for creating, maintaining, and using of your Ethereum Accounts. You are also responsible for the contents of your Ethereum Accounts. This includes, but is not limited to, Ether (ETH) and smart contracts. AWS is not responsible for any of your smart contracts tested, compiled, deployed or called using Ethereum nodes in Amazon Managed Blockchain (AMB).
- For historic data that requires archival nodes, use Amazon Managed Blockchain (AMB) Query. For more information, see
  the _[AMB
  Query Developer Guide](../ambq-dg.md "../ambq-dg.md")_.

## Considerations and limitations for Amazon Managed Blockchain (AMB) Access Ethereum

When you use Amazon Managed Blockchain (AMB) Access Ethereum to host a node on an Ethereum network, consider the
following.

- **Supported networks**

Ethereum has a public _mainnet_ and several public
_testnets_ used for development, testing, and proof of concept. AMB Access
supports the following public networks.

    + **Mainnet** – The proof-of-stake network of the primary public Ethereum blockchain. Transactions on Mainnet have actual value (that is, they incur real costs) and are recorded on the distributed ledger. This network supports the JSON-RPC and Consensus API operations.

- **Networks no longer supported**

AMB Access Ethereum no longer supports the following public networks. Private networks aren't supported.

    + **Ropsten** – A public proof-of-stake [read-only](https://twitter.com/etherscan/status/1569311894279958531 "https://twitter.com/etherscan/status/1569311894279958531") testnet. Ether on this network has no real monetary value. You can't provision new nodes on Ropsten as of February 28th, 2023. The Ethereum foundation ceased support of Ropsten on [December 31st, 2022.](https://blog.ethereum.org/2022/11/30/ropsten-shutdown-announcement "https://blog.ethereum.org/2022/11/30/ropsten-shutdown-announcement").
    + **Rinkeby** – A public proof-of-authority [read-only](https://twitter.com/etherscan/status/1569311894279958531 "https://twitter.com/etherscan/status/1569311894279958531") testnet for Go Ethereum (Geth) clients. Ether on this network has no real monetary value. You can't provision new nodes on Rinkeby as of August 10th, 2023. The Ethereum foundation ceased support of Rinkeby on [May 31st, 2023](https://blog.ethereum.org/2022/06/21/testnet-deprecation "https://blog.ethereum.org/2022/06/21/testnet-deprecation").
    + **Görli (Goerli)** – A public cross-client, proof-of-stake network.
     Ether on this network has no real monetary value. In line with the April 17, 2024 sunsetting of the Goerli testnet communicated by the Ethereum Foundation, AMB Access Ethereum
     ended support of the Goerli testnet on April 1, 2024. We recommend using the Sepolia or Holesky testnets for
     your testing workload.

- **Compatibility with popular third-party programming libraries**

AMB Access Ethereum is compatible with popular programming libraries, such as ethers.js allowing developers to interact with the Polygon blockchain using familiar tools to integrate
easily with their existing implementations or develop new applications quickly.

- **Staking not supported**

Ethereum nodes that are created using AMB Access don't support staking.

- **Different endpoints for WebSockets and HTTP**

AMB Access Ethereum supports the Ethereum API over HTTP and WebSocket (JSON-RPC API only). Each Ethereum node in AMB Access
hosts different endpoints for HTTP and WebSocket connections.

- **JSON-RPC batch requests aren't supported**

Ethereum nodes that are created using AMB Access don't support JSON-RPC batch requests.

- **Payload quotas for API calls**

WebSocket calls have a 512 KB payload quota. Some calls might exceed this quota and cause a "message response is too large" error. For this reason, we recommend you use HTTP for these requests instead of WebSocket connections. If your HTTP response is larger than 5.9 MB, you will get an error. To correct this,
you must set both compression headers as `Accept: application/gzip` and `Accept-Encoding: 
 gzip`. The compressed response your client then receives contains the following headers: `Content-Type: application/json` and `Content-Encoding: gzip`.

- **Signature Version 4 signing of API calls**

Ethereum API calls to an Ethereum node in Amazon Managed Blockchain (AMB) can be authenticated by using the
[Signature Version 4 (SigV4) signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").
This means that only authorized IAM principals in the AWS account that created the node can interact with it using
the Ethereum APIs. AWS credentials (an access key ID and secret access key) must be provided with the call.

###### Important

Never embed client credentials in user-facing applications. To expose an Ethereum node in
AMB Access to anonymous users visiting from trusted web domains, you can set up a separate endpoint
in [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md") backed by a Lambda function that forwards requests to your node that uses
the proper IAM credentials.

- **Support for Token Based
  Access**

You can use Accessor tokens to make Ethereum API calls to an Ethereum node as a convenient
alternative to the Signature Version 4 (SigV4) signing process. You must provide a `BILLING_TOKEN`
from one of the Accessor tokens that you create as a query parameter with the call.

###### Important

    + If you prioritize security and auditability over convenience, use the SigV4 signing
     process instead.
    + You can access the Ethereum APIs using Signature Version 4 (SigV4) and token based access. However,
     if you choose to use token based access, then any security benefits that are provided by using
     SigV4 are negated.
    + Never embed Accessor tokens in user-facing applications.

- **Only raw transactions are supported**

AMB Access only supports the use of the `eth_sendRawTransaction` method to submit
transactions that update the Ethereum blockchain state. Before transactions can be sent, you
must create and sign transactions using Ethereum private keys outside AMB Access. In other words,
you can't use AMB Access as an Ethereum wallet. You must generate and store Ethereum transactions
and private keys externally.

- **Node limit per account**

AMB Access supports a maximum of 50 Ethereum nodes for each account.
