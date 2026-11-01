

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Clusters and instances FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-clusters"></a>

Questions about creating, configuring, and scaling Amazon Timestream for InfluxDB 3 clusters and instance types. For detailed instructions, see [Manage InfluxDB 3 Clusters in Timestream](managing-influxdb-3-clusters.md) and [Configuring an InfluxDB 3 cluster in Timestream](configuring-a-influxdb-3-instance.md).

**What instance types are available?**  
Amazon Timestream for InfluxDB 3 offers instance types ranging from `db.influx.medium` (1 vCPU, 8 GiB) to `db.influx.24xlarge` (96 vCPUs, 768 GiB). All instances use the `db.influxIOIncluded` class, which bundles I/O costs into compute pricing for predictable billing.

**How do I create an InfluxDB 3 cluster?**  
You can create a cluster using the AWS Management Console, the AWS CLI, or the Amazon Timestream API. At minimum, you need to specify a cluster name, instance type, VPC subnet IDs, and security group IDs. For example, using the AWS CLI:  

```
aws timestream-influxdb create-db-cluster \
  --name "my-cluster" \
  --db-instance-type db.influx.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc
```

**How do multi-node Enterprise clusters work?**  
Enterprise clusters support up to 15 nodes distributed across multiple Availability Zones, with dedicated writer/reader (up to 4), reader-only (up to 13), and compactor roles. AWS manages the cluster topology and node roles. Nodes communicate internally and use DNS-based traffic distribution for client connections. For details, see [Scaling a cluster](multi-node-scaling.md) and the [InfluxDB 3 Enterprise clustering documentation](https://docs.influxdata.com/influxdb3/enterprise/admin/clustering/).

**How do I scale my cluster?**  
You can scale vertically by changing the instance type, or scale horizontally (Enterprise only) by adding writer/reader nodes (up to 4) or reader-only nodes (up to 13). To scale horizontally, create a new parameter group with your desired node configuration and apply it to your cluster. Use the `update-db-cluster` command or the AWS Management Console to apply changes. For more information, see [Scaling a cluster](multi-node-scaling.md).

**How do I upgrade from Core to Enterprise edition?**  
You can upgrade an existing Core cluster to Enterprise through the AWS Management Console. If this is the first Enterprise activation on your AWS account, the upgrade must be done via the console. After that initial activation, subsequent upgrades can also be performed using the AWS CLI or API. Note that this is a one-way operation—you cannot downgrade from Enterprise to Core. After the upgrade, your existing data will be gradually compacted in the background while the cluster remains usable. For details, see [Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md).

**What should I expect after upgrading from Core to Enterprise regarding compaction?**  
Because Core edition does not include a compactor, all existing data must be compacted after the upgrade to Enterprise. How this affects your cluster depends on your configuration:  
+ **Single-node clusters**: The compactor shares the same node as the writer and reader. You will likely need additional capacity (a larger instance type) to allow the compactor to process all existing data without impacting your running workload. Consider scaling up before or immediately after the upgrade, and scaling back down once compaction catches up.
+ **3-node clusters**: A dedicated compactor node is provisioned, but the full performance benefits of Enterprise (such as optimized query performance from compacted data) will not be realized until the compactor finishes processing all pre-existing data. The time required depends on the volume of data in the database, the current workload, and the instance size and configuration.
To speed up compaction, you can increase `compaction-max-num-files-per-plan` and reduce `compaction-check-interval` in your parameter group. Scaling up the instance type also gives the compactor more CPU and memory to work with. For details, see [Category 4: Compaction](compaction-parameters.md) and [Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md).

**Why is my cluster creation failing?**  
Common causes include insufficient IAM permissions, invalid VPC subnet or security group IDs, or missing the required Amazon S3 VPC endpoint for private clusters. Verify that your IAM role has the `timestream-influxdb:CreateDbCluster` permission, that your subnets are in different Availability Zones, and that your security groups allow the required inbound ports. Check the AWS CloudTrail logs for the specific error message.

**What are cluster endpoints and how do they work?**  
Multi-node Enterprise clusters provide two types of cluster endpoints: a **read/write endpoint** that routes traffic to writer/reader nodes, and a **read-only endpoint** that routes traffic to all nodes capable of read operations (only available when the cluster includes reader-only nodes). There are also node-specific endpoints for direct access to individual nodes, but these are not recommended for production use as they do not provide automatic failover. For more information, see [Scaling a cluster](multi-node-scaling.md).

**What happens during a scaling operation?**  
When you scale a cluster by applying a new parameter group, the cluster restarts to apply the new node configuration. For multi-node clusters using cluster endpoints, traffic is automatically redistributed to available nodes during the update process. Nodes are distributed across multiple Availability Zones for high availability. You can monitor the scaling progress through the cluster status, which shows `UPDATING` during the operation. For details, see [Scaling a cluster](multi-node-scaling.md).

**What is the dedicated compactor and when is it required?**  
The dedicated compactor is a node that handles background data optimization tasks such as compacting Parquet files in Amazon S3. It is required for Enterprise clusters with 3 or more nodes (`dedicatedCompactor: true`). By running compaction on a separate node, write and read performance on your other nodes is not impacted by background optimization. Single-node Enterprise clusters handle compaction on the same node alongside read and write operations.

**Can the nodes in one cluster use different instance types?**  
Yes, if you configure the cluster with a **deployment configuration**. A deployment configuration describes the cluster as a list of node groups, and each group carries its own instance type, node count, and set of functions (`INGEST`, `QUERY`, `PROCESS`, `COMPACT`). Clusters whose nodes differ in size this way are called heterogeneous clusters. A cluster configured the older way, through topology parameters on a DB parameter group, uses a single instance type for every node. For details, see [Size cluster functions independently with deployment configurations](influxdb3-deployment-configuration.md).

**Why would I want a heterogeneous cluster?**  
Because the four functions of an Enterprise cluster have different compute needs. Compaction is bursty and memory-hungry, query serving scales with concurrency, and ingest scales with write throughput. When every node must be the same size, you size the whole cluster for its most demanding function. With a deployment configuration you give, for example, the compactor a `db.influx.2xlarge` while your query-only nodes stay on `db.influx.medium`. Compaction gets the compute it needs without enlarging the rest of the cluster.

**What are the node limits for a deployment configuration?**  
Across all groups: 1 to 4 `INGEST` nodes, 0 to 13 `QUERY` nodes, exactly 1 `COMPACT` node, and up to 15 nodes in the cluster counting the compactor. The cluster total is a limit in its own right, so the per-function maximums cannot all be taken at once: 4 ingest plus 13 query plus a compactor is 18 nodes and is rejected, and reaching 13 query nodes means running a single ingest node. A group that includes `PROCESS` must also include `QUERY`. Splitting a function across several groups does not raise its limit. The cap applies to the total number of nodes carrying that mode, so 3 `["INGEST"]` nodes plus 2 `["INGEST","QUERY"]` nodes is 5 ingest nodes and is rejected.  
Separately, the request shape allows 1 to 10 node groups with 1 to 4 distinct modes per group. That is a limit on how you describe a cluster, not on how big it can be. The node limits above and the 15-node cluster total apply regardless of how many groups you use. Add a group when you want part of a function on a different instance type; nodes that share a mode set and an instance type belong in a single group. Requests that break any limit fail validation before a node is provisioned. See [Shape rules and limits](influxdb3-deployment-configuration.md#influxdb3-depcfg-limits) and [Working out a valid shape](influxdb3-deployment-configuration.md#influxdb3-depcfg-combinations).

**Do I still need a dedicated compactor?**  
Above 3 non-compact nodes, yes. `COMPACT` must be its own node group. At 3 or fewer non-compact nodes you can add `COMPACT` to a group that also ingests or queries, which saves an instance. Be aware that a shared compactor competes with live reads and writes for CPU and memory, so for production workloads that compact continuously, give it its own group.

**How do I change the shape of a cluster after I create it?**  
Submit the complete target shape to `update-db-cluster` with `--deployment-configuration`. Timestream compares what you submit against the running cluster and adds, removes, or resizes only what differs, so one call can add a group, drop a group, change a group's `count`, and change a group's `instanceType`. Important: any group you leave out of the request is removed, so resubmit the groups you want to keep unchanged. See [Reshape an existing cluster](influxdb3-deployment-configuration.md#influxdb3-depcfg-update).

**What happens to my existing clusters and parameter groups?**  
Nothing changes. A cluster created with parameter-group topology (`ingestQueryInstances`, `queryOnlyInstances`, `dedicatedCompactor`) keeps running, and read APIs still return its legacy `clusterConfiguration` values. If you pass `--deployment-configuration` on a request whose parameter group still carries those three topology fields, the deployment configuration wins and the topology fields are ignored rather than rejected. Every other parameter-group setting, such as `bufferMemLimitMb` and the compaction parameters, continues to apply normally. Note that you cannot pass `--db-instance-type` together with `--deployment-configuration`, because instance sizes now live inside the node groups.

**How do I see the current shape of my cluster?**  
`get-db-cluster` returns a `deploymentConfiguration` field for any cluster governed by one. Timestream reconstructs it from the cluster's live provisioned instances, so it reflects the shape the cluster actually has rather than a stored copy of your last request; a cluster still using parameter-group topology returns it empty. For a node-by-node view, call `list-db-instances-for-cluster`. Each node reports its own `instanceModes` and `dbInstanceType`. Node grouping is not preserved on read, so a compactor you sideloaded onto an existing group comes back as a `COMPACT` mode on that node rather than as a separate group. Group the returned nodes by mode set and instance type to confirm the shape matches what you requested.

**Do my endpoints change when I reshape a cluster?**  
No. Both cluster endpoints keep working and Timestream updates their membership automatically. `endpoint` is the writer endpoint, backed by the nodes that have `INGEST`. `readerEndpoint` is the reader endpoint, backed by the nodes that have `QUERY` but not `INGEST`. A cluster with no query-only nodes has no reader endpoint. Adding, removing, or resizing nodes restarts the affected nodes, and traffic is redistributed across the remaining nodes behind the endpoints while the change is applied.

**How does billing work for a heterogeneous cluster?**  
Each node is billed for the instance type of the node group it belongs to, for as long as that node runs. There is no separate charge for using a deployment configuration. Sizing functions independently is usually what makes a cluster cheaper: a large compactor plus small query nodes costs less than running every node at the compactor's size. For current rates, see [Amazon Timestream pricing](https://aws.amazon.com/timestream/pricing/).

**How do maintenance windows work?**  
Every Timestream for InfluxDB resource has a weekly maintenance window during which routine maintenance such as OS patching and engine updates is performed. By default, the service manages the maintenance window automatically. You can specify a preferred window using the format `ddd:HH:MM-ddd:HH:MM` (for example, `Sun:02:00-Sun:04:00`) with a minimum duration of 2 hours and a maximum of 24 hours. For details, see [Maintenance windows for Timestream for InfluxDB 3](influxdb3-maintenance-windows.md).

**Can I set a maintenance window in my local timezone?**  
Yes. You can specify a timezone for your maintenance window using IANA timezone identifiers such as `America/New_York`, `Europe/London`, or `Asia/Tokyo`. The `timezone` field is required when configuring a maintenance schedule. The system handles Daylight Saving Time transitions automatically. For the full list of supported timezones, see [Maintenance windows for Timestream for InfluxDB 3](influxdb3-maintenance-windows.md).