# PostgreSQL Endpoint Troubleshooting

This section contains replication scenarios specific to PostgreSQL.

###### Topics

- [Long-running transaction on source](#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Longrunning "#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Longrunning")
- [High workload on source](#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Highworkload "#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Highworkload")
- [High network throughput](#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Highnetwork "#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Highnetwork")
- [Spill files in
  Aurora PostgreSQL](#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Spill "#CHAP_Troubleshooting_Latency_Source_PostgreSQL_Spill")

## Long-running transaction on source

When there are long-running transactions in the source database, such as a few thousand inserts in a single transaction,
the DMS CDC event and transaction counters do not increase until the transaction is complete. This delay can cause latency
issues that you can measure using the `CDCLatencyTarget` metric.

To review long-running transactions, do one of the following:

- Use the `pg_replication_slots` view. If the `restart_lsn`
  value isn't updating, it is likely that PostgreSQL is unable to release Write Ahead Logs (WALs) due to long-running
  active transactions. For information about the `pg_replication_slots` view, see
  [pg_replication_slots](https://www.postgresql.org/docs/15/view-pg-replication-slots.html "https://www.postgresql.org/docs/15/view-pg-replication-slots.html")
  in the [PostgreSQL 15.4 Documentation](https://www.postgresql.org/docs/15/ "https://www.postgresql.org/docs/15/").
- Use the following query to return a list of all active queries in the database, along with
  related information:

```
SELECT pid, age(clock_timestamp(), query_start), usename, query
FROM pg_stat_activity WHERE query != '<IDLE>'
AND query NOT ILIKE '%pg_stat_activity%'
ORDER BY query_start desc;
```

In the query results, the `age` field shows the active duration of each query, which you can
use to identify long-running queries.

## High workload on source

If your source PostgreSQL has a high workload, check the following to reduce latency:

- You may experience high latency when
  using the `test_decoding` plugin while migrating a subset of tables from the source database
  with a high transactions per second (TPS) value. This is because the `test_decoding` plugin sends all
  database changes to the replication instance which DMS then filters, based on the task’s table mapping.
  Events for tables that aren’t part of the task’s table mapping can increase source latency.
- Check TPS throughput using one of the following methods.
  - For Aurora PostgreSQL sources, use the `CommitThroughput` CloudWatch metric.
  - For PostgreSQL running on Amazon RDS or on-premises, use the following query using a
    PSQL client version 11 or higher (Press `enter` during the query to advance the results):

  ```
  SELECT SUM(xact_commit)::numeric as temp_num_tx_ini FROM pg_stat_database; \gset
  select pg_sleep(60);
  SELECT SUM(xact_commit)::numeric as temp_num_tx_final FROM pg_stat_database; \gset
  select (:temp_num_tx_final - :temp_num_tx_ini)/ 60.0 as "Transactions Per Second";

  ```

- To reduce latency when using the `test_decoding` plugin, consider using the
  `pglogical` plugin instead. Unlike the `test_decoding` plugin, the
  `pglogical` plugin filters write ahead log (WAL) changes at the source,
  and only sends relevant changes to the replication instance. For information about using the
  `pglogical` plugin with AWS DMS, see [Configuring the
  pglogical plugin](CHAP_Source.md#CHAP_Source.PostgreSQL.Security.Pglogical "CHAP_Source.md#CHAP_Source.PostgreSQL.Security.Pglogical").

## High network throughput

Your replication may have high network bandwidth use when using the `test_decoding` plugin,
especially during high-volume transactions.
This is because the `test_decoding` plugin processes changes, and converts them into a
human-readable format that is larger than the original binary format.

To improve performance, consider using the `pglogical` plugin instead, which is a binary plugin.
Unlike the `test_decoding` plugin, the `pglogical` plugin generates binary format output,
resulting in compressed write ahead log (WAL) stream changes.

## Spill files in

Aurora PostgreSQL

In PostgreSQL version 13 and higher, the `logical_decoding_work_mem` parameter determines
the memory allocation for decoding and streaming. For more information about the `logical_decoding_work_mem`
parameter, see [Resource Consumption in PostgreSQL](https://www.postgresql.org/docs/13/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM "https://www.postgresql.org/docs/13/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM") in the [PostgreSQL 13.13 Documentation](https://www.postgresql.org/docs/13/ "https://www.postgresql.org/docs/13/").

Logical replication accumulates changes for all transactions in memory until those transactions commit.
If the amount of data stored across all transactions exceeds the amount
specified by the database parameter `logical_decoding_work_mem`, then DMS spills the transaction data
to disk to release memory for new decoding data.

Long running transactions, or many subtransactions, may result in DMS consuming increased logical decoding memory.
This increased memory use results in DMS creating spill files on disk, which causes high source latency during
replication.

To reduce the impact of an increase in the source workload, do the following:

- Reduce long-running transactions.
- Reduce the number of sub-transactions.
- Avoid performing operations that generate a large burst of log records,
  such as deleting or updating an entire table in a single transaction. Perform operations in smaller batches
  instead.

You can use the following CloudWatch metrics to monitor the workload on the source:

- `TransactionLogsDiskUsage`: The number of bytes currently occupied by the logical WAL.
  This value increases monotonically if logical replication slots are unable to keep up with the pace of new writes,
  or if any long running transactions prevent garbage collection of older files.
- `ReplicationSlotDiskUsage`: The amount of disk space the logical replication slots
  currently use.

You can reduce source latency by tuning the `logical_decoding_work_mem` parameter.
The default value for this parameter is 64 MB. This parameter limits the amount of memory used
by each logical streaming replication connection. We recommend setting the `logical_decoding_work_mem`
value significantly higher than the `work_mem` value to reduce the amount of decoded changes that DMS
writes to disk.

We recommend that you periodically check for spill files, particularly
during periods of heavy migration activity or latency. If DMS is creating a significant number of spill files,
this means that logical decoding isn't operating efficiently, which can increase latency.
To mitigate this, increase the `logical_decoding_work_mem` parameter value.

You can check the current transaction overflow with the `aurora_stat_file` function.
For more information, see
[Adjusting working memory for logical decoding](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.md#AuroraPostgreSQL.BestPractices.Tuning-memory-parameters.logical-decoding-work-mem "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.md#AuroraPostgreSQL.BestPractices.Tuning-memory-parameters.logical-decoding-work-mem") in the
_Amazon Relational Database Service Developer Guide_.
