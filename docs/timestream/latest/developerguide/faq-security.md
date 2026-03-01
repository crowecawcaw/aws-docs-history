For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Security and access FAQ for Amazon Timestream for InfluxDB 3

Questions about securing your Amazon Timestream for InfluxDB 3 clusters and managing access control. For the complete security guide, see [Overview](timestream-for-influx-security.md "timestream-for-influx-security.md").

**Does InfluxDB 3 run inside my VPC?**

Yes. Amazon Timestream for InfluxDB 3 clusters are deployed within your VPC. You specify VPC subnet IDs and security group IDs when creating a cluster, giving you full control over network access.

**How do I control access to Amazon Timestream for InfluxDB 3 resources?**

Use AWS Identity and Access Management (IAM) to control access to Amazon Timestream API operations, including creating, modifying, and deleting resources such as DB clusters, security groups, and parameter groups. AWS provides managed policies for common access patterns.
