# Managing serverless resources in

Amazon Keyspaces (for Apache Cassandra)

Amazon Keyspaces (for Apache Cassandra) is serverless. Instead of deploying, managing, and maintaining storage and
compute resources for your workload through nodes in a cluster, Amazon Keyspaces allocates storage and
read/write throughput resources directly to tables.

Amazon Keyspaces provisions storage automatically based on the data stored
in your tables. It scales storage up and down as you write, update, and delete data, and you pay only for the storage you
use. Data is replicated across multiple [Availability
Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") for high availability. Amazon Keyspaces monitors the size of your tables continuously to determine your storage charges.
For more information about how Amazon Keyspaces calculates the billable size of the data, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md").

This chapter covers key aspects of resource management in Amazon Keyspaces.

- **Estimate row size** – To estimate the encoded size of rows in Amazon Keyspaces, consider factors like
  partition key metadata, clustering column metadata, column identifiers, data types, and row metadata. This encoded row size is used for billing,
  quota management, and provisioned throughput capacity planning.
- **Estimate capacity consumption** – This section covers examples of how to estimate read and write
  capacity consumption for common scenarios like range queries, limit queries, table scans, lightweight transactions, static columns, and multi-Region tables.
  You can use Amazon CloudWatch to monitor actual capacity utilization. For more information about monitoring with CloudWatch, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Configure read/write capacity modes** – You can choose between two capacity modes for processing
  reads and writes on your tables:
  - **On-demand mode (default)** – Pay per request for read and write throughput.
    Amazon Keyspaces can instantly scale capacity
    up to any previously reached traffic level.
  - **Provisioned mode** – Specify the required number of read and write capacity
    units in advance. This
    mode helps maintain predictable throughput performance.

- **Manage throughput capacity with automatic scaling** – For provisioned tables, you can enable automatic scaling to adjust
  throughput capacity automatically based on actual application traffic.
  Amazon Keyspaces uses target tracking to increase or decrease provisioned capacity, keeping utilization at your specified target.
- **Use burst capacity effectively** – Amazon Keyspaces provides burst capacity by reserving a portion of unused
  throughput for handling spikes in traffic. This flexibility allows occasional bursts of activity beyond your provisioned throughput.
  To troubleshoot capacity errors, see [Serverless capacity errors](troubleshooting.md#troubleshooting-serverless "troubleshooting.md#troubleshooting-serverless").

###### Topics

- [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md")
- [Estimate capacity consumption of read and write throughput in Amazon Keyspaces](capacity-examples.md "capacity-examples.md")
- [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md")
- [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md")
- [Use burst
  capacity effectively in Amazon Keyspaces](throughput-bursting.md "throughput-bursting.md")
