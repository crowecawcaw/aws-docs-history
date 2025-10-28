# Architectural differences between Neptune and Neo4j

When customers first consider migrating an application from Neo4j to Neptune, it is often
tempting to perform a like-to-like comparison based on instance size. However, the architectures
of Neo4j and Neptune have fundamental differences. Neo4j is based on an all-in-one approach
where data loading, data ETL, application queries, data storage, and management operations
all happen in the same set of compute resources, such as EC2 instances.

Neptune, by contrast, is an OLTP focused graph database where the architecture
separates responsibilities and where resources are decoupled so they can scale dynamically
and independently.

When migrating from Neo4j to Neptune, determine the data durability, availability and
scalability requirements of your application. Neptune's cluster architecture simplifies
the design of applications that require high durability, availability and scalability.
With an understanding of Neptune's cluster architecture, you can then design a Neptune
cluster topology to satisfy these requirements.

## Neo4j's cluster architecture

Many production applications use Neo4j's [causal
clustering](https://neo4j.com/docs/operations-manual/current/clustering/introduction/ "https://neo4j.com/docs/operations-manual/current/clustering/introduction/") to provide data durability, high availability and scalability. Neo4j's
clustering architecture uses core-server and read-replica instances:

- Core servers provide for data durability and fault tolerance by
  replicating data using the Raft protocol.
- Read replicas use transaction log shipping to asynchronously replicate data
  for high read throughput workloads.

Every instance in a cluster, whether core server or read replica, contains a full
copy of the graph data.

## Neptune's cluster architecture

[A Neptune cluster](feature-overview-db-clusters.md "feature-overview-db-clusters.md") is made up
of a primary writer instance and up to 15 read replica instances. All the instances in
the cluster share the same underlying distributed storage service that is separate
from the instances.

- The primary writer instance coordinates all write operations to the
  database and is vertically scalable to provide flexible support for different write
  workloads. It also supports read operations.
- Read replica instances support read operations from the underlying storage
  volume, and allow you to scale horizontally to support high read workloads.
  They also provide for high availability by serving as failover targets for the
  primary instance.

###### Note

For heavy write workloads, it is best to scale the read replica instances
to the same size as the writer instance, to ensure that the readers can stay
consistent with the data changes.

- The underlying storage volume scales storage capacity automatically as
  the data in your database increases, up to 128 tebibytes (TiB) of storage.

Instance sizes are dynamic and independent. Each instance can be resized while the
cluster is running, and read replicas can be added or removed while the cluster is running.

The [Neptune Serverless](neptune-serverless.md "neptune-serverless.md") feature
can scale your compute capacity up and down automatically as demand rises and falls.
Not only can this decrease your administrative overhead, it also lets you configure
the database to handle large spikes in demand without degrading performance or
requiring you to over-provision.

You can stop a Neptune cluster for up to 7 days.

Neptune also supports [auto-scaling](manage-console-autoscaling.md "manage-console-autoscaling.md"),
to adjust the reader instance sizes automatically based on workload.

Using Neptune's [global database feature](neptune-global-database.md "neptune-global-database.md"),
you can mirror a cluster in up to 5 other regions.

Neptune is also [fault
tolerant by design](backup-restore-overview-fault-tolerance.md "backup-restore-overview-fault-tolerance.md"):

- The cluster volume that provides data storage to all the instances in the
  cluster spans multiple Availability Zones (AZs) in a single AWS Region. Each AZ contains
  a full copy of the cluster data.
- If the primary instance becomes unavailable, Neptune automatically fails over
  to an existing read replica with zero data loss, typically in under 30 seconds. If there are
  no existing read replicas in the cluster, Neptune automatically provisions a new primary
  instance – again, with zero data loss.

What all this means is that when migrating from a Neo4j causal cluster to Neptune, you
don't have to architect the cluster topology explicitly for high data durability and high
availability. This leaves you to size your cluster for expected read and write workloads,
and any increased availability requirements you may have, in just a few ways:

- To scale read operations, [add
  read replica instances](feature-overview-db-clusters.md#feature-overview-read-replicas "feature-overview-db-clusters.md#feature-overview-read-replicas") or enable [Neptune
  Serverless](neptune-serverless.md "neptune-serverless.md") functionality.
- To improve availability, distribute the primary instance and read replicas
  in your cluster over multiple Availability Zones (AZs).
- To reduce any failover time, provision at least one read replica instance
  that can serve as a failover target for the primary. You can determine the order in which
  read replica instances are promoted to primary after a failure by [﻿assigning each replica a priority﻿](manage-console-add-replicas.md "manage-console-add-replicas.md"). It’s a best
  practice to ensure that a failover target has an instance class capable of handling your
  application’s write workload if promoted to primary.
