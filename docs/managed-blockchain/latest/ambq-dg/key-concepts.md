# Key concepts: Amazon Managed Blockchain (AMB) Query

###### Note

This guide assumes that you're familiar with essential blockchain concepts.
These concepts include decentralization, tokens, contracts, transactions, proof-of-work,
wallets, public and private keys, staking, mining, halvings, and others.

Amazon Managed Blockchain (AMB) Query provides you with convenient access to multi-blockchain network data, which makes
it easier for you to extract contextual data related to blockchain activity. You can use AMB Query
to read data from public blockchain networks, such as Bitcoin Mainnet and Ethereum Mainnet. You
can also get information, such as current and historical balances of addresses, or you can get a
list of blockchain transactions for a given time period. Additionally, you can get details of a
given transaction, such as transaction events, which you can further analyze or use in business
logic for your applications.

## Considerations and limitations for

using Amazon Managed Blockchain (AMB) Query

When you use AMB Query, consider the following:

- **Available Regions**

AMB Query is supported in the _US East (N. Virginia)_ `us-east-1` Region.

- **Service endpoints**

AMB Query is accessible by using the following endpoint:

`https://managedblockchain-query.us-east-1.amazonaws.com`.

- **Supported blockchain networks**

AMB Query supports the following public blockchain networks:

    + **Bitcoin Mainnet** — The public Bitcoin blockchain network
     that is secured by proof-of-work consensus, and on which the Bitcoin (BTC)
     cryptocurrency is issued and transacted. Transactions on Mainnet have actual value
     (that is, they incur real costs) and are recorded on the public blockchain.
    + **Bitcoin Testnet** — The testnet for the Bitcoin
     Mainnet. Bitcoin (BTC) on this network is separate and distinct from Mainnet BTC, and
     does not usually have any value.
    + **Ethereum Mainnet** — The proof-of-stake main network for
     the public Ethereum blockchain. Transactions on Mainnet have actual value (that is,
     they incur real costs) and are recorded on the distributed ledger.
    + **Sepolia Testnet** — The testnet for the Ethereum
     Mainnet. Ether (ETH) on this network is separate and distinct from Mainnet ETH, and
     does not usually have any value.

- **Supported blockchain tokens and contracts**

AMB Query supports the following native and standard Ethereum contract tokens.

    + **Public blockchain native tokens**




    	- **Bitcoin (BTC)**— This is the native token of
    	 Bitcoin-related blockchains.
    	- **Ether (ETH)**— This is the native token of
    	 Ethereum-related blockchains.
    + **Ethereum contract standards**




    	- **ERC-20 Token Standard** — The ERC-20 is a standard
    	 for fungible tokens. It has a property that makes each ERC-20 token exactly the
    	 same (in type and value) as another ERC-20 token minted, which means that one
    	 token is and will always be equal to all the other tokens. For more information,
    	 see the [ERC-20 Token
    	 Standard](https://eips.ethereum.org/EIPS/eip-20 "https://eips.ethereum.org/EIPS/eip-20") on Ethereum.org.
    	- **ERC-721 Non-fungible Token Standard** — The
    	 ERC-721 is a standard for non-fungible tokens (NFTs). This type of token is unique and can
    	 have a different value than another token from the same contract, possibly due to its
    	 age, rarity, or other properties. For more information, see the [ERC-721 Token
    	 Standard](https://eips.ethereum.org/EIPS/eip-721 "https://eips.ethereum.org/EIPS/eip-721") on Ethereum.org.


    	**ERC-1155 Multi-token Standard** — The ERC-1155 is
    	 a standard that creates a contract interface that can represent and control any
    	 number of fungible and non-fungible token types. In this way, the ERC-1155 token
    	 can function the same as [ERC-20](https://eips.ethereum.org/EIPS/eip-20 "https://eips.ethereum.org/EIPS/eip-20") and [ERC-721](https://eips.ethereum.org/EIPS/eip-721 "https://eips.ethereum.org/EIPS/eip-721") tokens, even functioning as both at the same time. The ERC-1155
    	 token improves on the functionality of both the ERC-20 and ERC-721 standards,
    	 making it more efficient, while correcting obvious implementation errors. For more
    	 information, see the [ERC-1155
    	 Token Standard](https://eips.ethereum.org/EIPS/eip-1155 "https://eips.ethereum.org/EIPS/eip-1155") on Ethereum.org.

- **Finality**

In blockchains, _finality_ means that valid transactions are unlikely
to be reversed. For the Bitcoin Mainnet, AMB Query considers a transaction final after 6 blocks.
For the Bitcoin Testnet, it considers a transaction final after either 6 blocks or 60 minutes,
whichever comes first. For supported Ethereum networks, AMB Query considers a transaction
final after 64 blocks.

AMB Query's token balance and contract API operations only return data that has reached ﬁnality.
However, AMB Query's transaction and transaction event API operations can return data for transactions
that are confirmed on the blockchain network even if they have not yet reached finality.

- **NULL address not supported**

AMB Query does not support the `NULL` (`0x0000000000000000000000000000000000000000`) address.

- **Signature Version 4 signing of API calls**

When making calls to the AMB Query APIs, you
can do so over an HTTPS connection authenticated using the [Signature Version 4 signing
process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). This means that only authorized IAM principals in the AWS
account can make AMB Query API calls. To do this, AWS credentials
(an access key ID and secret access key) must be provided with the call.

###### Important

Do not embed client credentials in user-facing applications.

- **AMB Query supports Bitcoin
  transaction identifiers and transaction hashes**

For Bitcoin networks, AMB Query API operations support both the transaction identifier
(`transactionId`) and the transaction hash (`transactionHash`). The
`transactionId` is a double-SHA hash of the transaction not including
witness data. The `transactionHash` is a double-SHA hash of the transaction including
witness data (also known as witness transaction id).

When invoking the [`GetTransaction`](../AMBQ-APIReference/API_GetTransaction.md "../AMBQ-APIReference/API_GetTransaction.md") or [`ListTransactionEvents`](../AMBQ-APIReference/API_ListTransactions.md "../AMBQ-APIReference/API_ListTransactions.md") API operations for Bitcoin networks, you
can specify either the `transactionId` or the `transactionHash`.
Also, all AMB Query operations on Bitcoin networks that return either a
`transactionId` or a `transactionHash` will include both values as
a part of the response.
