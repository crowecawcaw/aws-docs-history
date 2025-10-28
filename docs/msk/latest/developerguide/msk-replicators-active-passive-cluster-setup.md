# Create an

active-passive Kafka cluster setup with recommended topic naming configurations

For an active-passive setup, we recommend you to operate a similar setup of
producers, MSK clusters, and consumers (with the same consumer group name) in two
different AWS Regions. It is important that the two MSK clusters have identical
read and write capacity to ensure reliable data replication. You need to create a
MSK Replicator to continuously copy data from the primary to the standby cluster.
You also need to configure your producers to write data into topics on a cluster in
the same AWS Region.

For an active-passive setup, create a new Replicator with Identical topic name replication (**Keep the same topics name** in console) to start replicating data from your MSK cluster in the primary region to your cluster in the secondary region. We recommend that you operate a duplicate set of producers and consumers in the two AWS Regions, each connecting to the cluster in their own region using its bootstrap string. This simplifies the failover process since it won’t require changes to the bootstrap string. To ensure that consumers read from near where they left off, consumers in the source and target clusters should have the same consumer group ID.

If you use Identical topic name replication (**Keep the same topics name** in console) for your MSK Replicator, it will replicate your topics with the same name as the corresponding source topics.

We recommend that you configure cluster level settings and permissions for your clients on the target cluster. You do not need to configure topic level settings and literal read ACLs as MSK Replicator automatically copies them if you have selected the option to copy access control lists. See [Metadata replication](msk-replicator-how-it-works.md#msk-replicator-metadata-replication "msk-replicator-how-it-works.md#msk-replicator-metadata-replication").
