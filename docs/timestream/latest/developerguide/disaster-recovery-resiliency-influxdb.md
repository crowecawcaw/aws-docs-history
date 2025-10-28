For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Resilience in Amazon Timestream for InfluxDB

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

Amazon Timestream for InfluxDB periodically takes internal backups and retains them for 24 hours to support availability and durability.
Snapshots are taken during deletes and retained for 30 days to support restores. To access or use these, file a ticket at [AWS support](https://support.console.aws.amazon.com/support/home?nc2=h_ql_cu#/ "https://support.console.aws.amazon.com/support/home?nc2=h_ql_cu#/").

You can create your instance with Multi-AZ recovery capabilities. For more information, see [Multi-AZ DB instance deployments](timestream-for-influx-managing.md#timestream-for-influx-managing-multi-az-instance-deployments.html "timestream-for-influx-managing.md#timestream-for-influx-managing-multi-az-instance-deployments.html").
