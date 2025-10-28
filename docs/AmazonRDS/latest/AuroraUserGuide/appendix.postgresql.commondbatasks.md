# Understanding the behavior of

autovacuum with invalid databases

A new value `-2` is introduced into the `datconnlimit` column in the
`pg_database` catalog to indicate databases that have been interrupted in the
middle of the DROP DATABASE operation as invalid.

This new value is available from the following Aurora PostgreSQL versions:

- 15.4 and all higher versions
- 14.9 and higher versions
- 13.12 and higher versions
- 12.16 and higher versions
- 11.21 and higher versions
  Invalid databases do not affect autovacuum's ability to freeze functionality for valid
  databases. Autovacuum ignores invalid databases. Consequently, regular vacuum operations will
  continue to function properly and efficiently for all valid databases in your PostgreSQL
  environment.

###### Topics

- [Monitoring
  transaction ID](#appendix.postgresql.commondbatasks.autovacuum.monitorxid "#appendix.postgresql.commondbatasks.autovacuum.monitorxid")
- [Adjusting the
  monitoring query](#appendix.postgresql.commondbatasks.autovacuum.monitoradjust "#appendix.postgresql.commondbatasks.autovacuum.monitoradjust")
- [Resolving invalid
  database issue](#appendix.postgresql.commondbatasks.autovacuum.connissue "#appendix.postgresql.commondbatasks.autovacuum.connissue")

## Monitoring

transaction ID

The `age(datfrozenxid)` function is commonly used to monitor the transaction
ID (XID) age of databases to prevent transaction ID wraparound.

Since invalid databases are excluded from autovacuum, their transaction ID (XID) counter
can reach the maximum value of `2 billion`, wrap around to `- 2
 billion`, and continue this cycle indefinitely. A typical query to monitor Transaction
ID wraparound might look like:

```
SELECT max(age(datfrozenxid)) FROM pg_database;
```

However, with the introduction of the -2 value for `datconnlimit`, invalid
databases can skew the results of this query. Since these databases are not valid and should
not be part of regular maintenance checks, they can cause false positives, leading you to
believe that the `age(datfrozenxid)` is higher than it actually is.

## Adjusting the

monitoring query

To ensure accurate monitoring, you should adjust your monitoring query to exclude invalid
databases. Follow this recommended query:

```

SELECT
    max(age(datfrozenxid))
FROM
    pg_database
WHERE
    datconnlimit <> -2;

```

This query ensures that only valid databases are considered in the
`age(datfrozenxid)` calculation, providing a true reflection of the transaction
ID age across your PostgreSQL environment.

## Resolving invalid

database issue

When attempting to connect to an invalid database, you may encounter an error message
similar to the following:

```

postgres=> \c db1
connection to server at "mydb.xxxxxxxxxx.us-west-2.rds.amazonaws.com" (xx.xx.xx.xxx), port xxxx failed: FATAL:  cannot connect to invalid database "db1"
HINT:  Use DROP DATABASE to drop invalid databases.
Previous connection kept

```

Additionally, if the `log_min_messages` parameter is set to
`DEBUG2` or higher, you may notice the following log entries indicating that the
autovacuum process is skipping the invalid database:

```

       `2024-07-30 05:59:00 UTC::@:[32000]:DEBUG: autovacuum: skipping invalid database "db6"
2024-07-30 05:59:00 UTC::@:[32000]:DEBUG: autovacuum: skipping invalid database "db1"`

```

To resolve the issue, follow the `HINT` provided during the connection attempt.
Connect to any valid database using your RDS master account or a database account with the
`rds_superuser` role, and drop invalid database(s).

```

SELECT
    'DROP DATABASE ' || quote_ident(datname) || ';'
FROM
    pg_database
WHERE
    datconnlimit = -2 \gexec

```
