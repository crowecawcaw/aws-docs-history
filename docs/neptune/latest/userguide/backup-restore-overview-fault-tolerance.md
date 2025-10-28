# Fault tolerance for a Neptune DB cluster

A Neptune DB cluster is fault tolerant by design. The cluster volume spans multiple
Availability Zones in a single AWS Region, and each Availability Zone contains a copy of the
cluster volume data. This functionality means that your DB cluster can tolerate a failure of
an Availability Zone without any loss of data and only a brief interruption of service.

If the primary instance in a DB cluster fails, Neptune automatically fails over to a new
primary instance in one of two ways:

- By promoting an existing Neptune replica to the new primary instance
- By creating a new primary instance
  If the DB cluster has one or more Neptune replicas, then a Neptune replica is
  promoted to the primary instance during a failure event. A failure event results in a brief
  interruption, during which read and write operations fail with an exception. However,
  service is typically restored in less than 120 seconds, and often less than 60 seconds. To
  increase the availability of your DB cluster, we recommend that you create at least one or
  more Neptune replicas in two or more different Availability Zones.

You can customize the order in which your Neptune replicas are promoted to the primary
instance after a failure by assigning each replica a priority. Priorities range from 0 for
the highest priority to 15 for the lowest priority. If the primary instance fails, Neptune
promotes the Neptune replica with the highest priority to the new primary instance. You
can modify the priority of a Neptune replica at any time. Modifying the priority doesn't
trigger a failover.

You can use the AWS CLI to set the failover priority of a DB instance, as follows:

```
aws neptune modify-db-instance --db-instance-identifier `(the instance ID)` --promotion-tier `(the failover priority value)`
```

More than one Neptune replica can share the same priority, resulting in promotion
tiers. If two or more Neptune replicas share the same priority, then Neptune promotes
the replica that is largest in size. If two or more Neptune replicas share the same
priority and size, then Neptune promotes an arbitrary replica in the same promotion tier.

If the DB cluster doesn't contain any Neptune replicas, then the primary instance is
recreated during a failure event. A failure event results in an interruption during which
read and write operations fail with an exception. Service is restored when the new primary
instance is created, which typically takes less than 10 minutes. Promoting a Neptune
replica to the primary instance is much faster than creating a new primary instance.
