

Amazon Managed Blockchain (AMB) Access Polygon is in preview release and is subject to change.

# Managed Blockchain API and the JSON-RPCs supported with AMB Access Polygon
<a name="polygon-api"></a>

Amazon Managed Blockchain provides API operations for [creating and managing token accessors ](https://docs.aws.amazon.com/managed-blockchain/latest/ambp-dg/polygon-tokens.html)for AMB Access Polygon. For more information, see the * [Managed Blockchain API Reference Guide](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/Welcome.html) *.

The following topic provides a list and reference of the Polygon JSON-RPCs that AMB Access Polygon supports. Each supported JSON-RPC has a brief description of its use. You use the Polygon JSON-RPCs to query and get smart contract data, get transaction details, submit transactions, and other utilities such as running traces on transactions, and estimate fees. 

AMB Access Polygon supports the following JSON-RPC methods. Each supported JSON-RPC has a category and a brief description of its utility and its default request quotas. Unique considerations for using the JSON-RPC method with Amazon Managed Blockchain are indicated where applicable.

**Note**  
Any methods that aren't listed are not supported.
When making calls to the Polygon JSON-RPCs on Amazon Managed Blockchain, you can do so over an HTTPS connection authenticated using the [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account can make Polygon JSON-RPC calls. To do this, AWS credentials (an access key ID and a secret access key) must be provided with the call.
You can also use token-based access as a convenient alternative to the Signature Version 4 (SigV4) signing process. If you prioritize security and auditability over convenience, use the SigV4 signing process instead. However, if you use both SigV4 and token-based access, your requests will not work.
JSON-RPC batch requests aren't supported on Amazon Managed Blockchain (AMB) Access Polygon for this preview.
The **Quotas** column in the following table lists the quota for each JSON-RPC. Quotas are set in requests per second (RPS) per Region per Polygon network (Mainnet) for each JSON-RPC.   
For increasing your quota, you must contact Support. To contact Support, sign into the [AWS Support Center Console](https://console.aws.amazon.com/support). Choose **Create case**. Choose **Technical**. Choose *Managed Blockchain* as your **service**. Choose *Access:Polygon* as your **Category** and *General guidance* as your **Severity**. Enter *RPC Quota* as the **Subject** and in the **Description** text box list the JSON-RPC and the quota limits applicable to your needs in *RPS per Polygon network per Region*. **Submit** your case. 

**Topics**



- **Ethereum**
  - **JSON-RPC:** eth\_blockNumber / **Description:** Returns the number of the most recent block. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_call / **Description:** Immediately runs a new message call without creating a transaction on the blockchain. / **Quota:** 100 / **Considerations:** eth\_call consumes 0 gas, but has a gas parameter for messages that require it. 
  - **JSON-RPC:** eth\_chainId / **Description:** Returns an integer value for the currently configured Chain Id value that's introduced in [EIP-155](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md). Returns None if no Chain Id is available. / **Quota:** 300 / **Considerations:** 
  - **JSON-RPC:** eth\_estimateGas / **Description:** Estimates and returns the gas that's required for a transaction without adding the transaction to the blockchain. / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** eth\_feeHistory / **Description:** Returns a collection of historical gas information. / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** eth\_gasPrice / **Description:** Returns the current price per gas in Wei. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getBalance / **Description:** Returns the balance of an account for the specified account address and block identifier. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getBlockByHash / **Description:** Returns information about the block specified using the block hash. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getBlockByNumber / **Description:** Returns information about the block specified using the block number. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getBlockReceipts / **Description:** Returns receipts about the block specified using the block number. / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** eth\_getBlockTransactionCountByHash / **Description:** Returns the number of transactions in the block specified using the block hash. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getBlockTransactionCountByNumber / **Description:** Returns the number of transactions in the block specified using the block number. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getCode / **Description:** Returns the code at the specified account address and block identifier. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getLogs / **Description:** Returns an array of all logs for a specified filter object. / **Quota:** 10 / **Considerations:** You can make eth\_getloqs requests on any block range with a 1K block range by default when a contract address is provided. Contracts with high activity may be limited to smaller block ranges. If no contract address is provided, the block range will be 8.
  - **JSON-RPC:** eth\_getRawTransactionByHash / **Description:** Returns the raw form of the transaction specified by the transaction\_hash. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getStorageAt / **Description:** Returns the value of the specified storage position for the specified account address and block identifier. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getTransactionByBlockHashAndIndex / **Description:** Returns information about a transaction using the specified block hash and transaction index position. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getTransactionByBlockNumberAndIndex / **Description:** Returns information about a transaction using the specified block number and transaction index position. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getTransactionByHash / **Description:** Returns information about the transaction with the specified transaction hash. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getTransactionCount / **Description:** Returns the number of transactions sent from the specified address and block identifier. / **Quota:** 100 / **Considerations:** 
  - **JSON-RPC:** eth\_getTransactionReceipt / **Description:** Returns the receipt of the transaction using the specified transaction hash. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getUncleByBlockHashAndIndex / **Description:** Returns information about the uncle block specified using the block hash and uncle index position. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getUncleByBlockNumberAndIndex / **Description:** Returns information about the uncle block specified using the block number and uncle index position. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getUncleCountByBlockHash / **Description:** Returns the number of counts in the uncle specified using the uncle hash. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_getUncleCountByBlockNumber / **Description:** Returns the number of counts in the uncle specified using the uncle number. / **Quota:** 150 / **Considerations:** 
  - **JSON-RPC:** eth\_maxPriorityFeePerGas / **Description:** Returns the fee per gas that's an estimate of how much you can pay as a priority fee, or "tip," to get a transaction included in the current block. / **Quota:** 300 / **Considerations:** Generally you use the value that's returned from this method to set the maxFeePerGas in the subsequent transaction that you're submitting.
  - **JSON-RPC:** eth\_protocolVersion / **Description:** Returns the current Ethereum protocol version. / **Quota:** 300 / **Considerations:** 
  - **JSON-RPC:** eth\_sendRawTransaction / **Description:** Creates a new message call transaction or a contract creation for signed transactions.  / **Quota:** 10 / **Considerations:** Managed Blockchain supports raw transactions only. You must create and sign transactions before sending them.

- ** Debug**
  - **JSON-RPC:** debug\_traceBlockByHash / **Description:** Returns the possible tracing result number by executing all transactions in the block specified by the block hash with a tracer (Trace Mode required). / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** debug\_traceBlockByNumber / **Description:** Returns the tracing result by executing all transactions in the block specified by number with a tracer (Trace Mode required). / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** debug\_traceCall / **Description:** Returns the number of possible tracing results by executing an eth call within the context of the given block execution (Trace Mode required). / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** debug\_traceTransaction / **Description:** Returns all traces of a given transaction (Trace Mode required). / **Quota:** 10 / **Considerations:** 

- **Net**
  - **JSON-RPC:** net\_version
  - **Description:** Returns the current network id.
  - **Quota:** 300
  - **Considerations:** 

- **Trace**
  - **JSON-RPC:** trace\_block / **Description:** Returns a full stack trace of all invoked opcodes of all transactions that were included in a block. / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** trace\_call / **Description:** Returns the number of possible tracing results by executing an eth call within the context of the given block execution (Trace Mode required). / **Quota:** 10 / **Considerations:** 
  - **JSON-RPC:** trace\_transaction / **Description:** Returns all traces of a given transaction (Trace Mode required). / **Quota:** 100 / **Considerations:** 

- **Tx Pool**
  - **JSON-RPC:** txpool\_content / **Description:** Returns all pending and queued transactions. / **Quota:** 2 / **Considerations:** 
  - **JSON-RPC:** txpool\_status / **Description:** Provides a count of all transactions currently pending inclusion in the next blocks, and those that are queued (being scheduled for future execution only). / **Quota:** 10 / **Considerations:** 

- **Web**
  - **JSON-RPC:** web3\_clientVersion
  - **Description:** Returns the current client version.
  - **Quota:** 150
  - **Considerations:** 

