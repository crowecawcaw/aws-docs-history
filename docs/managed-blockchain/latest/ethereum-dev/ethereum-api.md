# Using Ethereum APIs with Amazon Managed Blockchain (AMB)

Amazon Managed Blockchain (AMB) provides API operations for creating and managing token accessors, nodes,
and networks for AMB Access Ethereum. For more information, see the _[AMB Access API Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md")_.

The following section provides a list and reference of the Ethereum (JSON-RPC and Consensus) API methods
that Amazon Managed Blockchain (AMB) supports. It also includes code examples that implement API calls from clients
using either HTTP or WebSocket (JSON-RPC API only) connections.

You use the Ethereum API from a client to query smart contract data and submit transactions
to an Ethereum node on Amazon Managed Blockchain (AMB). You use the Ethereum Consensus API from a client to query the Beacon
chain, its configuration, and the node health. For more information, see [Viewing node details](ethereum-nodes.md#ethereum-node-information "ethereum-nodes.md#ethereum-node-information").

**Execution and consensus client support**

The Ethereum Merge transitioned the Ethereum blockchain to a proof-of-stake
consensus, and it resulted in a new modular design for Ethereum. After the
Merge, the original Ethereum stack forked into two distinct layers: the execution
layer and the consensus layer. There are many different client implementations for
both of these layers; however, Amazon Managed Blockchain (AMB) provides a fully managed Ethereum node
that uses the _GoEthereum (Geth)_ execution client and the
_Lighthouse_ consensus client.

###### Topics

- [Supported JSON-RPC methods](supported-json-rpc.md "supported-json-rpc.md")
- [Supported Consensus API methods](supported-consensus-apis.md "supported-consensus-apis.md")
