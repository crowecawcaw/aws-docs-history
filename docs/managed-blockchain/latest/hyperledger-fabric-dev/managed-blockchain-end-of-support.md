

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Amazon Managed Blockchain (AMB) end of support
<a name="managed-blockchain-end-of-support"></a>

After careful consideration, we decided to end support for Amazon Managed Blockchain (AMB), effective September 29, 2027. Amazon Managed Blockchain (AMB) will no longer accept new customers beginning October 29, 2026. As an existing customer, you can continue to use the service as normal until September 29, 2027. After September 29, 2027, you will no longer be able to access Amazon Managed Blockchain (AMB) functionality.

We recommend that you begin planning your migration as soon as possible. If you use AMB Access Ethereum, Bitcoin, or Polygon, you can migrate to self-managed blockchain nodes on AWS or to a third-party blockchain infrastructure provider. If you use AMB Query, you can migrate to a managed blockchain data provider. If you use AMB Access Hyperledger Fabric, you can migrate to another managed Hyperledger Fabric network, to self-managed Hyperledger Fabric on AWS (Amazon EC2 or Amazon EKS), or to an AWS database.

## AMB Access Ethereum, Bitcoin or Polygon
<a name="amb-eos-access-ethereum-bitcoin-polygon"></a>

AMB Access Ethereum, Bitcoin, and Polygon expose standard blockchain RPC interfaces, so most applications can preserve their RPC methods and request bodies while changing endpoints, authentication, and network controls. You have two options.

### Migration options
<a name="amb-eos-access-migration-options"></a>

#### Self-managed nodes on AWS
<a name="amb-eos-access-self-managed-nodes"></a>

If you want full control of your blockchain node, you can move to self-hosting on AWS using AWS Blockchain Node Runners, an open-source accelerator for blockchain nodes on AWS. The Node Runners blueprints provide infrastructure-as-code templates that let you deploy your chosen client on vetted Amazon EC2 instance configurations, in either a single-node or multi-node high-availability setup.

#### Third-party blockchain infrastructure provider
<a name="amb-eos-access-third-party"></a>

Use a managed node/RPC service from an AWS Partner, such as Alchemy, QuickNode, or Kaleido. Your provider supplies endpoints and an authentication mechanism (commonly an API key).

### How to migrate
<a name="amb-eos-access-how-to-migrate"></a>

1. Inventory the networks, HTTP and WebSocket endpoints, RPC methods, request volume, historical-data requirements, and confirmation rules used by the application.

1. Provision the replacement on the same blockchain network.

1. Fully synchronize the replacement before sending application traffic to it, if self-managing nodes as a replacement.

1. Send read requests to both systems and compare results at fixed blocks or confirmation depths.

1. Store endpoints and credentials in configuration or a secrets manager rather than application code.

1. Shift traffic gradually while monitoring errors, latency, throttling, block height, and synchronization lag.

1. Keep AMB available as a rollback target through an agreed rollback period.

1. After the rollback period, remove unused AMB IAM permissions, delete AMB Accessor tokens, and delete AMB nodes where applicable (AMB Ethereum).

For detailed instructions, endpoint formats, code examples, and validation checklists, see [Migrating Amazon Managed Blockchain Node and RPC Workloads](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/migrating-node-rpc-workloads.html).

## AMB Query
<a name="amb-eos-query"></a>

AMB Query is a SigV4-authenticated, indexed API that returns normalized blockchain data, including transaction history, balances, token and contract information, and transaction events. Migrating is not an endpoint-only change: a standard node does not provide these indexed query capabilities, so you should expect to normalize provider fields into your application's data model and validate against representative AMB responses before cutover. You have two options.

### Migration options
<a name="amb-eos-query-migration-options"></a>

#### QuickNode: API-oriented migration
<a name="amb-eos-query-quicknode"></a>

QuickNode is the better fit when the application prefers documented request/response APIs and low-latency synchronous access, such as wallet, explorer, transaction-monitoring, or application backends.

