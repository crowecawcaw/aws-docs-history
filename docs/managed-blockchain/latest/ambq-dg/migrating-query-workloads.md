

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Migrating Amazon Managed Blockchain Query Workloads
<a name="migrating-query-workloads"></a>

This guide covers moving applications from Amazon Managed Blockchain (AMB) Query to one of two managed blockchain data providers:
+ QuickNode for an API-oriented replacement path
+ Allium for a flexible Realtime API and query-oriented replacement path

The guide evaluates Ethereum Mainnet and Bitcoin Mainnet only. Ethereum Sepolia and Bitcoin Testnet are out of scope.

## This is not an endpoint-only migration
<a name="migrating-not-endpoint-only"></a>

AMB Query is a SigV4-authenticated, indexed API that returns normalized blockchain data, including transaction history, current and historical balances, token and contract information, and transaction events.

A standard Ethereum or Bitcoin node does not provide all of these indexed query capabilities. Third-party APIs in this document are not a drop-in, one-to-one replacement for every AMB Query response. Expect to do the following:
+ Replace SigV4 and the AWS SDK client with provider authentication and interfaces
+ Normalize provider fields into the application's expected data model
+ Combine related provider records for some AMB operations
+ Replace AMB pagination, ordering, confirmation, and error semantics
+ Validate the replacement against representative AMB responses before cutover

## Alternative data providers
<a name="migrating-alternative-providers"></a>

**Note**  
The following data provider options are non-exhaustive. These represent two alternatives in the market that provide strong coverage of the data returned by AMB Query APIs, but other providers might be able to support your specific data needs.

### Option 1: QuickNode (API-oriented migration)
<a name="migrating-quicknode"></a>

QuickNode is the better fit when the application prefers documented request/response APIs and low-latency synchronous access.

#### Ideal for customers that
<a name="migrating-quicknode-ideal"></a>
+ Operate wallet, explorer, transaction-monitoring, or application backends with synchronous requests
+ Prefer provider APIs over writing and operating saved data queries
+ Want most common balance, token, transaction, and address-history requests to follow direct or composed API paths
+ Can own additional derived data for the small number of AMB capabilities that do not have a direct equivalent

#### Typical use cases
<a name="migrating-quicknode-usecases"></a>

Displaying current wallet balances and holdings, looking up transactions by hash or ID, showing address transaction history, retrieving token and NFT metadata, and expanding a transaction into token transfers or Bitcoin inputs and outputs.

#### Where composition is needed
<a name="migrating-quicknode-composition"></a>
+ QuickNode does not provide a complete `GetAssetContract` response. Applications must supply their own heuristics to determine the token standard when provider metadata is insufficient.
+ Ethereum contracts by deployer require contract-creation history combined with token metadata.
+ Bitcoin events filtered by destination, time, and spent state can be composed from address history and transaction vout data.
+ Exact historical balances might require balance history combined with transaction or transfer history.
+ Complete Ethereum events might require transaction data, token transfers, logs, and internal native transfers from more than one source.

Customers must own the derived contract view needed for `ListAssetContracts`; Bitcoin historical spent-output filtering is a composed API path whose completeness and pagination still require live validation.

### Option 2: Allium (flexible data and query migration)
<a name="migrating-allium"></a>

Allium is the better fit when the application requires flexible access to provider-maintained blockchain datasets and can use a combination of Realtime APIs and Explorer queries.

#### Ideal for customers that
<a name="migrating-allium-ideal"></a>
+ Need complex historical, reconciliation, reporting, or data-enrichment queries
+ Have data engineering or analytics capabilities and are comfortable managing saved queries
+ Prefer querying provider-maintained datasets instead of operating their own blockchain indexes
+ Can tolerate asynchronous query execution or use planned caching/materialization for latency-sensitive paths

#### Typical use cases
<a name="migrating-allium-usecases"></a>

Historical wallet and asset reporting, contract discovery and classification, complex transaction-event reconstruction, Bitcoin UTXO and spent-output analysis, reconciliation, accounting, analytics, batch processing, and custom application views that combine several blockchain datasets.

