

# Supported Bitcoin JSON-RPCs with Amazon Managed Blockchain (AMB) Access Bitcoin
<a name="bitcoin-api"></a>

This topic provides a list of and references to the Bitcoin JSON-RPCs that Managed Blockchain supports. Each supported JSON-RPC has a brief description of its use. 

**Note**  
 You can authenticate Bitcoin JSON-RPCs on Managed Blockchain by using the [ Signature Version 4 (SigV4) signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account can interact with it by using the Bitcoin JSON-RPCs. Provide AWS credentials (an access key ID and secret access key) with the call.
If your HTTP response is larger than 10 MB, you will get an error. To correct this, you must set the compression headers to `Accept-Encoding:gzip`. The compressed response your client then receives contains the following headers: `Content-Type: application/json` and `Content-Encoding: gzip`. 
Amazon Managed Blockchain (AMB) Access Bitcoin generates a 400 error for malformed JSON-RPC requests.
Use the `sendrawtransaction` JSON-RPC to submit transactions that update the Bitcoin blockchain state. 
AMB Access Bitcoin has a default request limit of 100 requests per second (RPS), per `NETWORK_TYPE`, per AWS Region.  
For increasing your quota, you must contact *AWS support*. To contact AWS support, sign into the [AWS Support Center Console](https://console.aws.amazon.com/support). Choose **Create case**. Choose **Technical**. Choose *Managed Blockchain* as your **service**. Choose *Access:Bitcoin* as your **Category** and *General guidance* as your **Severity**. Enter *RPC Quota* as the **Subject** and in the **Description** text box and list the quota limits applicable to your needs in *RPS per Bitcoin network per Region*. **Submit** your case. 

## Supported JSON-RPCs
<a name="supported-json-rpc"></a>

AMB Access Bitcoin supports the following Bitcoin JSON-RPCs. Each supported call has a brief description of its use.



- **[ Blockchain RPCs](https://developer.bitcoin.org/reference/rpc/#blockchain-rpcs)**
  - **JSON-RPC:** [getbestblockhash](https://developer.bitcoin.org/reference/rpc/getbestblockhash.html) / **Description:** Returns the hash of the best (tip) block in the most-work, fully validated chain.
  - **JSON-RPC:** [getblock](https://developer.bitcoin.org/reference/rpc/getblock.html) / **Description:** If verbosity is 0, returns a string that is serialized, hex-encoded data for block ‘hash’. If verbosity is 1, returns an Object with information about the block ‘hash’. If verbosity is 2, returns an Object with information about the block ‘hash’ and information about each transaction. If verbosity is 3, returns an Object with information about the block ‘hash’ and information about each transaction, including the prevout information for inputs.
  - **JSON-RPC:** [getblockchaininfo](https://developer.bitcoin.org/reference/rpc/getblockchaininfo.html) / **Description:** Returns an object containing various state info regarding blockchain processing.
  - **JSON-RPC:** [getblockcount](https://developer.bitcoin.org/reference/rpc/getblockcount.html) / **Description:** Returns the height of the most-work, fully validated chain. The genesis block has height 0.
  - **JSON-RPC:** [getblockfilter](https://developer.bitcoin.org/reference/rpc/getblockfilter.html) / **Description:** Retrieves a BIP 157 content filter for a particular block using the block hash.
  - **JSON-RPC:** [getblockhash](https://developer.bitcoin.org/reference/rpc/getblockhash.html) / **Description:** Returns hash of block in best-block-chain at height provided.
  - **JSON-RPC:** [ getblockheader](https://developer.bitcoin.org/reference/rpc/getblockheader.html) / **Description:** If verbose is false, returns a string that is serialized, hex-encoded data for blockheader ‘hash’. If verbose is true, returns an Object with information about blockheader ‘hash’. 
  - **JSON-RPC:** [getblockstats](https://developer.bitcoin.org/reference/rpc/getblockstats.html) / **Description:** Computes per block statistics for a given window. All amounts are in satoshis. It won’t work for some heights with pruning.
  - **JSON-RPC:** [getchaintips](https://developer.bitcoin.org/reference/rpc/getchaintips.html) / **Description:** Returns information about all known tips in the block tree, including the main chain and orphaned branches.
  - **JSON-RPC:** [getchaintxstats](https://developer.bitcoin.org/reference/rpc/getchaintxstats.html) / **Description:** Computes statistics about the total number and rate of transactions in the chain.
  - **JSON-RPC:** [getdifficulty](https://developer.bitcoin.org/reference/rpc/getdifficulty.html) / **Description:** Returns the proof-of-work difficulty as a multiple of the minimum difficulty.
  - **JSON-RPC:** [getmempoolancestors](https://developer.bitcoin.org/reference/rpc/getmempoolancestors.html) / **Description:** If txid is in the mempool, returns all in-mempool ancestors.
  - **JSON-RPC:** [getmempooldescendants](https://developer.bitcoin.org/reference/rpc/getmempooldescendants.html) / **Description:** If txid is in the mempool, returns all in-mempool descendants.
  - **JSON-RPC:** [getmempoolentry](https://developer.bitcoin.org/reference/rpc/getmempoolentry.html) / **Description:** Returns mempool data for given transaction.
  - **JSON-RPC:** [getmempoolinfo](https://developer.bitcoin.org/reference/rpc/getmempoolinfo.html) / **Description:** Returns details on the active state of the TX memory pool.
  - **JSON-RPC:** [getrawmempool](https://developer.bitcoin.org/reference/rpc/getrawmempool.html) / **Description:** Returns all transaction IDs in memory pool as a JSON array of string transaction IDs.  `verbose = true` is not supported. 
  - **JSON-RPC:** [gettxout](https://developer.bitcoin.org/reference/rpc/gettxout.html) / **Description:** Returns details about an unspent transaction output.
  - **JSON-RPC:** [gettxoutproof](https://developer.bitcoin.org/reference/rpc/gettxoutproof.html) / **Description:** Returns a hex-encoded proof that “txid” was included in a block.

- **[Rawtransactions RPCs](https://developer.bitcoin.org/reference/rpc/#rawtransactions-rpcs)**
  - **JSON-RPC:** [createrawtransaction](https://developer.bitcoin.org/reference/rpc/createrawtransaction.html) / **Description:** Creates a transaction spending the given inputs and creating new outputs.
  - **JSON-RPC:** [decoderawtransaction](https://developer.bitcoin.org/reference/rpc/decoderawtransaction.html) / **Description:** Returns a JSON object representing the serialized, hex-encoded transaction.
  - **JSON-RPC:** [decodescript](https://developer.bitcoin.org/reference/rpc/decodescript.html) / **Description:** Decodes a hex-encoded script.
  - **JSON-RPC:** [getrawtransaction](https://developer.bitcoin.org/reference/rpc/getrawtransaction.html) / **Description:** Returns the raw transaction data.
  - **JSON-RPC:** [sendrawtransaction](https://developer.bitcoin.org/reference/rpc/sendrawtransaction.html) / **Description:** Submits a raw transaction (serialized, hex-encoded) to local node and network.
  - **JSON-RPC:** [testmempoolaccept](https://developer.bitcoin.org/reference/rpc/testmempoolaccept.html) / **Description:** Returns result of mempool acceptance tests indicating if raw transaction (serialized, hex-encoded) would be accepted by mempool. This checks if the transaction violates the consensus or policy rules.

- **[Util RPCs](https://developer.bitcoin.org/reference/rpc/#util-rpcs)**
  - **JSON-RPC:** [createmultisig](https://developer.bitcoin.org/reference/rpc/createmultisig.html) / **Description:** Creates a multi-signature address with n signature of m keys required.
  - **JSON-RPC:** [estimatesmartfee](https://developer.bitcoin.org/reference/rpc/estimatesmartfee.html) / **Description:** Estimates the approximate fee per kilobyte required for a transaction to begin confirmation within conf\_target blocks, if possible, and returns the number of blocks for which the estimate is valid. Uses virtual transaction size, as defined in BIP 141 (witness data is discounted).
  - **JSON-RPC:** [validateaddress](https://developer.bitcoin.org/reference/rpc/validateaddress.html) / **Description:** Returns information about the given bitcoin address.
  - **JSON-RPC:** [verifymessage](https://developer.bitcoin.org/reference/rpc/verifymessage.html) / **Description:** Verifies a signed message.

