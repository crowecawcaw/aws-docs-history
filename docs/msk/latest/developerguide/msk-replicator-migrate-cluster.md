

# Migrate between Amazon MSK clusters

Amazon MSK Replicator supports migrations between Amazon MSK clusters in the same AWS account. You can use Identical topic name replication for cluster migration, but your consumers must be able to handle duplicate messages without downstream impact. This is because MSK Replicator provides at-least-once replication, which can lead to duplicate messages in rare scenarios. If your consumers meet this requirement, follow these steps.

**Note**  
To move an existing Amazon MSK Provisioned cluster from Standard brokers to Express brokers, you can upgrade the cluster in place instead of migrating to a new cluster. In-place upgrade keeps your cluster endpoints and consumer offsets, so you don't need to reconfigure producers or consumers. In-place upgrade is available for clusters running Apache Kafka version 3.9 with KRaft across three Availability Zones. For more information, see [Upgrade Standard brokers to Express brokers](msk-upgrade-standard-to-express.md).  
If your cluster isn't eligible for in-place upgrade, contact AWS Support or your AWS account team for help migrating to Express brokers.

1. Create a Replicator that replicates data from your old cluster to the new cluster with Replicator's starting position set to *Earliest* and using Identical topic name replication (**Keep the same topics name** in console).

1. Configure cluster-level settings and permissions on the new cluster. You do not need to configure topic-level settings and "literal" read ACLs, as MSK Replicator automatically copies them.

1. Monitor the `MessageLag` metric in Amazon CloudWatch until it reaches 0, which indicates all data has been replicated.

1. After all data has been replicated, stop producers from writing data to the old cluster.

1. Reconfigure those producers to connect to the new cluster and start them.

1. Monitor `MaxOffsetLag` metric for your consumers reading data from the old cluster until it becomes `0`, which indicates all existing data has been processed.

1. Stop consumers that are connecting to the old cluster.

1. Reconfigure consumers to connect to the new cluster and start them.