#### Where composition is needed
<a name="migrating-allium-composition"></a>
+ Realtime fungible balances can be combined with historical and NFT balance datasets for complete ETH/ERC-20/ERC-721/ERC-1155 coverage.
+ Token metadata can be combined with contract deployment data to obtain the deployer and token standard.
+ Ethereum transactions can be combined with block and receipt data for the complete transaction response.
+ Ethereum transfers, traces, and decoded logs can be combined to reconstruct native, internal, token, NFT, and named contract events.
+ Bitcoin outputs can be combined with inputs to establish spent state and spending-transaction references.

Allium is the more flexible data-platform migration. It can express AMB gaps through provider-maintained datasets, but query execution and result delivery must meet the application's latency and availability requirements.

### Choosing between QuickNode and Allium
<a name="migrating-choosing"></a>

The following table compares QuickNode and Allium across the key considerations for a migration.


| Consideration | QuickNode | Allium | 
| --- | --- | --- | 
| Primary model | Provider APIs | Realtime APIs plus Explorer queries | 
| Best fit | Synchronous application backends | Flexible data, historical, and analytical workloads | 
| Common operations | More direct or bounded API compositions | Realtime APIs for common wallet operations | 
| Complex gaps | Customer-owned derived data might be required | Provider-maintained datasets can be combined through queries | 
| Latency model | Better aligned with request/response application traffic | Explorer-backed operations might be asynchronous | 
| Customer skill set | Application and API engineering | Data engineering, SQL, and query orchestration | 
| Operational tradeoff | Operate a small amount of derived data where required | Operate saved queries and potentially cache/materialize results | 

Choose QuickNode when predictable synchronous API access and a smaller application change are the priority. Choose Allium when flexible access to complete provider-maintained datasets is more important than having a direct endpoint for each AMB operation.

## AMB Query API and tool mapping
<a name="migrating-api-mapping"></a>

The following table identifies the documented APIs or provider tools that can supply each part of an AMB Query response. The composition notes explain which records must be related, but intentionally do not prescribe storage, schemas, query text, or implementation for custom joins or compositions of multiple responses. API and product availability can vary by plan.


