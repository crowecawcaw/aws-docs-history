# Instance-specific performance and resource monitoring

Monitoring on instance level is key to understand connection skew, workload skew and data skew, as well as when to add routers or split shards to scale up for higher throughput with retained latency.

## Overview

When your application issues a query against , that request traverses a sophisticated distributed system before returning results. A seemingly simple `SELECT` statement might touch multiple database instances, each playing a distinct role in processing your request. Understanding this journey—and the instances that power it—transforms how you design applications, interpret monitoring data, and diagnose performance issues.

This guide provides deep technical insight into instance architecture:

- Limitless Architecture refresher, router and shards
- When and how to scale each instance type to meet your performance and capacity requirements
- How to monitor, troubleshoot, and optimize instance-level performance
- Best practices for application design that leverage the distributed architecture effectively

## Instance architecture fundamentals

achieves horizontal scalability through functional separation across two specialized instance types:

- **Router instances** provide the orchestration layer—they accept client connections, analyze queries, coordinate distributed operations, and aggregate results. Routers are stateless, meaning they don't store data and can be added or removed without data migration.
- **Shard instances** provide the data and compute layer—they store table data, execute queries against local data, and handle transactions. Shards are stateful, each owning a specific subset of your data determined by consistent hashing.

This separation allows to scale connection handling, query coordination, and data storage independently based on your workload characteristics.

### Router and shard comparison

| Characteristic  | Router Instances                            | Shard Instances                         |
| --------------- | ------------------------------------------- | --------------------------------------- |
| Primary Role    | Query coordination and distribution         | Data storage and query execution        |
| State           | Stateless (no data storage)                 | Stateful (owns data)                    |
| Scalability     | Add/remove instantly                        | Requires data rebalancing               |
| Resource Focus  | CPU for coordination; moderate memory       | CPU for queries; high memory for cache  |
| Scaling Trigger | High connection count, distributed txn rate | High CPU, data volume, query throughput |

## Monitoring instance performance

Understanding instance-level performance is critical for operating effectively. Instance-specific monitoring reveals the distribution patterns that impact performance: connection skew, workload skew, and data skew.

### Detecting skew

In an ideal deployment, workload and resources distribute evenly across instances. In practice, applications frequently experience skew—uneven distribution that concentrates load on specific instances.

Three types of skew to monitor:

- **Connection skew**: Uneven distribution of client connections across routers
- **Workload skew**: Uneven query load across shards due to hot shard keys
- **Data skew**: Uneven data volume across shards due to shard key frequency

### Database Insights load distribution

The fastest way to assess instance-level health is Database Insights' Load Distribution view, which provides immediate visibility into how Active Sessions distribute across instances.

To access Load Distribution:

1. Navigate to RDS Console → Your Limitless Cluster
2. Select "Performance Insights" tab
3. Click "Load Distribution" section

**Healthy pattern:** Load distributed relatively evenly across instances

- Routers may show slightly higher AAS than shards (coordination overhead)
- Shard AAS values within 20% of each other indicates good balance

**Concerning pattern:** Significant concentration on specific instances

- One router with >70% of router load → Connection skew
- One shard with >50% of shard load → Workload or data skew
- Large variance between shards → Investigate shard key distribution

### CloudWatch metrics

For deeper analysis beyond Database Insights, CloudWatch provides instance-specific metrics that reveal resource utilization patterns.

The `ServerlessDatabaseCapacity` metric with dimension `DBShardGroupInstance` shows ACU consumption per instance, providing the most direct view of resource utilization.

**When to investigate:**

- Router ACU variance >30% → Connection skew or cross-shard workload concentration
- Shard ACU variance >40% → Data or workload skew
- Any instance consistently at max ACU → Capacity constraint

## Router monitoring and troubleshooting

Routers can experience performance issues from two primary causes: uneven connection distribution and cross-shard workload concentration.

### Unevenly distributed sessions

**Symptom:** One router handles disproportionate share of connections

**Root cause:** DNS caching causes multiple connection requests to resolve to the same router endpoint.

**Most common during:**

- Benchmarking with tools like pgbench
- Connection pool initialization (many connections established rapidly)
- Application server restarts

**Remedies:**

- Make sure to use the Limitless endpoint specified in the console
- Manual balancing: extract router endpoints and connect different applications to different routers
- For libpq applications use the feature `LOADBALANCEHOSTS`
- For JDBC applications use the Limitless connection Plugin
- Use an NLB to manage sessions and distributions

## Shard monitoring and troubleshooting

Shards experience performance issues from three primary causes: resource constraints, data skew, and workload skew.

### Shard resource utilization

A shard with popular shard keys will have more data and higher workloads. This manifests as resource utilization, i.e. the instance will consume more ACUs.

**Remediation strategies:**

1. **Re-assess shard key selection:** Review shard key cardinality and access patterns. Consider composite shard keys for better distribution.
2. **Split the shard:** Distribute load across more shard instances

**When to split shards:**

- Single shard consistently at >80% max ACU
- Query throughput limited by single shard capacity

### Shard data volumes

Use SQL functions to query data volumes:

```

SELECT subcluster_id, subcluster_type, pg_size_pretty(db_size)
FROM rds_aurora.limitless_stat_database_size('postgres_limitless')
ORDER BY 1;

```

To view per-table and per-shard data:

```

SELECT * FROM rds_aurora.limitless_stat_relation_sizes('public', 'table_name');

```

### Resolving uneven utilization

When workload or data skew concentrates on specific shards, splitting shards redistributes load across more instances.

Important considerations:

- Which shard keys to move cannot be controlled
- There is no way of undoing a split without recovering to a manual snapshot taken before the split
- All instances, including a new shard, consume instance minimum ACU when idling

Splitting shards allow further scaling, and consecutive shard splits is the path to higher throughput and further scaling, while retaining low latency.

## Limitations

Be aware of these operational constraints:

**Router limitations:**

- **Routers cannot be removed** - Once added, routers remain in cluster
- Plan router additions carefully to avoid unnecessary baseline costs

**Shard limitations:**

- **Shards cannot be merged** - Shard splits are one-way operations
- Only recovery option: Restore from snapshot taken before split

**Mitigation strategies:**

- Start with minimum viable instance count
- Add capacity incrementally as needed
- Take snapshots before major topology changes
- Monitor baseline costs as cluster grows
