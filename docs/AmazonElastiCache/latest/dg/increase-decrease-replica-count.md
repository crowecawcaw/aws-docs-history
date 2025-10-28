# Changing the number of replicas

You can dynamically increase or decrease the number of read replicas in your Valkey or Redis OSS replication group using the AWS Management Console, the AWS CLI, or the ElastiCache API. If your replication
group is a Valkey or Redis OSS (cluster mode enabled) replication group, you can choose which shards (node groups) to
increase or decrease the number of replicas.

To dynamically change the number of replicas in your replication group, choose the operation from the
following table that fits your situation.

| To Do This      | For Valkey or Redis OSS (cluster mode enabled)                                                        | For Valkey or Redis OSS (cluster mode disabled)                                                                                                                                                                  |
| --------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add replicas    | [Increasing the number of replicas in a shard](increase-replica-count.md "increase-replica-count.md") | [Increasing the number of replicas in a shard](increase-replica-count.md "increase-replica-count.md") [Adding a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](Replication.md "Replication.md")   |
| Delete replicas | [Decreasing the number of replicas in a shard](decrease-replica-count.md "decrease-replica-count.md") | [Decreasing the number of replicas in a shard](decrease-replica-count.md "decrease-replica-count.md") [Deleting a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](Replication.md "Replication.md") |
