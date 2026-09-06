

# Supported Consensus API methods
<a name="supported-consensus-apis"></a>

Amazon Managed Blockchain (AMB) Access Ethereum supports the following Ethereum Consensus API methods. Each supported API has a brief description of its utility. Unique considerations for using the Consensus method with an Ethereum node in Amazon Managed Blockchain (AMB) are indicated where applicable.

**Note**  
The Consensus API doesn't support WebSocket connections.
Any methods that aren't listed are not supported.
Ethereum API calls to an Ethereum node in Amazon Managed Blockchain (AMB) can be authenticated by using the [Signature Version 4 (SigV4) signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account that created the node can interact with it using the Ethereum APIs. AWS credentials (an access key ID and secret access key) must be provided with the call.
Token based access can also be used to make Ethereum API calls to an Ethereum node as a convenient alternative to the Signature Version 4 (SigV4) signing process. If you prioritize security and auditability over convenience, use the SigV4 signing process instead. However, if you use token based access to make Ethereum APIs calls, any security benefits that are provided by using the SigV4 signing process is negated.

**Topics**
+ [Making Consensus API calls to an Ethereum node in Amazon Managed Blockchain (AMB)](consensus-api-examples.md)

State related APIs are supported only for the following states:
+ `/eth/v1/beacon/states/head`
+ `/eth/v1/beacon/states/finalized`
+ `/eth/v1/beacon/states/justified`
+ `/eth/v1/beacon/states/genesis`


| Method | Description | 
| --- | --- | 
| /eth/v1/beacon/genesis | Returns the details of the chain's genesis block. | 
| /eth/v1/beacon/states/{state\_id}/root | Calculates the HashTreeRoot for the state with a given state\_id. If the state\_id is root, the same value will be returned. | 
| /eth/v1/beacon/states/{state\_id}/fork | Gets the fork object for the requested state\_id. | 
| /eth/v1/beacon/states/{state\_id}/finality\_checkpoints | Returns the finality checkpoints for a state with a given state\_id. In case finality is not yet achieved, the checkpoint returns epoch 0 and ZERO\_HASH as root. | 
| /eth/v1/beacon/states/{state\_id}/committees | Returns the committees for a given state\_id. | 
| /eth/v1/beacon/headers | Returns the block headers matching a given query. | 
| /eth/v1/beacon/headers/headers/{block\_id} | Returns the block header for a given block\_id. | 
| /eth/v2/beacon/blocks/{block\_id} | Returns the block details for a given block\_id. | 
| /eth/v1/beacon/blocks/{block\_id}/root | Returns the hashTreeRoot of a BeaconBlock/BeaconBlockHeader for a given block\_id. | 
| /eth/v1/beacon/blocks/{block\_id}/attestations | Returns the attestations of a block using its block\_id. | 
| /eth/v1/config/fork\_schedule | Returns all the forks; past, present, and future, of which this node is aware. | 
| /eth/v1/config/spec | Returns the configuration specification used for this node. | 
| /eth/v1/config/deposit\_contract | Returns the Eth1 deposit contract address and chain ID. | 
| /eth/v2/debug/beacon/heads | Returns all the possible chain heads (leaves of the fork choice tree). | 
| /eth/v1/node/identity | Returns data about the node's network presence. | 
| /eth/v1/node/peers | Returns data about the node's network peers. | 
| /eth/v1/node/peers/{peer\_id} | Returns data about a peer given the peer\_id. | 
| /eth/v1/node/peer\_count | Returns the number of known peers. | 
| /eth/v1/node/version | Requests the Beacon node identify information about its implementation in a format similar to a [HTTP User-Agent](https://datatracker.ietf.org/doc/html/rfc7231#section-5.5.3) field. | 
| /eth/v1/node/syncing | Requests the Beacon node to describe if it's currently syncing, and if it's, what block it's up to. | 
| /eth/v1/node/health | Returns the Beacon node's health status in HTTP status codes. This is useful information for load balancers. | 