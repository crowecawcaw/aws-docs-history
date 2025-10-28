# Supported cluster

types and versions for MSK Replicator

These are requirements for supported instance types, Kafka versions, and network configurations.

- MSK Replicator supports both MSK provisioned clusters and MSK Serverless clusters in any combination as source and target clusters. Other types of Kafka clusters are not supported at this time by MSK Replicator.
- MSK Serverless clusters require IAM access control, don't support Apache Kafka ACL replication and with limited support on-topic configuration replication. See [What is MSK Serverless?](serverless.md "serverless.md").
- MSK Replicator is supported only on clusters running Apache Kafka 2.7.0 or higher, regardless of whether your source and target clusters are in the same or in different AWS Regions.
- MSK Replicator supports clusters using instance types of m5.large or larger. t3.small clusters aren't supported.
- If you are using MSK Replicator with an MSK Provisioned cluster, you need
  a minimum of three brokers in both source and target clusters. You can
  replicate data across clusters in two Availability Zones, but you would need
  a minimum of four brokers in those clusters.
- Both your source and target MSK clusters must be in the same AWS account. Replication across clusters in different accounts is not supported.
- If the source and target MSK clusters are in different AWS Regions (cross-region), MSK Replicator requires the source cluster to have multi-VPC private connectivity turned on for its IAM Access Control method.

Multi-VPC isn't required for other authentication methods on the source cluster for MSK replication across AWS Regions.

Multi-VPC is also not required if you're replicating data between clusters in the same AWS Region. See [Amazon MSK multi-VPC private connectivity in a single Region](aws-access-mult-vpc.md "aws-access-mult-vpc.md").

- Identical topic name replication (**Keep the same topics name** in console) requires an MSK cluster running Kafka version 2.8.1 or higher.
- For Identical topic name replication (**Keep the same topics name** in console) configurations, to avoid the risk of cyclic replication, do not make changes to the headers that MSK Replicator creates (`__mskmr`).
