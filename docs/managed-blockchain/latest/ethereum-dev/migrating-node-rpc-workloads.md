

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Migrating Amazon Managed Blockchain Node and RPC Workloads
<a name="migrating-node-rpc-workloads"></a>

This guide covers moving applications from Amazon Managed Blockchain Access Ethereum, AMB Access Bitcoin, and AMB Access Polygon to either of the following:
+ Self-managed blockchain nodes deployed on AWS with AWS Blockchain Node Runners ([https://github.com/aws-samples/aws-blockchain-node-runners](https://github.com/aws-samples/aws-blockchain-node-runners)) where a blueprint is available, or with protocol-specific AWS deployment guidance.
+ A third-party blockchain infrastructure provider, such as Alchemy, Quicknode, or Kaleido (AWS Marketplace listings).

AMB Access Ethereum, AMB Access Bitcoin, and AMB Access Polygon expose standard blockchain RPC interfaces. Most applications can therefore preserve their RPC methods and request bodies while changing endpoints, authentication, and network controls.

**Note**  
AWS Blockchain Node Runners is open-source infrastructure as code, not a managed service. Customers assume responsibility for availability, scaling, security, monitoring, client upgrades, backups, and chain synchronization.

## Recommended migration process
<a name="migrating-recommended-process"></a>

1. Inventory the networks, HTTP and WebSocket endpoints, RPC methods, request volume, historical-data requirements, and confirmation rules used by the application.

1. Provision the replacement on the same blockchain network.

1. Fully synchronize the replacement before sending application traffic to it, if self-managing nodes as a replacement.

1. Send read requests to both systems and compare results at fixed blocks or confirmation depths.

1. Store endpoints and credentials in configuration or a secrets manager rather than application code.

1. Shift traffic gradually while monitoring errors, latency, throttling, block height, and synchronization lag.

1. Keep AMB available as a rollback target through an agreed rollback period.

1. After the rollback period, remove unused AMB IAM permissions, delete AMB Accessor tokens, and delete AMB nodes where applicable (AMB Ethereum).

**Note**  
Near-tip results can legitimately differ because of propagation delays or blockchain reorganizations. Use finalized blocks or a fixed confirmation depth for comparisons.

## AMB Access Ethereum
<a name="migrating-eth"></a>

### Existing interface
<a name="migrating-eth-existing"></a>

AMB Ethereum applications commonly use separate HTTP and WebSocket endpoints:

```
HTTPS: https://<node-id>.ethereum.managedblockchain.<region>.amazonaws.com/
WSS:   wss://<node-id>.wss.ethereum.managedblockchain.<region>.amazonaws.com/
```

Requests use either: AWS Signature Version 4, with `managedblockchain` as the signing service; or an AMB Accessor billing token in the endpoint URL.

### Option 1: AWS Blockchain Node Runners
<a name="migrating-eth-option1"></a>

The current Ethereum Node Runners blueprints allow you to deploy Ethereum nodes with multiple client pairings across testnet and mainnet, including the same pair AMB Ethereum provides: Geth as the execution client with Lighthouse as the consensus client. Using the same client combination can reduce client-specific behavior differences during migration.

1. Deploy and synchronize an Ethereum Node Runner ([https://aws-samples.github.io/aws-blockchain-node-runners/docs/blueprints/ethereum](https://aws-samples.github.io/aws-blockchain-node-runners/docs/blueprints/ethereum)) template on AWS.

1. Select a deployment appropriate for the workload:
   + A single node for development or interruption-tolerant workloads.
   + An HA deployment for production-like availability.
   + An archive-capable configuration for historical state calls such as `eth_getBalance` or `eth_call` across historical blocks.

1. Replace the AMB HTTP endpoint with the private node or internal load-balancer endpoint: `http://<private-node-address-or-internal-alb>:8545`

1. Remove the AMB SigV4 signing provider or Accessor billing-token parameter.

1. Configure your application to use a standard Ethereum JSON-RPC provider and the new RPC endpoint.

Example configuration:

```
# Before
ETH_RPC_URL=https://<node-id>.ethereum.managedblockchain.<region>.amazonaws.com/
# After
ETH_RPC_URL=http://<private-node-address-or-internal-alb>:8545
```

Example with ethers:

```
const provider = new ethers.JsonRpcProvider(process.env.ETH_RPC_URL);
```

The JSON-RPC method and parameters can generally remain unchanged when the selected Ethereum client supports the same method. Validate client-specific namespaces, optional response fields, error responses, and historical retention.

**Note**  
Ensure that your application has the appropriate network access to the blockchain nodes you deploy.

#### Secure the new endpoint
<a name="migrating-eth-secure"></a>

The documented Node Runner Ethereum endpoint is private and controlled primarily through VPC routing and security groups. It does not provide AMB-style application authentication, which is configurable using your own authentication and authorization patterns.
+ Restrict ingress to specific application security groups or CIDRs.
+ Enable only required RPC namespaces. Do not expose administrative, account-management, personal, or debug methods unless required.
+ Do not publish port 8545 directly to the internet.
+ If clients are outside the VPC, place an authenticated TLS proxy or API layer in front of the endpoint.
+ Treat `eth_sendRawTransaction` as write-capable even though transactions are signed elsewhere.

#### WebSocket and Consensus API workloads
<a name="migrating-eth-websocket"></a>

The documented Node Runner endpoint is HTTP JSON-RPC on port 8545. Applications using `eth_subscribe` must separately enable and securely expose the selected execution client's WebSocket interface. When WebSockets are enabled in Geth, the interface uses port 8546 by default. Account for long-lived connections, application-managed reconnection and resubscription, and load-balancer stickiness.

Applications using the AMB Ethereum Consensus API must configure a separate private Beacon REST API endpoint. The execution JSON-RPC endpoint is not a replacement for the Consensus API.

### Option 2: Third-party RPC provider
<a name="migrating-eth-option2"></a>

1. Create a provider project for the same Ethereum network.

1. Obtain separate HTTP and WSS endpoints if the application uses both.

1. Replace the AMB endpoints with the provider endpoints.

1. Remove SigV4 or the AMB Accessor token.

1. Add the provider's authentication mechanism, commonly an API key in the URL or an HTTP header.

1. Store credentials in a secrets manager and never embed them in browser or mobile application code.

1. Confirm support for required methods, historical state, batch requests, subscriptions, quotas, and rate limits.

```
ETH_RPC_URL=https://<provider-endpoint>/<secret>
ETH_WS_URL=wss://<provider-endpoint>/<secret>
```

### Ethereum validation checklist
<a name="migrating-eth-validation"></a>
+ `eth_chainId` returns the intended network.
+ `eth_blockNumber` stays close to the latest block height reported by an independent trusted node or explorer, allowing for expected propagation delay.
+ Block, transaction, and receipt lookups return expected results.
+ Contract calls through `eth_call` succeed.
+ Required historical-state calls succeed.
+ Controlled transaction submission works on a test network.
+ Application reconnect logic re-establishes WebSocket connections and subscriptions after disconnects without missing required events.
+ Batch behavior, errors, timeouts, and rate limits meet application requirements.

## AMB Access Bitcoin
<a name="migrating-btc"></a>

### Existing interface
<a name="migrating-btc-existing"></a>

AMB Bitcoin uses regional Mainnet and Testnet HTTPS endpoints:

```
https://mainnet.bitcoin.managedblockchain.<region>.amazonaws.com/
https://testnet.bitcoin.managedblockchain.<region>.amazonaws.com/
```

Bitcoin JSON-RPC requests to these endpoints are authenticated with SigV4.

### Option 1: AWS Blockchain Node Runners
<a name="migrating-btc-option1"></a>

The current Bitcoin Node Runner blueprint uses Bitcoin Core as its node client, the same one supported in AMB Bitcoin, preserving compatibility with Bitcoin Core JSON-RPC methods.

1. Deploy and synchronize a Bitcoin Node Runner ([https://aws-samples.github.io/aws-blockchain-node-runners/docs/blueprints/bitcoin](https://aws-samples.github.io/aws-blockchain-node-runners/docs/blueprints/bitcoin)) template on AWS.

1. Confirm Initial Block Download is complete and the node is on the intended chain (e.g. mainnet).

1. Obtain the private node or internal load-balancer address.

1. Retrieve the generated RPC username and password from AWS Secrets Manager.

1. Replace the AMB endpoint with: `http://<private-node-address-or-internal-alb>:8332/`

1. Remove SigV4 signing and use the Bitcoin Core rpcauth credentials through HTTP Basic authentication, or an alternative authentication setup of your choice.

Example:

```
BTC_RPC_AUTH=$(aws secretsmanager get-secret-value --secret-id bitcoin_rpc_credentials --query SecretString --output text --region "$AWS_REGION")
curl --user "$BTC_RPC_AUTH" --data-binary '{"jsonrpc":"1.0","id":"migration-test","method":"getblockchaininfo","params":[]}' -H 'content-type: text/plain' http://<private-node-address>:8332/
```

The Node Runner configuration enables txindex, supporting lookup of arbitrary confirmed transactions through methods such as `getrawtransaction`. Existing Bitcoin JSON-RPC method names and parameters can generally remain unchanged when Bitcoin Core supports them.

**Note**  
Ensure that your application has the appropriate network access to the blockchain nodes you deploy.

#### Security and HA considerations
<a name="migrating-btc-security-ha"></a>
+ Keep the RPC endpoint private and restrict access with VPC routing and security groups.
+ Basic authentication protects access but does not encrypt traffic. Add TLS if traffic crosses an untrusted network boundary.
+ Store RPC credentials in Secrets Manager rather than application files.
+ AMB Access Bitcoin does not manage customer wallet keys. Migration does not transfer wallets or private keys.
+ HA nodes do not share wallet or mempool state. A transaction sent to one node might not immediately appear in another node's mempool.

### Option 2: Third-party RPC provider
<a name="migrating-btc-option2"></a>

1. Confirm support for the required Bitcoin network and RPC methods.

1. Replace the AMB regional endpoint with the provider endpoint.

1. Remove SigV4.

1. Add the provider's API key, header, or Basic authentication as documented.

1. Validate method restrictions. Hosted providers might not expose wallet, peer-management, or administrative Bitcoin Core methods.

1. Review quotas, batch behavior, transaction-broadcast policy, mempool visibility, and historical transaction support.

### Bitcoin validation checklist
<a name="migrating-btc-validation"></a>
+ `getblockchaininfo` reports the expected chain and completed synchronization.
+ `getblockcount` and `getbestblockhash` track a trusted reference.
+ `getblock`, `getblockheader`, and `getrawtransaction` return expected results.
+ `getrawmempool` works if the application depends on mempool visibility.
+ Controlled transaction submission works on Testnet.
+ Authentication failures, timeouts, retries, and rate limits behave as expected.
+ HA behavior is acceptable for mempool-dependent or stateful calls.

## AMB Access Polygon
<a name="migrating-polygon"></a>

### Existing interface
<a name="migrating-polygon-existing"></a>

AMB Access Polygon exposes Polygon Mainnet through a regional HTTPS endpoint:

```
https://mainnet.polygon.managedblockchain.<region>.amazonaws.com/
```

Requests use either: AWS Signature Version 4, with `managedblockchain` as the signing service; or an AMB Accessor billing token in the billingtoken query parameter. Do not use both authentication methods in the same request. AMB Access Polygon exposes only its documented JSON-RPC method subset and does not support batch requests. Its documented interface is HTTPS; it does not provide an AMB WebSocket endpoint.

### Option 1: Self-managed Polygon nodes on AWS
<a name="migrating-polygon-option1"></a>

AWS Blockchain Node Runners does not currently include a built-in Polygon blueprint. For a self-managed replacement, use the official Polygon full-node Docker guide ([https://docs.polygon.technology/pos/how-to/full-node/full-node-docker](https://docs.polygon.technology/pos/how-to/full-node/full-node-docker)) for current Heimdall and Bor setup instructions. The AWS architecture guidance for running Polygon nodes ([https://aws.amazon.com/blogs/database/run-polygon-nodes-on-aws/](https://aws.amazon.com/blogs/database/run-polygon-nodes-on-aws/)) provides additional AWS infrastructure, storage, snapshot, and scaling considerations.

A Polygon PoS RPC node runs Heimdall for consensus and checkpoint processing with Bor as the EVM-compatible execution client. Bor is based on Geth and serves the application-facing JSON-RPC interface.

1. Deploy Heimdall and Bor for Polygon Mainnet and fully synchronize both clients.

1. Select a deployment appropriate for the workload:
   + A single full node for development or interruption-tolerant workloads.
   + Multiple RPC nodes behind a load balancer for production-like availability and capacity.
   + An archive-capable configuration when calls require historical state that a pruned full node does not retain.

1. Plan for multi-terabyte storage and use trusted Polygon snapshots or internally maintained snapshots to reduce bootstrap time.

1. Replace the AMB endpoint with the private Bor RPC endpoint: `http://<private-node-address-or-internal-alb>:8545`

1. Remove the AMB SigV4 signing provider or Accessor billing-token parameter.

1. Configure the application to use a standard EVM JSON-RPC provider.

Example configuration:

```
# Before
POLYGON_RPC_URL=https://mainnet.polygon.managedblockchain.<region>.amazonaws.com/
# After
POLYGON_RPC_URL=http://<private-node-address-or-internal-alb>:8545
```

Example with ethers:

```
const provider = new ethers.JsonRpcProvider(process.env.POLYGON_RPC_URL);
```

Existing `eth_*`, `net_*`, `web3_*`, `debug_*`, `trace_*`, and `txpool_*` method names can generally remain unchanged when Bor enables and supports the required namespace. Validate response fields, errors, tracing options, transaction-pool behavior, historical retention, and any methods that were outside the AMB-supported subset.

#### Secure and operate the new endpoint
<a name="migrating-polygon-secure"></a>
+ Keep Bor JSON-RPC private and restrict access with VPC routing and security groups.
+ Keep the Heimdall API internal unless a specific operational use requires access.
+ Enable only required RPC namespaces. Do not expose administrative, account-management, personal, debug, or trace methods unless required.
+ Do not publish ports 8545 or 8546 directly to the internet.
+ If clients are outside the VPC, place an authenticated TLS proxy or API layer in front of the endpoint.
+ Treat `eth_sendRawTransaction` as write-capable even though transactions are signed elsewhere.
+ Monitor both Heimdall and Bor synchronization. Do not route application traffic to a node until both clients are healthy and Bor is near the chain tip.
+ Account for node-local mempool state when distributing requests across multiple RPC nodes.

#### WebSocket workloads
<a name="migrating-polygon-websocket"></a>

When enabled, Bor exposes its WebSocket interface on port 8546 by default. Secure it separately from HTTP JSON-RPC and account for long-lived connections, application-managed reconnection and resubscription, and load-balancer stickiness.

### Option 2: Third-party RPC provider
<a name="migrating-polygon-option2"></a>

1. Create a provider project for Polygon PoS Mainnet.

1. Obtain an HTTPS endpoint and a WSS endpoint if the application will use subscriptions.

1. Replace the AMB HTTPS endpoint with the provider endpoint.

1. Remove SigV4 or the AMB Accessor token.

1. Add the provider's authentication mechanism, commonly an API key in the URL or an HTTP header.

1. Store credentials in a secrets manager and never embed them in browser or mobile application code.

1. Confirm support for every required AMB method, historical state, traces, transaction-pool calls, batch requests, subscriptions, quotas, and rate limits.

```
POLYGON_RPC_URL=https://<provider-endpoint>/<secret>
POLYGON_WS_URL=wss://<provider-endpoint>/<secret>
```

### Polygon validation checklist
<a name="migrating-polygon-validation"></a>
+ `eth_chainId` returns Polygon Mainnet chain ID 137 (0x89).
+ `eth_blockNumber` stays close to the latest block height reported by an independent trusted node or explorer, allowing for expected propagation delay.
+ Block, transaction, receipt, balance, and contract-call responses match at fixed block numbers.
+ Required historical-state, debug, trace, and transaction-pool calls succeed.
+ A controlled transaction-submission test succeeds using the application's established safe test procedure.
+ Confirmation depth and blockchain-reorganization handling meet application requirements.
+ If WebSockets are introduced on the replacement, application reconnect logic re-establishes connections and subscriptions without missing required events.
+ Batch behavior, errors, timeouts, quotas, and rate limits meet application requirements.
+ HA behavior is acceptable for mempool-dependent calls and transaction propagation.

## References
<a name="migrating-references"></a>
+ [AMB Ethereum JSON-RPC calls and authentication](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/json-rpc-api-examples.html)
+ [AMB Bitcoin endpoint and request examples](https://docs.aws.amazon.com/managed-blockchain/latest/ambbtc-dg/getting-started.html)
+ [AMB Polygon endpoint and request examples](https://docs.aws.amazon.com/managed-blockchain/latest/ambp-dg/getting-started.html)
+ [AMB Polygon supported JSON-RPC methods](https://docs.aws.amazon.com/managed-blockchain/latest/ambp-dg/polygon-api.html)
+ [AMB Polygon Accessor tokens](https://docs.aws.amazon.com/managed-blockchain/latest/ambp-dg/polygon-tokens.html)
+ [AWS Blockchain Node Runners](https://github.com/aws-samples/aws-blockchain-node-runners)
+ [Ethereum Node Runner](https://aws-samples.github.io/aws-blockchain-node-runners/docs/blueprints/ethereum)
+ [Bitcoin Node Runner](https://aws-samples.github.io/aws-blockchain-node-runners/docs/blueprints/bitcoin)
+ [Polygon full node using Docker](https://docs.polygon.technology/pos/how-to/full-node/full-node-docker)
+ [Run Polygon nodes on AWS](https://aws.amazon.com/blogs/database/run-polygon-nodes-on-aws/)
+ [Polygon node default ports](https://docs.polygon.technology/pos/reference/port-management/)