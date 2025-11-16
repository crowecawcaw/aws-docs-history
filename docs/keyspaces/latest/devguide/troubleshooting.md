# Troubleshooting capacity management errors in Amazon Keyspaces

Having trouble with serverless capacity? Here are some common issues and how to resolve them.

## Serverless capacity errors

This section outlines how to recognize errors related to serverless capacity management
and how to resolve them. For example, you might observe insufficient capacity events when
your application exceeds your provisioned throughput capacity.

Because Apache Cassandra is cluster-based software that is designed to run on a fleet of
nodes, it doesn’t have exception messages related to serverless features such as throughput
capacity. Most drivers only understand the error codes that are available in Apache
Cassandra, so Amazon Keyspaces uses that same set of error codes to maintain compatibility.

To map Cassandra errors to the underlying capacity events, you can use Amazon CloudWatch to monitor
the relevant Amazon Keyspaces metrics. Insufficient-capacity events that result in client-side errors can be categorized into these three
groups based on the resource that is causing the event:

- **Table** – If you choose **Provisioned**
  capacity mode for a table, and your application exceeds your
  provisioned throughput, you might observe insufficient-capacity errors.
  For more information, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").
- **Partition** – You might experience
  insufficient-capacity events if traffic against a given partition exceeds 3,000
  RCUs or 1,000 WCUs. We recommend distributing traffic uniformly across
  partitions as a best practice. For more information, see [Data modeling best practices: recommendations for designing data models](data-modeling.md "data-modeling.md").
- **Connection** – You might experience
  insufficient throughput if you exceed the quota for the maximum number of
  operations per second, per connection. To increase throughput, you can increase
  the number of default connections when configuring the connection with the
  driver.

