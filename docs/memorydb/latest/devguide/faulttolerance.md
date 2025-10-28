# Mitigating Failures

When planning your MemoryDB implementation,
you should plan so that failures have a minimal impact upon your application and data.
The topics in this section cover approaches you can take to protect your application and data from failures.

## Mitigating Failures: MemoryDB clusters

A MemoryDB cluster is comprised of a single primary node
which your application can both read from and write to,
and from 0 to 5 read-only replica nodes. However, we highly recommend to use at least 1 replica for high availability.
Whenever data is written to the primary node it is persisted to the transaction log and asynchronously updated on the replica nodes.

###### When a read replica fails

1. MemoryDB detects the failed replica.
2. MemoryDB takes the failed node offline.
3. MemoryDB launches and provisions a replacement node in the same AZ.
4. The new node synchronizes with the transaction log.

During this time your application can continue reading and writing using the other nodes.

###### MemoryDB Multi-AZ

If Multi-AZ is activated on your MemoryDB clusters, a failed primary will be detected and replaced automatically.

######

1. MemoryDB detects the primary node failure.
2. MemoryDB fails over to a replica after ensuring it is consistent with the failed primary.
3. MemoryDB spins up a replica in the failed primary's AZ.
4. The new node syncs with the transaction log.

Failing over to a replica node is generally faster than creating and provisioning a new primary node.
This means your application can resume writing to your primary node sooner.

For more information, see [Minimizing downtime in MemoryDB with Multi-AZ](autofailover.md "autofailover.md").
