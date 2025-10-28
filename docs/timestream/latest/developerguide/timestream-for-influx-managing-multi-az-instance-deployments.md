For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Multi-AZ DB instance deployments

Amazon Timestream for InfluxDB provides high availability and failover support for DB instances using Multi-AZ deployments with a single standby DB instance. This type of deployment is called a Multi-AZ DB instance deployment. Amazon Timestream for InfluxDB use the Amazon failover technology.

In a Multi-AZ DB instance deployment, Amazon Timestream automatically provisions and maintains a synchronous standby
replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability
Zones to a standby replica to provide data redundancy. Running a DB instance with high availability can enhance
availability during DB instance failure and Availability Zone disruption. For more information on ,
see [AWS Regions and Availability Zones](timestream-for-influxdb.md#timestream-for-influx-dbi-regions "timestream-for-influxdb.md#timestream-for-influx-dbi-regions") .

###### Note

The high availability option isn't a scaling solution for read-only scenarios. You can't use a standby replica to serve read traffic.

Using the Amazon Timestream console, you can create a Multi-AZ DB instance deployment by simply specifying **Create a standby instance**
option in the **Availability and durability configuration** section when creating a DB instance.
You can also specify a Multi-AZ DB instance deployment with the AWS Command Line Interface or Amazon Timestream API. Use the `create-db-instance` or CLI
command, or the `CreateDBInstance` API operation.

DB instances using Multi-AZ DB instance deployments can have increased write and
commit latency compared to a Single-AZ deployment. This can happen because of the synchronous data replication that occurs. You might have a change in latency if your deployment fails over to the standby replica, although AWS is engineered with low-latency network connectivity between . For production workloads, we recommend that you use IOPS Included storage 12K or 16K IOPS for fast,
consistent performance. For more information about DB instance classes, see [DB instance classes](timestream-for-influxdb.md#timestream-for-influx-dbi-classes "timestream-for-influxdb.md#timestream-for-influx-dbi-classes").
