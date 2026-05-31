# Amazon DocumentDB elastic cluster best practices

Learn best practices for working with Amazon DocumentDB elastic clusters.
All [best practices for instance-based Amazon DocumentDB clusters](best_practices.md "best_practices.md") also apply for elastic clusters.
This section is continually updated as new best practices are identified.

###### Topics

- [Choosing shard keys](#choosing-shard-keys "#choosing-shard-keys")
- [Connection management](#connection-management "#connection-management")
- [Unsharded collections](#unsharded-collections "#unsharded-collections")
- [Scaling elastic clusters](#scaling "#scaling")
- [Monitoring elastic clusters](#monitoring-elastic-clusters "#monitoring-elastic-clusters")

## Choosing shard keys

The following list describes guidelines for creating shard keys.

- Use an evenly distributed hash key to distribute your data across all of the shards in your cluster (avoid hot keys).
- Use your shard key in all read/update/delete requests to avoid scatter gather queries.
- Avoid nested shard keys when doing read/update/delete operations.
- When making batch operations, set `ordered` to false so all shards can run in parallel and improve latencies.

## Connection management

The following list describes guidelines for managing your connections to your database.

- Monitor your connection counts and how frequently new connections are opened closed.
- Distribute your connections across all of the subnets in your application's configuration.
  If your cluster is configured in multiple subnets but you only utilize a subset of the subnets, you may be bottlenecked on your maximum connections.

## Unsharded collections

The following describes a guideline for unsharded collections.

- When working with unsharded collections, to distribute load, try keeping highly utilized unsharded collections on different databases.
  Amazon DocumentDB elastic clusters place databases across different shards and co-locates unsharded collections for the same database on the same shard.

## Scaling elastic clusters

The following list describes guidelines for scaling your elastic clusters.

- Scaling operations may cause a brief period of intermittent database and network errors.
  When possible, avoid scaling during peak hours. Try to scale during maintenance windows.
- Scaling shard capacity up and down (changing vCPU count per shard) to increase compute is preferred over increasing or decreasing the shard-count as it is faster and has a shorter duration of intermittent database and network errors.
- When anticipating growth, favor increasing the shard count instead scaling the shard capacity.
  This enables you to scale your cluster by increasing the shard capacity for scenarios where you need to quickly scale.
- Monitor your client-side retry policies and retry with exponential backoff and jitter to avoid overloading your database when getting errors while scaling.

## Monitoring elastic clusters

The following list describes guidelines for monitoring your elastic clusters.

- Track the peak-to-average ratio of your per-shard metrics to determine if you are driving un-even traffic (have a hot-key/hot-spot).
  Key metrics to track peak-to-average ratios are:
  - `PrimaryInstanceCPUUtilization`
    - This can be monitored at the per-shard level.
    - At the cluster level you can monitor the average to p99 skew.

  - `PrimaryInstanceFreeableMemory`
    - This can be monitored at the per-shard level.
    - At the cluster level you can monitor the average to p99 skew.

  - `DatabaseCursorsMax`
    - This should be monitored at the per-shard level to determine skew.

  - `Documents-Inserted/Updated/Returned/Deleted`
    - This should be monitored at the per-shard level to determine skew.
