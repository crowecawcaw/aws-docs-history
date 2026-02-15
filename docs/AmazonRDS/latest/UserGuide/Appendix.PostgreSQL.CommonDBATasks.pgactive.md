# Handling

conflicts in active-active replication

The `pgactive` extension works per database and not per cluster. Each DB instance
that uses `pgactive` is an independent instance and can accept data changes from
any source. When a change is sent to a DB instance, PostgreSQL commits it locally and then uses
`pgactive` to replicate the change asynchronously to other DB instances. When two
PostgreSQL DB instances update the same record at nearly the same time, a conflict can occur.

The `pgactive` extension provides mechanisms for conflict detection and
automatic resolution. It tracks the time stamp when the transaction was committed on both the
DB instances and automatically applies the change with the latest time stamp. The
`pgactive` extension also logs when a conflict occurs in the
`pgactive.pgactive_conflict_history` table.

The `pgactive.pgactive_conflict_history` will keep growing. You may want to
define a purging policy. This can be done by deleting some records on a regular basis or
defining a partitioning scheme for this relation (and later detach, drop, truncate partitions
of interest). To implement the purging policy on a regular basis, one option is to use the
`pg_cron` extension. See the following information of an example for the
`pg_cron` history table, [Scheduling maintenance with the
PostgreSQL pg_cron extension](PostgreSQL_pg_cron.md "PostgreSQL_pg_cron.md").
