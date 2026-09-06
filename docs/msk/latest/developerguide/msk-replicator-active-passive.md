

# Active-passive replication
<a name="msk-replicator-active-passive"></a>

In an active-passive setup, only one MSK cluster at a time is actively serving streaming data, while the other cluster is on standby. Active-passive setups are suited to applications that can run in only one AWS Region at a time, or when you need more control over the data processing order.

For an active-passive setup, we recommend the following:
+ Operate a similar setup of producers, MSK clusters, and consumers (with the same consumer group name) in two different AWS Regions.
+ Ensure that the two MSK clusters have identical read and write capacity for reliable data replication.
+ Create an MSK Replicator to continuously copy data from the primary to the standby cluster.
+ Configure your producers to write data into topics on a cluster in the same AWS Region.

We recommend creating the Replicator with Identical topic name replication (**Keep the same topics name** in console). This simplifies the failover process since it does not require changes to the bootstrap string or topic name reconfigurations. To ensure that consumers read from near where they left off, consumers in the source and target clusters should have the same consumer group ID.

Configure cluster-level settings and permissions for your clients on the target cluster. You do not need to configure topic-level settings and literal read ACLs as MSK Replicator automatically copies them if you have selected the option to copy access control lists. See [Metadata and ACL replication](msk-replicator-metadata-acl.md).