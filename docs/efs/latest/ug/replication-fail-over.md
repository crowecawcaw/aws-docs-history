# Using the replica

In the event of a disaster or when performing game day exercises, you can fail over to your
replica file system by deleting its replication configuration. After the replication
configuration is deleted, the replica becomes writeable and you can start using it in your
application workflow. When the disaster is mitigated or the game day exercise is over, you can
continue using the replica as the primary file system or you can perform a failback to resume
operations on your original primary file system.

During the failback process, you can choose to discard the changes made to your replica file
system or preserve them by copying them back to your primary.

- To discard the changes made to your replica during failover, re-create the original
  replication configuration on your primary file system, where the replica file system is the
  replication destination. During replication, Amazon EFS synchronizes the file systems by updating
  your replica file system's data to match that of your primary.
- To replicate the changes made to your replica during failover, create a replication
  configuration on the replica file system, where the primary file system is the replication
  destination. During replication, Amazon EFS identifies and transfers the differences from your
  replica file system back to the primary file system. Once the replication is complete, you can
  resume replicating the primary file system by re-creating the original replication
  configuration or creating a new configuration.
  The amount of time it takes for Amazon EFS to complete the replication process varies and depends
  on factors such as the size of the file system and the number of files in it. For more
  information, see [Replication performance](efs-replication.md#efs-replication-performance "efs-replication.md#efs-replication-performance").
