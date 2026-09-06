

# Supported JSON-RPC methods
<a name="supported-json-rpc"></a>

Amazon Managed Blockchain (AMB) Access Ethereum supports the following Ethereum JSON-RPC API methods. Each supported API call has a brief description of its utility. Unique considerations for using the JSON-RPC method with an Ethereum node in Amazon Managed Blockchain (AMB) are indicated where applicable.

**Note**  
Ethereum API calls to an Ethereum node in Amazon Managed Blockchain (AMB) can be authenticated by using the [Signature Version 4 (SigV4) signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account that created the node can interact with it using the Ethereum APIs. AWS credentials (an access key ID and secret access key) must be provided with the call.
Token based access can also be used to make Ethereum API calls to an Ethereum node as a convenient alternative to the Signature Version 4 (SigV4) signing process. If you prioritize security and auditability over convenience, use the SigV4 signing process instead. However, if you use token based access to make Ethereum APIs calls, any security benefits that are provided by using the SigV4 signing process is negated.
JSON-RPC batch requests aren't supported on Amazon Managed Blockchain (AMB) Access Ethereum.
WebSocket calls have a 512 KB payload quota. Some calls might exceed this quota and cause a "message response is too large" error. For this reason, we recommend you use HTTP for these requests instead of WebSocket connections.
If your HTTP response is larger than 5.9 MB, you will get an error. To correct this, you must set both compression headers as `Accept: application/gzip` and `Accept-Encoding: gzip`. The compressed response your client then receives contains the following headers: ` Content-Type: application/json` and `Content-Encoding: gzip`.
For historic data that requires archival nodes, use Amazon Managed Blockchain (AMB) Query. For more information, see the *[AMB Query Developer Guide](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg)*.

**Topics**
+ [Making JSON-RPC API calls to an Ethereum node in Amazon Managed Blockchain (AMB)](json-rpc-api-examples.md)

**The block identifier parameter**

Some methods have an extra block identifier parameter. The following options are possible values for this parameter:
+ A hexadecimal string value that represents an integer block number.
+ `"earliest"` – String for the genesis block.
+ `"latest"` – String for the latest mined block.
+ `"pending"` – String for the pending state transactions.


| Method | Description | Considerations | 
| --- | --- | --- | 
| [debug\_traceBlock](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug#debugtraceblock) | Returns the full stack trace of all the invoked opcodes for all the transactions that were included in the block provided as a parameter in RLP format. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [debug\_traceBlockByHash](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug#debugtraceblockbyhash) | Returns the full stack trace of all the transactions that were included in a specified block by its hash. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [debug\_traceBlockByNumber](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug#debugtraceblockbynumber) | Returns the full stack trace of all the transactions that were included in the specified block number. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [debug\_traceCall](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug#debugtracecall) | Returns the full stack trace after running an eth\_call within the context of the given block execution. The method is also used to simulate the outcomes of transactions and supports custom tracers. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [debug\_traceTransaction](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug#debugtracetransaction) | Attempts to return all traces for a given transaction. |  | 
| [eth\_blockNumber](https://eth.wiki/json-rpc/API#eth_blocknumber) | Returns the number of the most recent block. |  | 
| [eth\_call](https://eth.wiki/json-rpc/API#eth_call) | Immediately runs a new message call without creating a transaction on the blockchain. | eth\_call consumes 0 gas, but has a gas parameter for messages that require it. Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| eth\_chainId | Returns an integer value for the currently configured Chain Id value that's introduced in [EIP-155](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md). Returns None if no Chain Id is available. |  | 
| eth\_createAccessList | This method creates an [EIP2930](https://eips.ethereum.org/EIPS/eip-2930) type accessList based on a given Transaction. The accessList contains all the storage slots and addresses read and written by the transaction, except for the sender account and the precompiles. This method uses the same transaction call object and blockNumberOrTag object as eth\_call. | An accessList can be used to unstuck contracts that became inaccessible due to gas cost increases. | 
| [eth\_estimateGas](https://eth.wiki/json-rpc/API#eth_estimategas) | Estimates and returns the gas that's required for a transaction without adding the transaction to the blockchain. |  | 
| eth\_feeHistory | Returns a collection of historical gas information. |  | 
| [eth\_gasPrice](https://eth.wiki/json-rpc/API#eth_gasprice) | Returns the current price per gas in Wei. |  | 
| [eth\_getBalance](https://eth.wiki/json-rpc/API#eth_getbalance) | Returns the balance of an account for the specified account address and block identifier. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [eth\_getBlockByHash](https://eth.wiki/json-rpc/API#eth_getblockbyhash) | Returns information about the block specified using the block hash. |  | 
| [eth\_getBlockByNumber](https://eth.wiki/json-rpc/API#eth_getblockbynumber) | Returns information about the block specified using the block number. |  | 
| [eth\_getBlockTransactionCountByHash](https://eth.wiki/json-rpc/API#eth_getblocktransactioncountbyhash) | Returns the number of transactions in the block specified using the block hash. |  | 
| [eth\_getBlockTransactionCountByNumber](https://eth.wiki/json-rpc/API#eth_getblocktransactioncountbynumber) | Returns the number of transactions in the block specified using the block number. |  | 
| [eth\_getCode](https://eth.wiki/json-rpc/API#eth_getcode) | Returns the code at the specified account address and block identifier. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [eth\_getFilterChanges](https://eth.wiki/json-rpc/API#eth_getfilterchanges) | Polls the specified filter ID, retuning an array of logs that occurred since the last poll. | Filters are ephemeral. If AMB Access needs to manage or maintain node instances for availability and performance, and an instance is replaced, filters might be deleted. We recommend that you write your application code to handle the occasional deletion of filters. | 
| [eth\_getFilterLogs](https://eth.wiki/json-rpc/API#eth_getfilterlogs) | Returns an array of all logs for the specified filter ID. | Filters are ephemeral. If AMB Access needs to manage or maintain node instances for availability and performance, and an instance is replaced, filters might be deleted. We recommend that you write your application code to handle the occasional deletion of filters. | 
| [eth\_getLogs](https://eth.wiki/json-rpc/API#eth_getlogs) | Returns an array of all logs for a specified filter object. | Filters are ephemeral. If AMB Access needs to manage or maintain node instances for availability and performance, and an instance is replaced, filters might be deleted. We recommend that you write your application code to handle the occasional deletion of filters. | 
| eth\_getProof | Experimental – Returns the account and storage values of the specified account, including the Merkle proof. |  | 
| [eth\_getStorageAt](https://eth.wiki/json-rpc/API#eth_getstorageat) | Returns the value of the specified storage position for the specified account address and block identifier. | Only data for the most recent 128 blocks is supported. Archival data is not supported. | 
| [eth\_getTransactionByBlockHashAndIndex](https://eth.wiki/json-rpc/API#eth_gettransactionbyblockhashandindex) | Returns information about a transaction using the specified block hash and transaction index position. |  | 
| [eth\_getTransactionByBlockNumberAndIndex](https://eth.wiki/json-rpc/API#eth_gettransactionbyblocknumberandindex) | Returns information about a transaction using the specified block number and transaction index position. |  | 
| [eth\_getTransactionByHash](https://eth.wiki/json-rpc/API#eth_gettransactionbyhash) | Returns information about the transaction with the specified transaction hash. |  | 
| [eth\_getTransactionCount](https://eth.wiki/json-rpc/API#eth_gettransactioncount) | Returns the number of transactions sent from the specified address and block identifier. |  | 
| [eth\_getTransactionReceipt](https://eth.wiki/json-rpc/API#eth_gettransactionreceipt) | Returns the receipt of the transaction using the specified transaction hash. |  | 
| [eth\_getUncleByBlockHashAndIndex](https://eth.wiki/json-rpc/API#eth_getunclebyblockhashandindex) | Returns information about the uncle block specified using the block hash and uncle index position. |  | 
| [eth\_getUncleByBlockNumberAndIndex](https://eth.wiki/json-rpc/API#eth_getunclebyblocknumberandindex) | Returns information about the uncle block specified using the block number and uncle index position. |  | 
| [eth\_getUncleCountByBlockHash](https://eth.wiki/json-rpc/API#eth_getunclecountbyblockhash) | Returns the number of counts in the uncle specified using the uncle hash. |  | 
| [eth\_getUncleCountByBlockNumber](https://eth.wiki/json-rpc/API#eth_getunclecountbyblocknumber) | Returns the number of counts in the uncle specified using the uncle number. |  | 
| [eth\_getWork](https://eth.wiki/json-rpc/API#eth_getwork) | Returns the hash of the current block, the seedHash, and the boundary condition (also called the "target") to be met. |  | 
| eth\_maxPriorityFeePerGas | Returns the fee per gas that's an estimate of how much you can pay as a priority fee, or "tip," to get a transaction included in the current block. | Generally you use the value that's returned from this method to set the maxFeePerGas in the subsequent transaction that you're submitting. | 
| [eth\_newBlockFilter](https://eth.wiki/json-rpc/API#eth_newblockfilter) | Creates a filter in the node to notify when a new block arrives. Use eth\_getFilterChanges to check for state changes. |  | 
| [eth\_newFilter](https://eth.wiki/json-rpc/API#eth_newfilter) | Creates a filter object with the specified filter options (such as from block, to block, contract address, or topics). |  | 
| [eth\_newPendingTransactionFilter](https://eth.wiki/json-rpc/API#eth_newpendingtransactionfilter) | Creates a filter in the node to notify when new pending transactions arrive. Use <code>eth\_getFilterChanges</code> to check for state changes. |  | 
| [eth\_protocolVersion](https://eth.wiki/json-rpc/API#eth_protocolversion) | Returns the current Ethereum protocol version. |  | 
| [eth\_sendRawTransaction](https://eth.wiki/json-rpc/API#eth_sendrawtransaction) | Creates a new message call transaction or a contract creation for signed transactions.  | AMB Access supports raw transactions only. You must create and sign transactions before sending them. For more information, see [How to create raw transactions in Ethereum](https://medium.com/blockchain-musings/how-to-create-raw-transactions-in-ethereum-part-1-1df91abdba7c). | 
| [eth\_subscribe](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub) | Experimental for publication subscription – Creates a subscription for specified events and returns a subscription ID.  | Available only when using WebSocket connections. Subscriptions are coupled to each connection. When the connection closes, the subscription is removed. | 
| [eth\_syncing](https://eth.wiki/json-rpc/API#eth_syncing) | Returns an object with sync status data or false when not syncing. |  | 
| [eth\_uninstallFilter](https://eth.wiki/json-rpc/API#eth_uninstallfilter) | Uninstalls the filter with the specified filter ID. |  | 
| [eth\_unsubscribe](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub#cancel-subscriptions) | Experimental for publication subscription – Cancels the subscription with the specified subscription ID. |  | 
| [net\_listening](https://eth.wiki/json-rpc/API#net_listening) | Returns true if the client is actively listening for network connections. |  | 
| [net\_peerCount](https://eth.wiki/json-rpc/API#net_peercount) | Returns the number of peers currently connected to the client. |  | 
| [net\_version](https://eth.wiki/json-rpc/API#net_version) | Returns the current network ID. |  | 
| [txpool\_inspect](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-txpool#txpool-inspect) | Lists a textual summary of all the transactions that are currently pending inclusion in the next blocks, and those that are queued (being scheduled for future execution only). |  | 
| [txpool\_status](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-txpool#txpool-status) | Provides a count of all transactions currently pending inclusion in the next blocks, and those that are queued (being scheduled for future execution only). |  | 
| [web3\_clientVersion](https://eth.wiki/json-rpc/API#web3_clientversion) | Returns the current client version. |  | 
| [web3\_sha3](https://eth.wiki/json-rpc/API#web3_sha3) | Returns Keccak-256 (not the standardized SHA3-256) of the given data. |  | 