| AMB Query operation | Data needed | QuickNode API or tool | Allium API or tool | 
| --- | --- | --- | --- | 
| BatchGetTokenBalance | Independent balances or errors for each owner, asset, token ID, network, and requested instant | Ethereum: qn\_getWalletTokenBalance, qn\_fetchNFTs, EVM Blockbook Address/Balance History. Bitcoin: BTC Blockbook Address/Balance History. Group compatible calls and match each result or error to its AMB input. | Realtime Latest Fungible Token Balances and Historical Fungible Token Balances; NFT Tokens by User or Explorer query for NFT quantities. Combine by owner, asset, token ID, and requested instant. | 
| GetAssetContract | Contract address, network, deployer, token standard, name, symbol, and decimals | qn\_getTokenMetadataByContractAddress and qn\_fetchNFTCollectionDetails. Use EVM Blockbook data only to determine the deployer. Application-owned heuristics must determine the token standard when provider metadata is insufficient. | Tokens API Get Tokens and NFT API NFT Contract, combined with Explorer query over contract deployment data for the deployer. | 
| GetTokenBalance | Exact current or historical balance for one owner and asset, including NFT token ID | Ethereum: qn\_getWalletTokenBalance, qn\_verifyNFTsOwner, qn\_fetchNFTs, EVM Blockbook Address/Balance History. Bitcoin: BTC Blockbook Address/Balance History. | Realtime Latest Fungible Token Balances or Historical Fungible Token Balances; Explorer query for ERC-721/1155 and exact historical selection. | 
| GetTransaction | Transaction and block identity, timestamp, status, parties, fees, execution/receipt fields, and chain-specific identifiers | EVM Blockbook Transaction (bb\_getTx) for Ethereum; BTC Blockbook Transaction for Bitcoin. Combine with block context when required AMB fields are absent. | Wallet API Transactions for common fields; Explorer query combining transaction, block, receipt, or Bitcoin input/output data for the complete response. | 
| ListAssetContracts | Complete token contracts filtered by deployer and token standard | No direct QuickNode API. Compose contract-creation records from EVM Blockbook Address/Transaction data plus Token/NFT metadata APIs. | Explorer query combining provider-maintained contract deployment data with ERC-20, ERC-721, and ERC-1155 token metadata, filtered by deployer and standard. | 
| ListFilteredTransactionEvents | Bitcoin outputs filtered by destination, time, and spent state | No single BTC Blockbook endpoint applies the complete AMB filter. Use bb\_getAddress to enumerate transactions and bb\_getTx for full vin/vout. bb\_getUTXOs returns only currently unspent references. | Explorer query combining provider-maintained Bitcoin output and input data, applying destination, time, and spent-state filters. | 
| ListTokenBalances | Complete current native, fungible, ERC-721, and ERC-1155 holdings with stable identities | Ethereum: qn\_getWalletTokenBalance, qn\_fetchNFTs, EVM Blockbook Address for native ETH. Bitcoin: BTC Blockbook Address. Combine and deduplicate holdings. | Realtime Latest Fungible Token Balances, NFT API NFT Tokens by User, and Explorer query for complete NFT quantities or unified pagination. | 
| ListTransactionEvents | Ethereum native/internal/token/NFT events or Bitcoin inputs/outputs for one transaction | Ethereum: EVM Blockbook Transaction, qn\_getWalletTokenTransactions, qn\_getTransfersByNFT. Bitcoin: BTC Blockbook Transaction expanded into input/output events. | Wallet API Transactions, Tokens API Transfers, NFT activity APIs, and Explorer query combining transfers, traces, decoded logs, or Bitcoin inputs/outputs. | 
| ListTransactions | Complete address history with timestamps, status/finality, ordering, and pagination | Ethereum: qn\_getTransactionsByAddress or EVM Blockbook Address (bb\_getAddress). Bitcoin: BTC Blockbook Address. | Wallet API Transactions for Ethereum and Bitcoin; Explorer query for broad or highly filtered historical windows. | 

## Important parity boundaries
<a name="migrating-parity-boundaries"></a>

Before migrating, verify that the target provider replicates exact AMB behavior or achieves parity adequate for your use case. Do not choose a provider as a replacement until your required AMB test fixtures pass. Validate the following:
+ New provider surfaces every field your application requires
+ Exact historical timestamp boundaries
+ Native, fungible, ERC-721, and ERC-1155 balance units
+ Ethereum successful, failed, and contract-creation transactions
+ Ethereum signature and receipt fields where required
+ Bitcoin transaction ID versus witness transaction hash semantics
+ Bitcoin spent and unspent output relationships
+ Inclusive time filters, sorting, and pagination without gaps or duplicates
+ Confirmation/finality and blockchain reorganization behavior
+ Data freshness, request/query latency, rate limits, and plan entitlement

## Migration steps
<a name="migrating-steps"></a>

Use the following steps to plan, build, and complete your migration.

### Step 1: Inventory the existing workload
<a name="migrating-step-inventory"></a>

Document the application's current use of AMB Query:
+ Ethereum Mainnet and Bitcoin Mainnet operations in use
+ Current and historical data requirements
+ Transaction, address, balance, token, contract, and event queries
+ Fields actually consumed by the application
+ Filters, sorting, pagination, and batch behavior
+ Request volume, concurrency, and latency objectives
+ Confirmation and finality rules
+ Data retention and export requirements
+ Downstream schemas and consumers

This inventory determines whether QuickNode's API-oriented model or Allium's query-oriented model is the better fit. Customers do not need to reproduce unused AMB operations.

### Step 2: Evaluate provider fit
<a name="migrating-step-evaluate"></a>

#### Choose QuickNode when
<a name="migrating-step-evaluate-quicknode"></a>
+ Most required operations map to synchronous APIs
+ Request latency is more important than query flexibility
+ The application team prefers API integration over saved SQL
+ The customer accepts ownership of the derived data required by its specific gaps

