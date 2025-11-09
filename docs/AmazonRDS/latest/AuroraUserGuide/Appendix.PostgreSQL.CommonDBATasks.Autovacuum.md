# Determining if

the tables in your database need vacuuming

You can use the following query to show the number of unfrozen transactions in a database.
The `datfrozenxid` column of a database's `pg_database` row is a lower
bound on the normal transaction IDs appearing in that database. This column is the minimum of
the per-table `relfrozenxid` values within the database.

```
SELECT datname, age(datfrozenxid) FROM pg_database ORDER BY age(datfrozenxid) desc limit 20;
```

For example, the results of running the preceding query might be the following.

```
datname    | age
mydb       | 1771757888
template0  | 1721757888
template1  | 1721757888
rdsadmin   | 1694008527
postgres   | 1693881061
(5 rows)
```

When the age of a database reaches 2 billion transaction IDs, transaction ID (XID)
wraparound occurs and the database becomes read-only. You can use this query to produce a
metric and run a few times a day. By default, autovacuum is set to keep the age of
transactions to no more than 200,000,000 ([`autovacuum_freeze_max_age`](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE")).

A sample monitoring strategy might look like this:

- Set the `autovacuum_freeze_max_age` value to 200 million
  transactions.
- If a table reaches 500 million unfrozen transactions, that triggers a low-severity
  alarm. This isn't an unreasonable value, but it can indicate that autovacuum
  isn't keeping up.
- If a table ages to 1 billion, this should be treated as an alarm to take action on. In
  general, you want to keep ages closer to `autovacuum_freeze_max_age` for
  performance reasons. We recommend that you investigate using the recommendations that
  follow.
- If a table reaches 1.5 billion unvacuumed transactions, that triggers a high-severity
  alarm. Depending on how quickly your database uses transaction IDs, this alarm can
  indicate that the system is running out of time to run autovacuum. In this case, we
  recommend that you resolve this immediately.
  If a table is constantly breaching these thresholds, modify your autovacuum parameters
  further. By default, using VACUUM manually (which has cost-based delays disabled) is more
  aggressive than using the default autovacuum, but it is also more intrusive to the system as a
  whole.

We recommend the following:

- Be aware and turn on a monitoring mechanism so that you are aware of the age of your
  oldest transactions.

For information on creating a process that warns you about transaction ID wraparound,
see the AWS Database Blog post [Implement an early warning system for transaction ID wraparound in Amazon RDS for
PostgreSQL](https://aws.amazon.com/blogs/database/implement-an-early-warning-system-for-transaction-id-wraparound-in-amazon-rds-for-postgresql/ "https://aws.amazon.com/blogs/database/implement-an-early-warning-system-for-transaction-id-wraparound-in-amazon-rds-for-postgresql/").

- For busier tables, perform a manual vacuum freeze regularly during a maintenance
  window, in addition to relying on autovacuum. For information on performing a manual
  vacuum freeze, see [Performing a
  manual vacuum freeze](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md").
