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

**Why is my cluster creation failing?**

Common causes include insufficient IAM permissions, invalid VPC subnet or security group IDs, or missing the required Amazon S3 VPC endpoint for private clusters. Verify that your IAM role has the `timestream-influxdb:CreateDbCluster` permission, that your subnets are in different Availability Zones, and that your security groups allow the required inbound ports. Check the AWS CloudTrail logs for the specific error message.
