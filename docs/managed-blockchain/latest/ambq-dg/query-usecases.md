

# Use cases with Amazon Managed Blockchain (AMB) Query
<a name="query-usecases"></a>

This topic provides a list AMB Query use cases.

**Topics**
+ [Query current and historical token balances](#query-token-balances)
+ [Retrieve historical transaction data](#query-transactions)
+ [Get all token balances for a given address](#query-token-balances)
+ [List events emitted for a transaction](#query-tokens-minted)
+ [Get all tokens minted by a contract](#query-transaction-events)
+ [List contracts and get contract information](#query-contract-info)

## Query current and historical token balances
<a name="query-token-balances"></a>

The [`GetTokenBalance`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTokenBalance.html) API gets the balance of supported tokens (ERC20, ERC721, ERC1155) and native coins (ETH, BTC) to get the current or a historical balance by using a universal timestamp (Unix timestamp, in seconds) of externally owned accounts (EOAs). For example, you can use the `GetTokenBalance` API operation to get an address balance of the ERC20 token, USDC, on the Ethereum Mainnet. You can also batch-retrieve balances of tokens and native coins by using the `BatchGetTokenBalance` API operation.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html).

## Retrieve historical transaction data
<a name="query-transactions"></a>

With Amazon Managed Blockchain (AMB) Query, you can retrieve historical data from public blockchains such as Ethereum and Bitcoin. This features enables several use cases, such as retrieving a transaction history on a blockchain wallet or providing contextual information about a transaction based on its transaction hash. You can use the [`ListTransactions`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactions.html) API operation to get a list of transactions for a given externally owned address (EOA) on the Ethereum Mainnet, and then you can use the [`GetTransaction`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTransaction.html) API operation to retrieve the transaction details for a single transaction from the list. 

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html).

## Get all token balances for a given address
<a name="query-token-balances"></a>

You can use the [`ListTokenBalances`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTokenBalances.html) API operation to get balances on wallets, user interfaces, web3 utilities, and more. This API operation returns a list of all balances for an address across tokens (ERC20, ERC721, ERC1155) and native coins (ETH, BTC) on a given public blockchain by using a single API operation. For example, you can provide an externally owned address (EOA) and a network (the Ethereum Mainnet), and you can receive a list of tokens and native coin balances in the response.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html).

## List events emitted for a transaction
<a name="query-tokens-minted"></a>

You can use the [`ListTransactionEvents`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactionEvents.html) API operation to retrieve a list of contract events that are emitted as a result of a given transaction, identified by its hash (transaction identifier). For example, you can use [`ListTransactionEvents`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactionEvents.html) to retrieve the resulting events of a transaction that calls a function of an ERC20 token contract on the Ethereum Blockchain, such as a *Transfer* event or a *Withdrawal* event from the ERC20 contract.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html).

## Get all tokens minted by a contract
<a name="query-transaction-events"></a>

You can use the [`ListTokenBalances`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTokenBalances.html) API operation to return a list of all supported tokens (ERC20, ERC721, ERC1155) minted by a contract when passed the contract address as input. For example, you can retrieve information related to non-fungible tokens (NFTs) minted by the ERC721 contract standard on the Ethereum blockchain by using the [`ListTokenBalances`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTokenBalances.html) API operation.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html).

## List contracts and get contract information
<a name="query-contract-info"></a>

You can use the [`ListAssetContracts`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/ListAssetContracts.html) API operation to list ERC-721, ERC-1155, or ERC-20 contracts deployed by a given address. Additionally, if you have the contract address, you can use the [`GetAssetContract`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/ListAssetContracts.html) API operation to retrieve the contract's properties, such as the contract type deployer address, and relevant token metadata.

For more information, see the [Amazon Managed Blockchain (AMB) Query Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html).