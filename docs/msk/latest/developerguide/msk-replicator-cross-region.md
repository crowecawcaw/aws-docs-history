

# Cross-region replication
<a name="msk-replicator-cross-region"></a>

In cross-region replication (CRR), the source and target MSK clusters are in different AWS Regions. Cross-region replication is the foundation for building multi-region resilient streaming applications.

Key requirements for cross-region replication:
+ The source cluster must have multi-VPC private connectivity turned on for IAM access control. See [Cluster owner turns on multi-VPC](mvpc-cluster-owner-action-turn-on.md).
+ You must attach a resource-based permissions policy to the source cluster. See [Prepare the source cluster](msk-replicator-prepare-clusters.md#msk-replicator-prepare-source).
+ You do not need to provide security groups for the source cluster.
+ The Replicator is created in the target cluster's AWS Region.

Replication latency varies based on the network distance between the AWS Regions, the throughput capacity of your clusters, and the number of partitions. For example, replication latency is typically lower between Europe (Ireland) and Europe (London) compared to Europe (Ireland) and Asia Pacific (Sydney).