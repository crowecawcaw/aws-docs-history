

# Same-region replication
<a name="msk-replicator-same-region"></a>

In same-region replication (SRR), both the source and target MSK clusters are in the same AWS Region. Same-region replication is useful for data aggregation, distributing data to partners, or migrating between clusters.

Key differences from cross-region replication:
+ The source cluster does not require multi-VPC private connectivity.
+ You do not need to attach a resource-based permissions policy to the source cluster.
+ You must provide security groups for both the source and target clusters. The subnets you select for the source and target clusters must be in the same Availability Zones.
+ The source cluster can still be accessed by other clients using the unauthenticated auth type.