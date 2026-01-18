# Distributed deadlocks in Aurora PostgreSQL Limitless Database

In a DB shard group, deadlocks can occur between transactions that are distributed among different routers and shards. For example, two concurrent
distributed transactions that span two shards are run, as shown in the following figure.

![Distributed deadlock on two distributed transactions.](images/limitless_distributed_transaction_deadlock.png)
The transactions lock tables and create wait events in the two shards as follows:

1. Distributed transaction 1:

```
UPDATE `table` SET `value` = 1 WHERE key = '`shard1_key`';
```

This holds a lock on shard 1. 2. Distributed transaction 2:

```
UPDATE `table` SET `value` = 2 WHERE key = '`shard2_key`';
```

This holds a lock on shard 2. 3. Distributed transaction 1:

```
UPDATE `table` SET `value` = 3 WHERE key = '`shard2_key`';
```

Distributed transaction 1 is waiting on shard 2. 4. Distributed transaction 2:

```
UPDATE `table` SET `value` = 4 WHERE key = '`shard1_key`';
```

Distributed transaction 2 is waiting on shard 1.
In this scenario, neither shard 1 nor shard 2 sees the problem: transaction 1 is waiting for transaction 2 on shard 2, and transaction 2 is
waiting for transaction 1 on shard 1. From a global view, transaction 1 is waiting for transaction 2, and transaction 2 is waiting for transaction

1.  This situation where two transactions on two different shards are waiting for each other is called a distributed deadlock.

Aurora PostgreSQL Limitless Database can detect and resolve distributed deadlocks automatically. A router in the DB shard group is notified when a transaction is waiting too
long to acquire a resource. The router receiving the notification starts to collect the necessary information from all of the routers and shards
within the DB shard group. The router then proceeds to end transactions that are participating in a distributed deadlock, until the rest of the
transactions in the DB shard group can proceed without being blocked by each other.

You receive the following error when your transaction was part of a distributed deadlock, and was then ended by the router:

```
ERROR: aborting transaction participating in a distributed deadlock
```

The `rds_aurora.limitless_distributed_deadlock_timeout` DB cluster parameter sets the time for each transaction to wait on a resource before
notifying the router to check for a distributed deadlock. You can increase the parameter value if your workload is less prone to deadlock
situations. The default is `1000` milliseconds (1 second).

The distributed deadlock cycle is published to the PostgreSQL logs when a cross-node deadlock is found and resolved. The information about each
process that's part of the deadlock includes the following:

- Coordinator node that started the transaction
- Virtual transaction ID (xid) of the transaction on the coordinator node, in the format
  ``backend_id`/`backend_local_xid``
- Distributed session ID of the transaction
