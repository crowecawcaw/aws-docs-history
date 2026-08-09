For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Security and access FAQ for Amazon Timestream for InfluxDB 3

Questions about securing your Amazon Timestream for InfluxDB 3 clusters and managing access control. For the complete security guide, see [Overview](timestream-for-influx-security.md "timestream-for-influx-security.md").

**Does InfluxDB 3 run inside my VPC?**

Yes. Amazon Timestream for InfluxDB 3 clusters are deployed within your VPC. You specify VPC subnet IDs and security group IDs when creating a cluster, giving you full control over network access.

**How do I control access to Amazon Timestream for InfluxDB 3 resources?**

Use AWS Identity and Access Management (IAM) to control access to Amazon Timestream API operations, including creating, modifying, and deleting resources such as DB clusters, security groups, and parameter groups. AWS provides managed policies for common access patterns.

**Can I use my own encryption key (CMK) for data at rest?**

Yes. You can specify a customer managed AWS KMS key when creating an InfluxDB 3 cluster. Your key encrypts the Amazon S3 objects that store your database data. If you don't specify a key, data is encrypted with an AWS owned key by default. For details, see [Encrypting resources with customer managed keys](influxdb3-cmk-encryption.md "influxdb3-cmk-encryption.md").

**Can I change the encryption key after cluster creation?**

No. The encryption key can only be specified during cluster creation. To migrate to a different key, create a new cluster with the desired key and migrate your data.

**What happens if I disable or delete my customer managed key?**

The cluster becomes unavailable and read/write operations fail. If you re-enable the key, the cluster automatically recovers. If you permanently delete the key, the data is unrecoverable. Service-managed backups for InfluxDB 3 use a separate key and are not affected.
