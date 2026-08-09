# Managing reserved memory for Valkey and Redis OSS

Each host type has an amount of memory dedicated for Valkey and Redis OSS. This is the
advertised memory. The `reserved-memory-percent` parameter sets aside part
of this memory for nondata uses:

- Client output buffers on replicas
- Memory lost to fragmentation
- Copy-on-write memory used by forked bgsave
  The `maxmemory` value equals the advertised memory minus the reserve.
  For example, with 13.5 GB of advertised memory and a 25% reserve, the
  `maxmemory` is about 10.1 GB.

###### Important

The `reserved-memory-percent` defaults to 25%. Do not reduce this
value. A lower reserve can cause data loss, especially during upgrades or other
changes to your cluster.

###### Topics

- [How much memory to reserve](#redis-memory-management-how-much "#redis-memory-management-how-much")
- [Configuring reserved memory](#redis-memory-management-configure "#redis-memory-management-configure")

## How much memory to reserve

The `reserved-memory-percent` parameter defaults to 25%. Do not
reduce this value. However, there are situations where you can benefit from
increasing the memory reserve.

Micro and small instances

The micro and small instances are sized for light activity without
the burden of replication. To improve operational reliability of these
instances for production workloads, increase the memory reserve to 30%
on small instances and 50% on micro instances.

Forcing a forked bgsave or full sync

During a traditional forked bgsave or full sync,
Valkey and Redis OSS memory usage can
double (or more), depending on the traffic load and pattern. If
`FreeableMemory` is insufficient to run a traditional
forked operation, Amazon ElastiCache automatically switches to a forkless save
mechanism. This forkless mechanism uses much less memory, but can add
client latencies — especially with very large key/value items.
If these latencies are impactful for your use case, increase the
memory reserve to ensure enough memory for a traditional forked
save.

If instructed by AWS Support

Unusual traffic patterns or requirements can result in unique memory
needs. Increase `reserved-memory-percent` if directed by
AWS Support.

## Configuring reserved memory

The `reserved-memory-percent` parameter is specific to ElastiCache. It isn't
part of the Valkey or Redis OSS open source code. To change this value, use a custom
parameter group. You can't modify default parameter groups.

If 25% works for you, no changes are needed. To use a different value, follow these
steps.

###### To change the reserved-memory-percent value

1. Run the following AWS CLI command to create a custom parameter group. Set the family
   to match your engine version. For more information about creating parameter groups,
   see [Creating an ElastiCache parameter group](ParameterGroups.Creating.md "ParameterGroups.Creating.md").

```
aws elasticache create-cache-parameter-group \
   --cache-parameter-group-name `my-parameter-group` \
   --description "`Custom reserved memory settings`" \
   --cache-parameter-group-family `redis7`
```

You need only one custom parameter group per engine family. The percent value
works the same for all node types. 2. Set `reserved-memory-percent` to the value you want. For more
information about modifying parameter groups, see [Modifying an ElastiCache parameter group](ParameterGroups.Modifying.md "ParameterGroups.Modifying.md").

```
aws elasticache modify-cache-parameter-group \
   --cache-parameter-group-name `my-parameter-group` \
   --parameter-name-values "ParameterName=reserved-memory-percent, ParameterValue=`30`"
```

3. Apply the custom parameter group to your cluster or replication group.

To modify a cluster, run the following AWS CLI command. For more information
about modifying clusters, see [Modifying an ElastiCache cluster](Clusters.Modify.md "Clusters.Modify.md").

```
aws elasticache modify-cache-cluster \
   --cache-cluster-id `my-cluster` \
   --cache-parameter-group-name `my-parameter-group` \
   --apply-immediately
```

To modify a replication group, run the following AWS CLI command. For more
information about modifying replication groups, see [Modifying a replication group](Replication.Modify.md "Replication.Modify.md").

```
aws elasticache modify-replication-group \
   --replication-group-id `my-replication-group` \
   --cache-parameter-group-name `my-parameter-group` \
   --apply-immediately
```
