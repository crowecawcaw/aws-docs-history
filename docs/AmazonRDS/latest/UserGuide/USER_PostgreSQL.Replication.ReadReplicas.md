# Using cascading

read replicas with RDS for PostgreSQL

As of version 14.1, RDS for PostgreSQL supports cascading read replicas. With _cascading read replicas_, you can scale reads without adding
overhead to your source RDS for PostgreSQL DB instance. Updates to the WAL log aren't sent by
the source DB instance to each read replica. Instead, each read replica in a cascading
series sends WAL log updates to the next read replica in the series. This reduces the
burden on the source DB instance.

With cascading read replicas, your RDS for PostgreSQL DB instance sends WAL data to the
first read replica in the chain. That read replica then sends WAL data to the second
replica in the chain, and so on. The end result is that all read replicas in the chain
have the changes from the RDS for PostgreSQL DB instance, but without the overhead solely on
the source DB instance.

You can create a series of up to three read replicas in a chain from a source
RDS for PostgreSQL DB instance. For example, suppose that you have an RDS for PostgreSQL 14.1 DB
instance, `rpg-db-main`. You can do the following:

- Starting with `rpg-db-main`, create the first read replica in the
  chain, `read-replica-1`.
- Next, from `read-replica-1`, create the next read replica in the
  chain, `read-replica-2`.
- Finally, from `read-replica-2`, create the third read replica in
  the chain, `read-replica-3`.
  You can't create another read replica beyond this third cascading read replica in
  the series for `rpg-db-main`. A complete series of instances from an
  RDS for PostgreSQL source DB instance through to the end of a series of cascading read
  replicas can consist of at most four DB instances.

For cascading read replicas to work, turn on automatic backups on your RDS for PostgreSQL.
Create the read replica first and then turn on automatic backups on the RDS for PostgreSQL DB
instance. The process is the same as for other Amazon RDS DB engines. For more information,
see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").

As with any read replica, you can promote a read replica that's part of a
cascade. Promoting a read replica from within a chain of read replicas removes that
replica from the chain. For example, suppose that you want to move some of the workload
off of your `rpg-db-main` DB instance to a new instance for use by the
accounting department only. Assuming the chain of three read replicas from the example,
you decide to promote `read-replica-2`. The chain is affected as
follows:

- Promoting `read-replica-2` removes it from the replication
  chain.
  - It is now a full read/write DB instance.
  - It continues replicating to `read-replica-3`, just as it
    was doing before promotion.

- Your `rpg-db-main` continues replicating to
  `read-replica-1`.
  For more information about promoting read replicas, see [Promoting a read replica to be a standalone
  DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

###### Note

- RDS for PostgreSQL doesn't support major version upgrades for cascading
  replicas. Before performing a major version upgrade, you need to remove
  cascading replicas. You can recreate them after completing the upgrade on
  your source DB instance and first-level replicas.
- For cascading read replicas, RDS for PostgreSQL supports 15 read replicas for
  each source DB instance at first level of replication, and 5 read replicas
  for each source DB instance at the second and third level of
  replication.
