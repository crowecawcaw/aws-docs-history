# The InnoDB history list length increased

significantly

Starting on `date`, your history list for row changes increased
significantly, up to `length` on
`db-instance`. This increase affects query and database
shutdown performance.

###### Topics

- [Supported engine
  versions](#proactive-insights.history-list.context.supported "#proactive-insights.history-list.context.supported")
- [Context](#proactive-insights.history-list.context "#proactive-insights.history-list.context")
- [Likely causes for this
  issue](#proactive-insights.history-list.causes "#proactive-insights.history-list.causes")
- [Actions](#proactive-insights.history-list.actions "#proactive-insights.history-list.actions")
- [Relevant metrics](#proactive-insights.history-list.metrics "#proactive-insights.history-list.metrics")

## Supported engine

versions

This insight information is supported for all versions of Aurora MySQL.

## Context

The InnoDB transaction system maintains multiversion concurrency control (MVCC). When
a row is modified, the pre-modification version of the data being modified is stored as
an undo record in an undo log. Every undo record has a reference to its previous redo
record, forming a linked list.

The _InnoDB history list_ is a global list of the undo logs for
committed transactions. MySQL uses the history list to purge records and log pages when
transactions no longer require the history. The _history list
length_ is the total number of undo logs that contain modifications in
the history list. Each log contains one or more modifications. If the InnoDB history
list length grows too large, indicating a large number of old row versions, queries and
database shutdowns become slower.

## Likely causes for this

issue

Typical causes of a long history list include the following:

- Long-running transactions, either read or write
- A heavy write load

## Actions

We recommend different actions depending on the causes of your insight.

###### Topics

- [Don't begin
  any operation involving a database shutdown until the InnoDB history list
  decreases](#proactive-insights.history-list.actions.no-shutdown "#proactive-insights.history-list.actions.no-shutdown")
- [Identify and end
  long-running transactions](#proactive-insights.history-list.actions.long-txn "#proactive-insights.history-list.actions.long-txn")
- [Identify the top
  hosts and top users by using Performance Insights.](#proactive-insights.history-list.actions.top-PI "#proactive-insights.history-list.actions.top-PI")

### Don't begin

any operation involving a database shutdown until the InnoDB history list
decreases

Because a long InnoDB history list slows database shutdowns, reduce the list size
before initiating operations involving a database shutdown. These operations include
major version database upgrades.

### Identify and end

long-running transactions

You can find long-running transactions by querying
`information_schema.innodb_trx`.

###### Note

Make sure also to look for long-running transactions on read replicas.

###### To identify and end long-running transactions

1. In your SQL client, run the following query:

```
SELECT a.trx_id,
      a.trx_state,
      a.trx_started,
      TIMESTAMPDIFF(SECOND,a.trx_started, now()) as "Seconds Transaction Has Been Open",
      a.trx_rows_modified,
      b.USER,
      b.host,
      b.db,
      b.command,
      b.time,
      b.state
FROM  information_schema.innodb_trx a,
      information_schema.processlist b
WHERE a.trx_mysql_thread_id=b.id
  AND TIMESTAMPDIFF(SECOND,a.trx_started, now()) > 10
ORDER BY trx_started
```

2. End each long-running transaction with the stored procedure [mysql.rds_kill](mysql-stored-proc-ending.md#mysql_rds_kill "mysql-stored-proc-ending.md#mysql_rds_kill").

### Identify the top

hosts and top users by using Performance Insights.

Optimize transactions so that large numbers of modified rows are immediately
committed.

## Relevant metrics

The following metrics are related to this insight:

- `trx_rseg_history_len` – This counter metric can be viewed
  in Performance Insights, as well as the `INFORMATION_SCHEMA.INNODB_METRICS` table.
  For more information, see [InnoDB INFORMATION_SCHEMA metrics table](https://dev.mysql.com/doc/refman/8.0/en/innodb-information-schema-metrics-table.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-information-schema-metrics-table.html") in the MySQL
  documentation.
- `RollbackSegmentHistoryListLength` – This Amazon CloudWatch metric
  measures the undo logs that record committed transactions with delete-marked
  records. These records are scheduled to be processed by the InnoDB purge
  operation. The metric `trx_rseg_history_len` has the same value as
  `RollbackSegmentHistoryListLength`.
- `PurgeBoundary` – The transaction number up to which InnoDB
  purging is allowed. If this CloudWatch metric doesn't advance for extended periods of
  time, it's a good indication that InnoDB purging is blocked by long-running
  transactions. To investigate, check the active transactions on your Aurora MySQL
  DB cluster. This metric is available only for Aurora MySQL version 2.11 and
  higher, and version 3.08 and higher.
- `PurgeFinishedPoint` – The transaction number up to which
  InnoDB purging is performed. This CloudWatch metric can help you examine how fast
  InnoDB purging is progressing. This metric is available only for Aurora MySQL
  version 2.11 and higher, and version 3.08 and higher.
- `TransactionAgeMaximum` – The age of the oldest active
  running transaction. This CloudWatch metric is available only for Aurora MySQL version
  3.08 and higher.
- `TruncateFinishedPoint` – The transaction number up to which
  undo truncation is performed. This CloudWatch metric is available only for Aurora MySQL
  version 2.11 and higher, and version 3.08 and higher.

For more information on the CloudWatch metrics, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").