#### Allium: flexible data and query migration
<a name="amb-eos-query-allium"></a>

Allium is the better fit when the application requires flexible access to provider-maintained blockchain datasets and can use a combination of Realtime APIs and Explorer queries.

### How to migrate
<a name="amb-eos-query-how-to-migrate"></a>

1. Inventory the existing workload: the AMB Query operations in use, the fields actually consumed, filters, sorting, pagination, request volume, and confirmation rules.

1. Evaluate provider fit against that inventory to determine whether QuickNode's API-oriented model or Allium's query-oriented model is the better fit.

1. Modify the application. Remove the AWS SDK client and SigV4 signing, integrate the provider's interfaces, translate data models, replace pagination and sorting, and store credentials in a secrets manager.

1. Validate the replacement against representative, finalized Ethereum Mainnet and Bitcoin Mainnet data, comparing normalized provider output with captured AMB responses.

1. Cut over safely. Run both paths in parallel where AMB Query remains available, shift traffic gradually while monitoring correctness and latency, then remove unused AMB Query dependencies and IAM permissions.

For a detailed provider comparison, an AMB Query API-to-provider mapping, and validation guidance, see [Migrating Amazon Managed Blockchain Query Workloads](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/migrating-query-workloads.html).

## AMB Access Hyperledger Fabric
<a name="amb-eos-hlf"></a>

If you use AMB Access Hyperledger Fabric, you have the following migration options.

### Migration options
<a name="amb-eos-hlf-migration-options"></a>

#### Another managed Hyperledger Fabric network
<a name="amb-eos-hlf-managed"></a>

Choose this if you want to continue with managed operations and are comfortable with a similar network model. This option keeps operational overhead low, but the destination is a new network with its own identities and configuration, so network state and identities are still rebuilt rather than copied.

#### Self-managed Hyperledger Fabric on AWS (Amazon EC2 or Amazon EKS)
<a name="amb-eos-hlf-self-managed"></a>

Choose this if you want full control over your Certificate Authorities, membership, network configuration, and upgrade cadence. This option requires rebuilding of state and identities that you have maintained in AMB. This migration involves more setup work to stand up and operate the network yourself, in exchange for full ownership of your identity material and channel configuration. Replay of network state from source to the destination self-managed network is still required.

#### An AWS database
<a name="amb-eos-hlf-database"></a>

Choose this if you no longer require a blockchain and want to retain your data in a queryable form. This removes blockchain-specific constructs such as endorsement policies and multi-organization consensus, so it is best suited to customers who need the historical data but not ongoing distributed-ledger operation.

### Migration steps
<a name="amb-eos-hlf-migration-steps"></a>

At a high level, a Hyperledger Fabric migration moves through the following stages:

1. **Discovery and destination selection**. Inventory your network (organizations, channels, chaincode source availability, and private data collections) and select your destination and approach with all participating organizations.

1. **Architecture and identity strategy**. Design the destination network (its channel topology, membership, and Certificate Authority structure) and plan how your existing identities and transaction attribution will map to the new network.

1. **Destination build**. Stand up the destination network and recreate its configuration, policies, identities, and chaincode.

1. **Extraction preparation and dry run**. Validate the migration process against a non-production channel or a copy to confirm it works end to end before touching production data, and schedule the migration window with all participating organizations.

1. **Extraction**. With the source network paused (quiesced) so that no new transactions are committed, extract the ledger data at an agreed point, coordinating across organizations so that private data is captured completely. Verify data extraction against the source network.

1. **Replay**. Load the extracted data into the destination, preserving transaction attribution where required.

1. **Validation and cutover**. Compare the destination against the source, validate that your applications and access controls behave correctly, then switch your applications over to the destination and place the source network in read-only mode.

1. **Decommission and handover**. After a monitoring period, retire the source network and operate on the destination.

As these migrations vary widely depending on your network configuration, identities, and private data, and require coordination across all participating organizations, contact AWS Support or your AWS account team and begin planning as soon as possible.