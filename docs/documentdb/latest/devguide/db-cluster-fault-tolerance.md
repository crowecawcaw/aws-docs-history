# Understanding Amazon DocumentDB cluster fault tolerance

Amazon DocumentDB clusters are fault tolerant by design. Each cluster's volume spans multiple Availability Zones in a single AWS Region, and each Availability Zone contains a copy of the cluster's volume data. This functionality means that your cluster can tolerate an Availability Zone failure without any loss of data and only a brief interruption of service.

If the primary instance in a cluster fails, Amazon DocumentDB automatically performs a failover to a new primary instance in one of two ways:

- By promoting an existing Amazon DocumentDB replica to the new primary instance chosen based on the Promotion Tier setting of each replica, and then creating a replacement for the former primary. A failover to the replica instance typically takes less than 30 seconds. Read and write operations may experience brief interruption during this period. To increase the availability of your cluster, we recommend that you create at least one or more Amazon DocumentDB replicas in two or more different Availability Zones.
- By creating a new primary instance. This only happens if you do not have a replica instance in your cluster and can take a few minutes to complete.
  If the cluster has one or more Amazon DocumentDB replicas, an Amazon DocumentDB replica is promoted to the primary instance during a failure event. A failure event
  results in a brief interruption, during which read and write operations fail with an exception. However, service is typically restored in less than 120
  seconds, and often less than 60 seconds. To increase the availability of your cluster, we recommend that you create at least one or more Amazon DocumentDB
  replicas in two or more different Availability Zones.

You can customize the order in which your Amazon DocumentDB replicas are
promoted to the primary instance after a failure by assigning each
replica a priority. Priorities range from 0 for the highest priority to
15 for the lowest priority. If the primary instance fails, the Amazon DocumentDB
replica with the highest priority is promoted to the new primary
instance. You can modify the priority of an Amazon DocumentDB replica at any time.
Modifying the priority doesn't trigger a failover. You can use the
`modify-db-instance` operation with the
`--promotion-tier` parameter. For more information about
customizing the failover priority of an instance, see [Amazon DocumentDB Failover](failover.md "failover.md").

More than one Amazon DocumentDB replica can share the same priority, resulting in promotion tiers. If two or more Amazon DocumentDB replicas share the same priority,
then the replica that is largest in size is promoted to primary. If two or more Amazon DocumentDB replicas share the same priority and size, an arbitrary replica
in the same promotion tier is promoted.

If the cluster doesn't contain any Amazon DocumentDB replicas, the primary instance is re-created during a failure event. A failure event results in an
interruption, during which read and write operations fail with an exception. Service is restored when the new primary instance is created, which
typically takes less than 10 minutes. Promoting an Amazon DocumentDB replica to the primary instance is much faster than creating a new primary instance.