To learn how to configure connections for Amazon Keyspaces, see [How to configure connections in Amazon Keyspaces](connections.md#connections.howtoconfigure "connections.md#connections.howtoconfigure"). For more information about optimizing
connections over VPC endpoints, see [How to configure connections over VPC endpoints in Amazon Keyspaces](connections.md#connections.VPCendpoints "connections.md#connections.VPCendpoints").

To determine which resource is causing the insufficient-capacity event that is
returning the client-side error, you can check the dashboard in the Amazon Keyspaces console. By default, the
console provides an aggregated view of the most common capacity and traffic related CloudWatch metrics
in the **Capacity and related metrics** section on the **Capacity** tab for the table.

To create your own dashboard using Amazon CloudWatch, check the following Amazon Keyspaces metrics.

- `PerConnectionRequestRateExceeded` – Requests to Amazon Keyspaces that
  exceed the quota for the per-connection request rate. Each client connection to
  Amazon Keyspaces can support up to 3000 CQL requests per second. You can perform more than 3000
  requests per second by creating multiple connections.
- `ReadThrottleEvents` – Requests to Amazon Keyspaces that exceed the read
  capacity for a table.
- `StoragePartitionThroughputCapacityExceeded` – Requests to
  an Amazon Keyspaces storage partition that exceed the throughput capacity of the partition.
  Amazon Keyspaces storage partitions can support up to 1000 WCU/WRU per second and 3000
  RCU/RRU per second. To mitigate these
  exceptions, we recommend that you review your data model to distribute
  read/write traffic across more partitions.
- `WriteThrottleEvents` – Requests to Amazon Keyspaces that exceed the write
  capacity for a table.

To learn more about CloudWatch, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"). For a list of
all available CloudWatch metrics for Amazon Keyspaces, see [Amazon Keyspaces metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md").

###### Note

To get started with a custom dashboard that shows all commonly observed metrics
for Amazon Keyspaces, you can use a prebuilt CloudWatch template available on GitHub in the [AWS samples](https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates "https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates") repository.

###### Topics

- [Client-side
  errors](#troubleshooting.serverless.clientside "#troubleshooting.serverless.clientside")
- [Write timeout errors
  during data import](#troubleshooting.serverless.writetimeout "#troubleshooting.serverless.writetimeout")
- [Keyspace or table
  storage size](#troubleshooting.serverless.storagesize "#troubleshooting.serverless.storagesize")

### I'm receiving

`NoHostAvailable` insufficient capacity errors from my client driver

**You're seeing `Read_Timeout` or `Write_Timeout` exceptions for a table.**

Repeatedly trying to write to or read from an Amazon Keyspaces table with insufficient capacity
can result in client-side errors that are specific to the driver.

Use CloudWatch to monitor your provisioned and actual throughput metrics, and insufficient
capacity events for the table. For example, a read request that doesn’t have enough
throughput capacity fails with a `Read_Timeout` exception and is posted to
the `ReadThrottleEvents` metric. A write request that doesn’t have enough
throughput capacity fails with a `Write_Timeout` exception and is posted to
the `WriteThrottleEvents` metric. For more information about these metrics,
see [Amazon Keyspaces metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md").

To resolve these issues, consider one of the following options.

- Increase the _provisioned throughput_ for the table, which is the maximum
  amount of throughput capacity an application can consume. For more information,
  see [Read capacity units
  and write capacity units](ReadWriteCapacityMode.md#ReadWriteCapacityMode.Provisioned.Units "ReadWriteCapacityMode.md#ReadWriteCapacityMode.Provisioned.Units").
- Let the service manage throughput capacity on your behalf with automatic scaling. For more
  information, see [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md").
- Chose **On-demand** capacity mode for the table. For more information, see
  [Configure on-demand capacity mode](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").

If you need to increase the default capacity quota for your account, see
[Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

**You're seeing errors related to exceeded partition
capacity.**

When you're seeing the error `StoragePartitionThroughputCapacityExceeded` the partition capacity
is temporarily exceeded. This might be automatically handled by adaptive capacity or on-demand capacity. We recommend
reviewing your data model to distribute read/write traffic across more partitions to mitigate these errors. Amazon Keyspaces storage
partitions can support up to 1000 WCU/WRU per second and 3000 RCU/RRU per second.
To learn more about how to improve your data model to distribute
read/write traffic across more partitions, see [Data modeling best practices: recommendations for designing data models](data-modeling.md "data-modeling.md").

`Write_Timeout` exceptions can also be caused by an elevated rate of
concurrent write operations that include static and nonstatic data in the same logical
partition. If traffic is expected to run multiple concurrent write operations that
include static and nonstatic data within the same logical partition, we recommend
writing static and nonstatic data separately. Writing the data separately also helps to
optimize the throughput costs.

**You're seeing errors related to exceeded connection
request rate.**

You're seeing `PerConnectionRequestRateExceeded` due to one of the following causes.

- You might not have enough connections configured per session.
- You might be getting fewer connections than available peers, because you don't
  have the VPC endpoint permissions configured correctly. For more information
  about VPC endpoint policies, see [Using interface VPC endpoints for
  Amazon Keyspaces](vpc-endpoints.md#using-interface-vpc-endpoints "vpc-endpoints.md#using-interface-vpc-endpoints").
- If you're using a 4.x driver, check to see if you have hostname validation
  enabled. The driver enables TLS hostname verification by default. This
  configuration leads to Amazon Keyspaces appearing as a single-node cluster to the driver.
  We recommend that you turn hostname verification off.

We recommend that you follow these best practices to ensure that your connections and
throughput are optimized:

- **Configure CQL query throughput tuning.**

Amazon Keyspaces supports up to 3,000 CQL queries per TCP connection per second, but
there is no limit on the number of connections a driver can establish.

Most open-source Cassandra drivers establish a connection pool to Cassandra
and load balance queries over that pool of connections. Amazon Keyspaces exposes 9 peer IP
addresses to drivers. The default behavior of most drivers is to establish a
single connection to each peer IP address. Therefore, the maximum CQL query
throughput of a driver using the default settings will be 27,000 CQL queries per
second.

To increase this number, we recommend that you increase the number of
connections per IP address that your driver is maintaining in its connection
pool. For example, setting the maximum connections per IP address to 2 will
double the maximum throughput of your driver to 54,000 CQL queries per second.

- **Optimize your single-node connections.**

By default, most open-source Cassandra drivers establish one or more
connections to every IP address advertised in the `system.peers`
table when establishing a session. However, certain configurations can lead to a
driver connecting to a single Amazon Keyspaces IP address. This can happen if the driver is
attempting SSL hostname validation of the peer nodes (for example, DataStax Java
drivers), or when it's connecting through a VPC endpoint.

To get the same availability and performance as a driver with connections to
multiple IP addresses, we recommend that you do the following:

    + Increase the number of connections per IP to 9 or higher depending on
     the desired client throughput.
    + Create a custom retry policy that ensures that retries are run against
     the same node. For more information, see


    [How to configure the retry policy for connections in Amazon Keyspaces](connections.md#connections.retry-policies "connections.md#connections.retry-policies").
    + If you use VPC endpoints, grant the IAM entity that is used to
     connect to Amazon Keyspaces access permissions to query your VPC for the endpoint
     and network interface information. This improves load balancing and
     increases read/write throughput. For more information, see [Populating system.peers table entries with
     interface VPC endpoint information](vpc-endpoints.md#system_peers "vpc-endpoints.md#system_peers").

### I'm receiving write timeout

errors during data import

**You're receiving a timeout error when uploading data using the
`cqlsh`
`COPY` command.**

```
`Failed to import 1 rows: WriteTimeout - Error from server: code=1100 [Coordinator node timed out waiting for replica nodes' responses]
 message="Operation timed out - received only 0 responses." info={'received_responses': 0, 'required_responses': 2, 'write_type': 'SIMPLE', 'consistency':
 'LOCAL_QUORUM'}, will retry later, attempt 1 of 100`
```

Amazon Keyspaces uses the `ReadTimeout` and `WriteTimeout` exceptions to
indicate when a write request fails due to insufficient throughput capacity. To help
diagnose insufficient capacity exceptions, Amazon Keyspaces publishes the following metrics in
Amazon CloudWatch.

- `WriteThrottleEvents`
- `ReadThrottledEvents`
- `StoragePartitionThroughputCapacityExceeded`

To resolve insufficient-capacity errors during a data load, lower the write rate per
worker or the total ingest rate, and then retry to upload the rows. For more
information, see [Step 4: Configure cqlsh COPY FROM
settings](bulk-upload-config.md "bulk-upload-config.md"). For a more robust data upload
option, consider using DSBulk, which is available from the [GitHub repository](https://github.com/datastax/dsbulk "https://github.com/datastax/dsbulk"). For step-by-step
instructions, see [Tutorial: Loading data into Amazon Keyspaces using DSBulk](dsbulk-upload.md "dsbulk-upload.md").

### I can't see the actual storage

size of a keyspace or table

**You can't see the actual storage size of the keyspace or
table.**

To learn more about the storage size of your table, see [Evaluate your costs at the table level](CostOptimization_TableLevelCostAnalysis.md "CostOptimization_TableLevelCostAnalysis.md"). You can also estimate storage
size by starting to calculate the row size in a table. Detailed instructions for
calculating the row size are available at [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md").
