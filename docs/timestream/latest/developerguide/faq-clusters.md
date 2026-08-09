For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Clusters and instances FAQ for Amazon Timestream for InfluxDB 3

Questions about creating, configuring, and scaling Amazon Timestream for InfluxDB 3 clusters and instance types. For detailed instructions, see [Manage InfluxDB 3 Clusters in Timestream](managing-influxdb-3-clusters.md "managing-influxdb-3-clusters.md") and [Configuring an InfluxDB 3 cluster in Timestream](configuring-a-influxdb-3-instance.md "configuring-a-influxdb-3-instance.md").

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

Enterprise clusters support up to 15 nodes distributed across multiple Availability Zones, with dedicated writer/reader (up to 4), reader-only (up to 13), and compactor roles. AWS manages the cluster topology and node roles. Nodes communicate internally and use DNS-based traffic distribution for client connections. For details, see [Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md") and the [InfluxDB 3 Enterprise clustering documentation](https://docs.influxdata.com/influxdb3/enterprise/admin/clustering/ "https://docs.influxdata.com/influxdb3/enterprise/admin/clustering/").

**How do I scale my cluster?**

You can scale vertically by changing the instance type, or scale horizontally (Enterprise only) by adding writer/reader nodes (up to 4) or reader-only nodes (up to 13). To scale horizontally, create a new parameter group with your desired node configuration and apply it to your cluster. Use the `update-db-cluster` command or the AWS Management Console to apply changes. For more information, see [Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md").

**How do I upgrade from Core to Enterprise edition?**

You can upgrade an existing Core cluster to Enterprise through the AWS Management Console. If
this is the first Enterprise activation on your AWS account, the upgrade must be done via
the console. After that initial activation, subsequent upgrades can also be performed using
the AWS CLI or API. Note that this is a one-way operation—you cannot downgrade from Enterprise
to Core. After the upgrade, your existing data will be gradually compacted in the background
while the cluster remains usable. For details, see
[Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md "upgrading-core-to-enterprise.md").

**What should I expect after upgrading from Core to Enterprise regarding compaction?**

Because Core edition does not include a compactor, all existing data must be compacted
after the upgrade to Enterprise. How this affects your cluster depends on your
configuration:

- **Single-node clusters**: The compactor shares the same
  node as the writer and reader. You will likely need additional capacity (a larger instance
  type) to allow the compactor to process all existing data without impacting your running
  workload. Consider scaling up before or immediately after the upgrade, and scaling back
  down once compaction catches up.
- **3-node clusters**: A dedicated compactor node is
  provisioned, but the full performance benefits of Enterprise (such as optimized query
  performance from compacted data) will not be realized until the compactor finishes
  processing all pre-existing data. The time required depends on the volume of data in the
  database, the current workload, and the instance size and configuration.

To speed up compaction, you can increase `compaction-max-num-files-per-plan`
and reduce `compaction-check-interval` in your parameter group. Scaling up the
instance type also gives the compactor more CPU and memory to work with. For details, see
[Category 4: Compaction](compaction-parameters.md "compaction-parameters.md") and
[Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md "upgrading-core-to-enterprise.md").

**Why is my cluster creation failing?**

Common causes include insufficient IAM permissions, invalid VPC subnet or security group IDs, or missing the required Amazon S3 VPC endpoint for private clusters. Verify that your IAM role has the `timestream-influxdb:CreateDbCluster` permission, that your subnets are in different Availability Zones, and that your security groups allow the required inbound ports. Check the AWS CloudTrail logs for the specific error message.

**What are cluster endpoints and how do they work?**

Multi-node Enterprise clusters provide two types of cluster endpoints: a
**read/write endpoint** that routes traffic to writer/reader
nodes, and a **read-only endpoint** that routes traffic to
all nodes capable of read operations (only available when the cluster includes
reader-only nodes). There are also node-specific endpoints for direct
access to individual nodes, but these are not recommended for production use as they do
not provide automatic failover. For more information, see
[Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md").

**What happens during a scaling operation?**

When you scale a cluster by applying a new parameter group, the cluster restarts to
apply the new node configuration. For multi-node clusters using cluster endpoints, traffic
is automatically redistributed to available nodes during the update process. Nodes are
distributed across multiple Availability Zones for high availability. You can monitor the
scaling progress through the cluster status, which shows `UPDATING` during the
operation. For details, see [Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md").

**What is the dedicated compactor and when is it required?**

The dedicated compactor is a node that handles background data optimization tasks
such as compacting Parquet files in Amazon S3. It is required for Enterprise clusters with 3 or
more nodes (`dedicatedCompactor: true`). By running compaction on a separate
node, write and read performance on your other nodes is not impacted by background
optimization. Single-node Enterprise clusters handle compaction on the same node alongside
read and write operations.

**How do maintenance windows work?**

Every Timestream for InfluxDB resource has a weekly maintenance window during which
routine maintenance such as OS patching and engine updates is performed. By default,
the service manages the maintenance window automatically. You can specify a preferred
window using the format `ddd:HH:MM-ddd:HH:MM` (for example,
`Sun:02:00-Sun:04:00`) with a minimum duration of 2 hours and a maximum of
24 hours. For details, see
[Maintenance windows for Timestream for InfluxDB 3](influxdb3-maintenance-windows.md "influxdb3-maintenance-windows.md").

**Can I set a maintenance window in my local timezone?**

Yes. You can specify a timezone for your maintenance window using IANA timezone
identifiers such as `America/New_York`, `Europe/London`, or
`Asia/Tokyo`. The `timezone` field is required when configuring a
maintenance schedule. The system handles Daylight Saving Time transitions automatically.
For the full list of supported timezones, see
[Maintenance windows for Timestream for InfluxDB 3](influxdb3-maintenance-windows.md "influxdb3-maintenance-windows.md").
