# How DynamoDB global tables work

Multi-account global tables extend DynamoDB global tables fully managed, serverless, multi-Region, and multi-active
capabilities to span multiple AWS accounts. Multi-account global tables replicate data across AWS Regions and accounts,
providing the same active-active functionality as same-account global tables. When you write to any replica, DynamoDB replicates the data to all other replicas.

Key differences from same-account global tables include:

- Multi-account replication is supported for multi-Region eventual consistency (MREC) global tables.
- You can only add replicas by starting with a single-Region table. Converting an existing same-account global table
  into a multi-account setup is not supported. To migrate, you must delete existing replicas to return to a single-Region
  table before creating a new multi-account global table.
- Each replica must reside in a separate AWS account. For a multi-account global table with
  _N_ replicas, you must have _N_ accounts.
- Multi-account global tables use unified table settings across all replicas
  by default. All replicas automatically share the same configuration (such as throughput mode,
  TTL, and PITR), and unlike same-account global tables, these settings cannot be overridden per replica.
- Customers must provide replication permissions to the DynamoDB global tables service principal in their resource policies.
  Multi-account global tables use the same underlying replication technology as same-account
  global tables. Table settings are replicated automatically across all regional replicas,
  and customers cannot override or customize settings per replica. This ensures consistent configuration
  and predictable behavior across multiple AWS accounts participating in the same global table.

Settings in DynamoDB global tables define how a table behaves and how data is replicated across
Regions. These settings are configured through DynamoDB control plane APIs during table creation or when
adding a new regional replica.

When creating a multi-account global table, customers must set `GlobalTableSettingsReplicationMode = ENABLED`
for each regional replica. This ensures that configuration changes made in one Region propagate automatically
to all other Regions that participate in the global table.

You can enable settings replication after table creation.
This supports the scenario where a table is originally created as a regional
table and later upgraded to a multi-account global table.

**Synchronized Settings**

The following table settings are always synchronized across all replicas in a multi-account global
table:

###### Note

Unlike same-account global tables, multi-account global tables do not allow per-Region overrides for these settings.
The only exception is that overrides for read auto-scaling policies (tables and GSIs) are allowed as they are separate external resources.

- Capacity mode (provisioned capacity or on-demand)
- Table provisioned read and write capacity
- Table read and write auto scaling
- Local Secondary Index (LSI) definition
- Global Secondary Index (GSI) definition
- GSI provisioned read and write capacity
- GSI read and write auto scaling
- Streams definition in MREC mode
- Time To Live (TTL)
- Warm Throughput
- On-demand maximum read and write throughput
  **Non-Synchronized Settings**

The following settings are not synchronized between replicas and must be configured
independently for each replica table in each Region.

- Table Class
- Server-side Encryption (SSE) type
- Server-side Encryption (SSE) KMS Key Id
- Deletion Protection
- Kinesis Data Streams (KDSD)
- Tags
- Resource Policy
- Table Cloudwatch-Contributor Insights (CCI)
- GSI Cloudwatch-Contributor Insights (CCI)

## Monitoring

Global tables configured for multi-Region eventual consistency (MREC) publish the [ReplicationLatency](metrics-dimensions.md#ReplicationLatency "metrics-dimensions.md#ReplicationLatency")
metric to CloudWatch. This metric tracks the elapsed time between when an item is written to a replica table, and when that item appears in another replica in the
global table. `ReplicationLatency` is expressed in milliseconds and is emitted for every source and destination Region pair in a global table.

Typical `ReplicationLatency` values depends on the distance between your chosen AWS Regions, as well as other variables
like workload type and throughput. For example, a source replica in the US West (N. California) (us-west-1) Region has lower `ReplicationLatency`
to the US West (Oregon) (us-west-2) Region compared to the Africa (Cape Town) (af-south-1) Region.

An increasing value for `ReplicationLatency` could indicate that updates from one replica are not propagating to other
replica tables in a timely manner. In this case, you can temporarily redirect your application's read and write activity to a different AWS Region.

**Handling Replication Latency Issues in Multi-account Global Tables**

If `ReplicationLatency` exceeds 3 hours due to customer-induced issues on a replica table, DynamoDB sends a notification
requesting the customer to address the underlying problem. Common customer-induced issues that may prevent replication include:

- Removing required permissions from the replica table's resource policy
- Opting out of an AWS Region that hosts a replica of the multi-account global table
- Denying the table's AWS KMS key permissions required to decrypt data

DynamoDB sends an initial notification within 3 hours of elevated replication latency, followed by a second notification after
20 hours if the issue remains unresolved. If the problem is not corrected within the required time window, DynamoDB will automatically
disassociate the replica from the global table. The affected replica will then be converted to a regional table.
