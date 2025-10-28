# Troubleshooting common errors when using the

Spark Cassandra Connector with Amazon Keyspaces

If you're using Amazon Virtual Private Cloud and you connect to Amazon Keyspaces, the most common errors experienced when using the Spark connector are caused by the following
configuration issues.

- The IAM user or role used in the VPC lacks the required permissions to access the `system.peers` table in Amazon Keyspaces. For more
  information, see [Populating system.peers table entries with
  interface VPC endpoint information](vpc-endpoints.md#system_peers "vpc-endpoints.md#system_peers").
- The IAM user or role lacks the required read/write permissions to the user table and read
  access to the system tables in Amazon Keyspaces. For more information, see [Step 1: Configure Amazon Keyspaces for integration with the
  Apache Cassandra Spark Connector](spark-tutorial-step1.md "spark-tutorial-step1.md").
- The Java driver configuration doesn't disable hostname verification when creating the SSL/TLS
  connection. For examples, see [Step 2: Configure the
  driver](using_java_driver.md#java_tutorial.driverconfiguration "using_java_driver.md#java_tutorial.driverconfiguration").
  For detailed connection troubleshooting steps, see [My VPC endpoint connection doesn't work properly](troubleshooting.md#troubleshooting.connection.vpce "troubleshooting.md#troubleshooting.connection.vpce").

In addition, you can use Amazon CloudWatch metrics to help you troubleshoot issues with your Spark
Cassandra Connector configuration in Amazon Keyspaces. To learn more about using Amazon Keyspaces with
CloudWatch, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

The following section describes the most useful metrics to observe when you're
using the Spark Cassandra Connector.

**PerConnectionRequestRateExceeded**

Amazon Keyspaces has a quota of 3,000 requests per second, per connection. Each Spark
executor establishes a connection with Amazon Keyspaces. Running multiple retries can
exhaust your per-connection request rate quota. If you exceed this quota,
Amazon Keyspaces emits a `PerConnectionRequestRateExceeded` metric in CloudWatch.

If you see PerConnectionRequestRateExceeded events present along with
other system or user errors, it's likely that Spark is running multiple
retries beyond the allotted number of requests per connection.

If you see `PerConnectionRequestRateExceeded` events without
other errors, then you might need to increase the number of connections in
your driver settings to allow for more throughput, or you might need to
increase the number of executors in your Spark job.

**StoragePartitionThroughputCapacityExceeded**

Amazon Keyspaces has a quota of 1,000 WCUs or WRUs per second/3,000 RCUs or RRUs per
second, per-partition. If you're seeing
`StoragePartitionThroughputCapacityExceeded` CloudWatch events, it
could indicate that data is not randomized on load. For examples how to
shuffle data, see [Step 4: Prepare the source data and the target
table in Amazon Keyspaces](spark-tutorial-step4.md "spark-tutorial-step4.md").

## Common errors and warnings

If you're using Amazon Virtual Private Cloud and you connect to Amazon Keyspaces, the Cassandra driver might
issue a warning message about the control node itself in the
`system.peers` table. For more information, see [Common errors and warnings](vpc-endpoints.md#vpc_troubleshooting "vpc-endpoints.md#vpc_troubleshooting"). You can safely ignore this warning.
