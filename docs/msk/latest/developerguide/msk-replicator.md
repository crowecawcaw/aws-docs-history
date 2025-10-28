# What is Amazon MSK Replicator?

Amazon MSK Replicator is an Amazon MSK feature that enables you to reliably replicate data across Amazon MSK clusters in different or the same AWS Region. However, both the source and target clusters must be in the same AWS account. With MSK Replicator, you can easily build regionally resilient streaming applications for increased availability and business continuity. MSK Replicator provides automatic asynchronous replication across MSK clusters, eliminating the need to write custom code, manage infrastructure, or setup cross-region networking.

MSK Replicator automatically scales the underlying resources so that you can replicate
data on-demand without having to monitor or scale capacity. MSK Replicator also
replicates the necessary Kafka metadata including topic configurations, Access Control
Lists (ACLs), and consumer group offsets. If an unexpected event occurs in a region, you
can failover to the other AWS region and seamlessly resume processing.

MSK Replicator supports both cross-region replication (CRR) and same-region
replication (SRR). In cross-region replication, the source and target MSK clusters are
in different AWS Regions. In same-region replication, both the source and target MSK
clusters are in the same AWS Region. You need to create source and target MSK clusters
before using them with MSK Replicator.

###### Note

MSK Replicator supports the following AWS Regions: US East (us-east-1, N. Virginia); US East (us-east-2, Ohio); US West (us-west-2, Oregon); Europe (eu-west-1, Ireland); Europe (eu-central-1, Frankfurt); Asia Pacific (ap-southeast-1, Singapore); Asia Pacific (ap-southeast-2, Sydney), Europe (eu-north-1, Stockholm), Asia Pacific (ap-south-1, Mumbai), Europe (eu-west-3, Paris), South America (sa-east-1, São Paulo), Asia Pacific (ap-northeast-2, Seoul), Europe (eu-west-2, London), Asia Pacific (ap-northeast-1, Tokyo), US West (us-west-1, N. California), Canada (ca-central-1, Central), China (Beijing) (cn-north-1), and China (Ningxia) (cn-northwest-1).

Here are some common uses for Amazon MSK Replicator.

- Build multi-region streaming applications: Build highly available and fault-tolerant streaming applications for increased resiliency without setting up custom solutions.
- Lower latency data access: Provide lower latency data access to consumers in
  different geographic regions.
- Distribute data to your partners: Copy data from one Apache Kafka cluster to
  many Apache Kafka clusters, so that different teams/partners have their own
  copies of data.
- Aggregate data for analytics: Copy data from multiple Apache Kafka clusters into one cluster for easily generating insights on aggregated real-time data.
- Write locally, access your data globally: Set up multi-active replication to automatically
  propagate writes performed in one AWS Region to other Regions for providing
  data at lower latency and cost.
