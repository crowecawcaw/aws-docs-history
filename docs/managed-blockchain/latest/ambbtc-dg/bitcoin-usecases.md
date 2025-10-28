# Bitcoin use cases with Amazon Managed Blockchain (AMB) Access Bitcoin

This topic provides a list AMB Access Bitcoin use cases

###### Topics

- [Build a Bitcoin (BTC) wallet to send and
  receive BTC](#bitcoin-wallet "#bitcoin-wallet")
- [Analyze activity on the Bitcoin
  blockchain](#bitcoin-activity "#bitcoin-activity")
- [Verify messages signed using a
  Bitcoin key pair](#bitcoin-signed-messages "#bitcoin-signed-messages")
- [Inspect the Bitcoin mempool](#bitcoin-mempool "#bitcoin-mempool")

## Build a Bitcoin (BTC) wallet to send and

receive BTC

BTC, the native cryptocurrency on the Bitcoin network, serves as an
essential component of the network's security model. It also acts as a
commodity and medium of exchange, widely used by institutions, businesses,
and individuals. Consequently, many wallet applications rely on Bitcoin
nodes to interact with the Bitcoin blockchain. These applications calculate
the balance of unspent outputs (UTXOs) for a given set of addresses, sign
and send transactions to the Bitcoin network, and retrieve data about
historical transactions.

The following is a sample of some of the Bitcoin JSON-RPCs that
Amazon Managed Blockchain (AMB) Access Bitcoin supports for BTC wallet transactions:

- `estimatesmartfee`
- `createmultisig`
- `createrawtransaction`
- `sendrawtransaction`

For more information, see [Supported JSON-RPCs](bitcoin-api.md#supported-json-rpc "bitcoin-api.md#supported-json-rpc").

## Analyze activity on the Bitcoin

blockchain

You can analyze the volume of transaction activity on the Bitcoin
blockchain by using the `getchaintxstats` JSON-RPC method. This
JSON-RPC allows you to access metrics such as average transaction rates per
second, total transaction count, block count, and more. You can also
define a window of block numbers or a block hash as a delimiter to
calculate these statistics for a specific set of blocks in the network,
if desired.

For more information, see [Supported JSON-RPCs](bitcoin-api.md#supported-json-rpc "bitcoin-api.md#supported-json-rpc").

## Verify messages signed using a

Bitcoin key pair

Bitcoin wallets have a private key and a public key that make up a
key pair. These keys are used to sign transactions and serve as the user's
identity on the blockchain. The public key is used to create addresses,
which are standardized alphanumeric identifiers (27 to 34 characters long).
These addresses are used to receive BTC outputs and handle transactions or
messages.

With a Bitcoin wallet, users can also sign and verify messages
cryptographically. This process is often used to prove ownership of a
specific wallet address and the BTC associated with it. By using the
`verifymessage` Bitcoin JSON-RPC, you can check the authenticity and
validity of a message signed by another wallet. Specifically, a
Bitcoin node can be used to verify if a message has been signed using
the private key corresponding to the provided public key derived address
within the signed message itself.

For more information, see [Supported JSON-RPCs](bitcoin-api.md#supported-json-rpc "bitcoin-api.md#supported-json-rpc").

## Inspect the Bitcoin mempool

Many applications need to access the _mempool_ to keep track of pending
transactions, get a list of all pending transactions, or find out where a
transaction came from. To do this, there are Bitcoin JSON-RPCs like
`getmempoolancestors`, `getmempoolentry`, and
`getrawmempool` that support this activity. These Bitcoin JSON-RPCs
help applications get the information they need from the _mempool_.

Amazon Managed Blockchain (AMB) Access Bitcoin also supports the `testmempoolaccept` Bitcoin
JSON-RPCs, which allows you to verify if a transaction meets protocol rules and would
be accepted by a node before submitting. Wallets, exchanges, and any
other entities who directly submit transactions to the Bitcoin blockchain
utilize these Bitcoin JSON-RPCs.

For more information, see [Supported JSON-RPCs](bitcoin-api.md#supported-json-rpc "bitcoin-api.md#supported-json-rpc").
