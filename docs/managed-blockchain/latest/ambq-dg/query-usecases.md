# Use cases with Amazon Managed Blockchain (AMB) Query

This topic provides a list AMB Query use cases.

###### Topics

- [Query current and historical
  token balances](#query-token-balances "#query-token-balances")
- [Retrieve historical transaction data](#query-transactions "#query-transactions")
- [Get all token balances for
  a given address](#query-token-balances "#query-token-balances")
- [List events emitted for a transaction](#query-tokens-minted "#query-tokens-minted")
- [Get all tokens minted by a
  contract](#query-transaction-events "#query-transaction-events")
- [List contracts and get contract
  information](#query-contract-info "#query-contract-info")

## Query current and historical

token balances

The [`GetTokenBalance`](../AMBQ-APIReference/API_GetTokenBalance.md "../AMBQ-APIReference/API_GetTokenBalance.md") API gets the balance of supported tokens (ERC20,
ERC721, ERC1155) and native coins (ETH, BTC) to get the current or a historical balance by
using a universal timestamp (Unix timestamp, in seconds) of externally owned accounts (EOAs).
For example, you can use the `GetTokenBalance` API operation to get an address
balance of the ERC20 token, USDC, on the Ethereum Mainnet. You can also batch-retrieve
balances of tokens and native coins by using the `BatchGetTokenBalance` API
operation.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](../AMBQ-APIReference/Welcome.md "../AMBQ-APIReference/Welcome.md").

## Retrieve historical transaction data

With Amazon Managed Blockchain (AMB) Query, you can retrieve historical data from public blockchains such as
Ethereum and Bitcoin. This features enables several use cases, such as retrieving a
transaction history on a blockchain wallet or providing contextual information about a
transaction based on its transaction hash. You can use the [`ListTransactions`](../AMBQ-APIReference/API_ListTransactions.md "../AMBQ-APIReference/API_ListTransactions.md") API operation to get a list of transactions for a
given externally owned address (EOA) on the Ethereum Mainnet, and then you can use the [`GetTransaction`](../AMBQ-APIReference/API_GetTransaction.md "../AMBQ-APIReference/API_GetTransaction.md") API operation to retrieve the transaction details for
a single transaction from the list.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](../AMBQ-APIReference/Welcome.md "../AMBQ-APIReference/Welcome.md").

## Get all token balances for

a given address

You can use the [`ListTokenBalances`](../AMBQ-APIReference/API_ListTokenBalances.md "../AMBQ-APIReference/API_ListTokenBalances.md") API operation to get balances on wallets, user
interfaces, web3 utilities, and more. This API operation returns a list of all balances for an
address across tokens (ERC20, ERC721, ERC1155) and native coins (ETH, BTC) on a given public
blockchain by using a single API operation. For example, you can provide an externally owned
address (EOA) and a network (the Ethereum Mainnet), and you can receive a list of tokens and
native coin balances in the response.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](../AMBQ-APIReference/Welcome.md "../AMBQ-APIReference/Welcome.md").

## List events emitted for a transaction

You can use the [`ListTransactionEvents`](../AMBQ-APIReference/API_ListTransactionEvents.md "../AMBQ-APIReference/API_ListTransactionEvents.md") API operation to retrieve a list of contract
events that are emitted as a result of a given transaction, identified by its hash
(transaction identifier). For example, you can use [`ListTransactionEvents`](../AMBQ-APIReference/API_ListTransactionEvents.md "../AMBQ-APIReference/API_ListTransactionEvents.md") to retrieve the resulting events of a
transaction that calls a function of an ERC20 token contract on the Ethereum Blockchain, such
as a _Transfer_ event or a _Withdrawal_ event from the ERC20 contract.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](../AMBQ-APIReference/Welcome.md "../AMBQ-APIReference/Welcome.md").

## Get all tokens minted by a

contract

You can use the [`ListTokenBalances`](../AMBQ-APIReference/API_ListTokenBalances.md "../AMBQ-APIReference/API_ListTokenBalances.md") API operation to return a list of all supported
tokens (ERC20, ERC721, ERC1155) minted by a contract
when
passed the contract address as input. For example, you can retrieve
information related to non-fungible tokens (NFTs) minted by the ERC721 contract standard on
the Ethereum blockchain by using the [`ListTokenBalances`](../AMBQ-APIReference/API_ListTokenBalances.md "../AMBQ-APIReference/API_ListTokenBalances.md") API operation.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](../AMBQ-APIReference/Welcome.md "../AMBQ-APIReference/Welcome.md").

## List contracts and get contract

information

You can use the [`ListAssetContracts`](../AMBQ-APIReference/ListAssetContracts.md "../AMBQ-APIReference/ListAssetContracts.md") API operation to list ERC-721, ERC-1155,
or ERC-20 contracts deployed by a given address. Additionally, if you have the contract
address, you can use the [`GetAssetContract`](../AMBQ-APIReference/ListAssetContracts.md "../AMBQ-APIReference/ListAssetContracts.md") API operation to retrieve the contract's
properties, such as the contract type deployer address, and relevant token metadata.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](../AMBQ-APIReference/Welcome.md "../AMBQ-APIReference/Welcome.md").
