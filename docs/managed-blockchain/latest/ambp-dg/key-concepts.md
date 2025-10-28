Amazon Managed Blockchain (AMB) Access Polygon is in preview release and is subject to change.

# Key concepts: Amazon Managed Blockchain (AMB) Access Polygon

###### Note

This guide assumes that you're familiar with the concepts that are essential to Polygon. These
concepts include staking, dApps, transactions, wallets, smart contracts, Polygon (POL, formerly
MATIC), and others. Before using Amazon Managed Blockchain (AMB) Access Polygon, we recommend that you review the [Polygon Development Documentation](https://polygon.technology/developers "https://polygon.technology/developers") and the
[Polygon wiki](https://wiki.polygon.technology/ "https://wiki.polygon.technology/").

Amazon Managed Blockchain (AMB) Access Polygon provides you with serverless access to the Polygon Mainnet and Polygon Mainnet
networks, without requiring you to provision and manage any Polygon infrastructure, including
nodes. Polygon nodes on a network collectively store a Polygon blockchain state, verify
transactions, and participate in consensus to change a blockchain state. You can use this
managed service to access the Polygon networks quickly and on demand, reducing your overall cost
of ownership.

With AMB Access Polygon, you have access to JSON Remote Procedure (JSON-RPC) calls. You can invoke
Polygon JSON-RPCs to communicate with the Polygon blockchain through nodes managed by Managed Blockchain. You
can use the AMB Access Polygon service to develop and use decentralized applications (dApps) that
interact with the Polygon blockchain. An integral part of dApps are _smart
contracts_. You can create and deploy smart contracts into the Polygon blockchain
using AMB Access Polygon. You can also check balances for your wallets, transaction details, estimate
fees, and so on, by invoking JSON-RPCs against AMB Access Polygon endpoints that run in a
decentralized way across all the nodes that are peers to the Polygon network. Any peer to the
Polygon network can develop and deploy a smart contract.

###### Important

You are responsible for creating, maintaining, using, and managing your Polygon addresses. You
are also responsible for the contents of your Polygon addresses. AWS is not responsible for any
transactions deployed or called using Polygon nodes on Amazon Managed Blockchain.

## Considerations and limitations for

using Amazon Managed Blockchain (AMB) Access Polygon

When you use Amazon Managed Blockchain (AMB) Access Polygon, consider the following:

- **Supported Polygon networks**

AMB Access Polygon supports the following public networks:

    + **Mainnet**—The public Polygon blockchain secured by
     proof-of-stake consensus, and on which the Polygon (POL) token is issued and transacted.
     Transactions on Mainnet have actual value (that is, they incur real costs) and are recorded
     on the public blockchain.

- **Networks no longer supported by Polygon**
  - As [communicated by Polygon Labs](https://polygon.technology/blog/polygon-pos-is-cooking-the-napoli-upgrade-means-better-ux-the-mumbai-testnet-takes-a-bow "https://polygon.technology/blog/polygon-pos-is-cooking-the-napoli-upgrade-means-better-ux-the-mumbai-testnet-takes-a-bow"), the Mumbai Testnet network will sunset in
    mid-April. In line with this news, AMB Access Polygon ended support of the Mumbai Testnet on
    April 15, 2024. We recommend using Amoy Testnet for your testing workload.
  - Private networks are not supported.
  - Furthermore, AMB Access Polygon does not include
    support for the _Polygon zkEVM_ network.

- **Compatibility with popular third-party programming libraries**

AMB Access Polygon is compatible with popular programming libraries, such as ethers.js, allowing developers to interact with the Polygon blockchain using familiar tools to integrate
easily with their existing implementations or develop new applications quickly.

- **Supported Regions**

This service is supported only in the US East (N. Virginia) Region.

- **Service endpoints**

The following are the service endpoints for AMB Access Polygon. To connect with the service, you
must use an endpoint that includes one of the supported Regions.

    + `mainnet.polygon.managedblockchain.us-east-1.amazonaws.com`

- **Staking not supported**

AMB Access Polygon does not support Polygon (POL) validator nodes for proof-of-stake.

- **Signature Version 4 signing of Polygon JSON-RPC requests**

When making calls to the Polygon JSON-RPCs on Amazon Managed Blockchain, you
can do so over an HTTPS connection authenticated using the [Signature Version 4 signing
process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). This means that only authorized IAM principals in the AWS
account can make Polygon JSON-RPC calls. To do this, AWS credentials
(an access key ID and a secret access key) must be provided with the call.

###### Important

    + Do not embed client credentials in user-facing applications.
    + You cannot use IAM policies to restrict access to individual Polygon JSON-RPCs.

- **Support for Token Based Access**

You can also use _Accessor_ tokens to make JSON-RPC
calls to the Polygon network endpoints as a convenient alternative to the Signature Version 4 (SigV4) signing
process. You must provide a `BILLING_TOKEN` from one of the Accessor tokens you [create](../APIReference/API_CreateAccessor.md "../APIReference/API_CreateAccessor.md") and add as a parameter with your calls.

###### Important

    + If you prioritize security and auditability over convenience, use the SigV4 signing
     process instead.
    + You can access the Polygon JSON-RPCs using Signature Version 4 (SigV4) and token-based access.
     However, if you choose to use both protocols, your request is rejected.
    + You must never embed Accessor tokens in user-facing applications.

- **Only submissions of raw transactions are supported**

Use the `eth_sendrawtransaction` JSON-RPC to submit transactions
that update the Polygon blockchain state.
