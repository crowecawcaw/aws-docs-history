# Key concepts: Amazon Managed Blockchain (AMB) Access Bitcoin

###### Note

This guide assumes that you're familiar with the concepts that are essential to Bitcoin. These
concepts include decentralization, nodes, transactions, proof-of-work, wallets, public and
private keys, halvings, and others. Before using Amazon Managed Blockchain (AMB) Access Bitcoin, we recommend that you review the
[Bitcoin Development Documentation](https://developer.bitcoin.org/ "https://developer.bitcoin.org/") and [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook "https://github.com/bitcoinbook/bitcoinbook").

Amazon Managed Blockchain (AMB) Access Bitcoin provides you with serverless access to the Bitcoin blockchain, without requiring
you to provision and manage any Bitcoin infrastructure, including nodes. You can use this managed
service to access the Bitcoin networks quickly and on-demand, reducing your overall cost of
ownership.

The AMB Access Bitcoin provides you with access to the Bitcoin network through full nodes running the
Bitcoin Core client, with the wallet functionality disabled, and supporting several JSON Remote
Procedure (JSON-RPC) calls. You can invoke Bitcoin JSON RPCs to communicate with Bitcoin nodes
managed by Managed Blockchain to interact with the Bitcoin networks. With the Bitcoin JSON-RPCs, you can read
data and write transactions, including querying data and submitting transactions to the Bitcoin
networks by using the Amazon Managed Blockchain service.

###### Important

You are responsible for creating, maintaining, using, and managing your Bitcoin addresses. You
are also responsible for the contents of your Bitcoin addresses. AWS is not responsible for any
transactions deployed or called using Bitcoin nodes on Amazon Managed Blockchain.

## Considerations and limitations for

using Amazon Managed Blockchain (AMB) Access Bitcoin

- **Supported Bitcoin networks**

AMB Access Bitcoin supports the following public networks:

    + **Mainnet**—The public Bitcoin blockchain secured by
     proof-of-work consensus, and on which the Bitcoin (BTC) cryptocurrency is issued and
     transacted. Transactions on Mainnet have actual value (that is, they incur real costs) and
     are recorded on the public blockchain.
    + **Testnet**—The testnet is an alternative Bitcoin
     blockchain used for testing. Testnet coins are separate and distinct from actual Bitcoin
     (BTC) and do not usually have any value.

###### Note

Private networks aren't supported.

- **Supported Regions**

The following are the supported Regions for this service:

| Region name              | Code | Region         |
| ------------------------ | ---- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia)    | IAD  | `us-east-1`    |
| Asia Pacific (Tokyo)     | NRT  | ap-northeast-1 |
| Asia Pacific (Seoul)     | ICN  | ap-northeast-2 |
| Asia Pacific (Singapore) | SIN  | ap-southeast-1 |
| Europe (Ireland)         | DUB  | eu-west-1      |
| Europe (London)          | LHR  | eu-west-2      | <br>• **Service endpoints** The following are the service endpoints for AMB Access Bitcoin. To connect with the service, you must use an endpoint that includes one of the supported Regions. + `mainnet.bitcoin.managedblockchain.`Region`.amazonaws.com` + `testnet.bitcoin.managedblockchain.`Region`.amazonaws.com` For example: `mainnet.bitcoin.managedblockchain.eu-west-2.amazonaws.com` <br>• **Mining not supported** AMB Access Bitcoin does not support Bitcoin (BTC) mining. <br>• **Signature Version 4 signing of Bitcoin JSON-RPC calls** When making calls to the Bitcoin JSON-RPCs on Amazon Managed Blockchain, you can do so over an HTTPS connection authenticated using the [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). This means that only authorized IAM principals in the AWS account can make Bitcoin JSON-RPC calls. To do this, AWS credentials (an access key ID and a secret access key) must be provided with the call. ###### Important + Do not embed client credentials in user-facing applications. + You can't use IAM policies to restrict access to individual Bitcoin JSON-RPCs. <br>• **Only submissions of raw transactions are supported** Use the `sendrawtransaction` JSON-RPC to submit transactions that update the Bitcoin blockchain state. <br>• **AWS CloudTrail logging support** You can configure CloudTrail to log your Bitcoin JSON-RPCs. For more information, see [Logging Amazon Managed Blockchain (AMB) Access Bitcoin events by using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") |