#### Choose Allium when
<a name="migrating-step-evaluate-allium"></a>
+ The workload requires complex historical or cross-dataset composition
+ Asynchronous queries are acceptable for some operations
+ The customer wants the provider to maintain the underlying indexed datasets
+ The customer can manage saved queries and a result-delivery or caching strategy

### Step 3: Modify the application
<a name="migrating-step-modify"></a>

#### Replace the AMB Query client
<a name="migrating-step-modify-client"></a>

Remove AWS SDK clients and commands associated with AMB Query. Integrate QuickNode's APIs or Allium's Realtime and Explorer interfaces.

#### Replace authentication
<a name="migrating-step-modify-auth"></a>

Remove AMB Query SigV4 signing. Store provider credentials in a secrets manager and use the provider's documented authentication mechanism. Do not remove AWS credentials or IAM permissions that the application still needs for other AWS services.

#### Translate data models
<a name="migrating-step-modify-datamodels"></a>

Normalize differences in network and token identifiers, transaction fields and status values, timestamps and time zones, numeric encoding and token decimals, confirmation and finality states, missing and optional fields, and error responses. Use exact string or arbitrary-precision numeric handling for blockchain values; do not use binary floating point.

#### Replace pagination and sorting
<a name="migrating-step-modify-pagination"></a>

The opaque `nextToken` in AMB Query might become a provider cursor or a query-result continuation. Keep provider-specific pagination inside the adapter and expose stable application-owned cursors and ordering.

#### Isolate provider-specific logic
<a name="migrating-step-modify-isolate"></a>

Keep authentication, query orchestration, pagination, normalization, and provider-specific errors inside an adapter layer. This reduces application changes and makes future provider transitions easier. This is also useful in cases where multiple data providers are required to address your use case.

### Step 4: Validate the replacement
<a name="migrating-step-validate"></a>

Use representative, finalized Ethereum Mainnet and Bitcoin Mainnet data covering the following:
+ Recent and historical transactions
+ High-activity addresses
+ Current and historical balances
+ Native ETH and BTC
+ ERC-20, ERC-721, and ERC-1155 assets
+ Bitcoin spent and unspent outputs
+ Contract deployments and token metadata
+ Successful, failed, and contract-creation transactions
+ Multi-page query results
+ Transactions near and beyond the application's finality threshold

Compare normalized provider output with captured AMB responses for the following:
+ Record completeness
+ Exact balances, values, and fees
+ Timestamps and historical boundaries
+ Transaction and execution status
+ Confirmation and finality state
+ Sorting and pagination
+ Historical coverage
+ Data freshness and latency

If AMB Query remains available, run both paths in parallel. Otherwise, replay the captured AMB baseline fixtures. Near-tip results might legitimately differ because of indexing delay or blockchain reorganizations; use finalized data or a fixed confirmation depth for correctness comparisons.

### Step 5: Cut over safely
<a name="migrating-step-cutover"></a>

Cut over to the replacement provider gradually by following these steps.

1. Complete provider integration and baseline validation.

1. Resolve every required field or explicitly remove the dependency.

1. Run both paths in parallel where AMB Query remains available.

1. Route a small percentage of eligible query traffic to the replacement.

1. Monitor correctness, latency, errors, quotas, and indexing lag.

1. Gradually increase replacement traffic.

1. Retain the AMB Query integration as a rollback path during the soak period.

1. After successful validation, remove unused AMB Query dependencies and IAM permissions.

## References
<a name="migrating-references"></a>

For more information, see the following resources.
+ [AMB Query API operations](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Operations.html)
+ [AMB Query setup and SigV4 authentication](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/ambq-setting-up.html)
+ [AWS Blockchain Node Runners](https://github.com/aws-samples/aws-blockchain-node-runners)
+ [QuickNode Ethereum documentation](https://www.quicknode.com/docs/ethereum)
+ [QuickNode Bitcoin Blockbook](https://www.quicknode.com/docs/bitcoin/blockbook/overview)
+ [Allium Realtime APIs](https://docs.allium.so/api/developer/overview)
+ [Allium Explorer API](https://docs.allium.so/api/explorer/overview)
+ [Allium historical data](https://docs.allium.so/historical-data/overview)