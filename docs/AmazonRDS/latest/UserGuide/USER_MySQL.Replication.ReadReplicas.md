# Using cascading read replicas with RDS for MySQL

RDS for MySQL supports cascading read replicas. With _cascading read replicas_, you can scale reads without
adding overhead to your source RDS for MySQL DB instance.

With cascading read replicas, your RDS for MySQL DB instance sends data
to the first read replica in the chain. That read replica then sends data to
the second replica in the chain, and so on. The end result is that all
read replicas in the chain have the changes from the RDS for MySQL DB instance, but without
the overhead solely on the source DB instance.

You can create a series of up to three read replicas in a chain from a source
RDS for MySQL DB instance. For example, suppose that you have an RDS for MySQL DB
instance, `mysql-main`. You can do the following:

- Starting with `mysql-main`, create the first read replica in the chain, `read-replica-1`.
- Next, from `read-replica-1`, create the next read replica in the chain,
  `read-replica-2`.
- Finally, from `read-replica-2`, create the third read replica in the chain, `read-replica-3`.
  You can't create another read replica beyond this third cascading read
  replica in the series for `mysql-main`. A complete series of instances
  from an RDS for MySQL source DB instance through to the end of a series of cascading
  read replicas can consist of at most four DB instances.

For cascading read replicas to work, each source RDS for MySQL DB instance must
have automated backups turned on. To turn on automatic backups on a read replica,
first create the read replica, and then modify the read replica to
turn on automatic backups. For more information, see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").

As with any read replica, you can promote a read replica that's part of a cascade.
Promoting a read replica from within a chain of read replicas removes that replica
from the chain. For example, suppose that you want to move some of the workload from
your `mysql-main` DB instance to a new instance for use by the accounting
department only. Assuming the chain of three read replicas from the example, you
decide to promote `read-replica-2`. The chain is affected as
follows:

- Promoting `read-replica-2` removes it from the replication chain.
  - It is now a full read/write DB instance.
  - It continues replicating to `read-replica-3`, just as it was doing before
    promotion.

- Your `mysql-main` continues replicating to `read-replica-1`.
  For more information about promoting read replicas,
  see [Promoting a read replica to be a standalone
  DB instance](USER_ReadRepl.md "USER_ReadRepl.md").
