# Distributed query tracing in PostgreSQL logs in Aurora PostgreSQL Limitless Database

Distributed query tracing is a tool to trace and correlate queries in PostgreSQL logs across Aurora PostgreSQL Limitless Database. In Aurora PostgreSQL, you use the transaction
ID to identify a transaction. But in Aurora PostgreSQL Limitless Database, the transaction ID can repeat across various routers. Therefore, we recommend that you use the
tracing ID instead in Limitless Database.

The key use cases are the following:

- Use the `rds_aurora.limitless_get_last_trace_id()` function to find the unique tracing ID of the last query run in the current
  session. Then search the DB cluster log group in Amazon CloudWatch Logs using that tracing ID to find all the related logs.

You can use the `log_min_messages` and `log_min_error_statement` parameters together to control the volume of logs
printed and print a statement that contains the tracing ID.

- Use the `log_min_duration_statement` parameter to determine the run time above which all of the queries print their run
  duration and tracing ID. This run time can then be searched in the DB cluster log group in CloudWatch Logs to help determine the bottleneck nodes and
  planner optimization efforts.

The `log_min_duration_statement` parameter enables the tracing ID for all nodes regardless of the values of
`log_min_messages` and `log_min_error_statement` parameters.

###### Topics

- [Tracing ID](#limitless-query.tracing.ID "#limitless-query.tracing.ID")
- [Using query tracing](#limitless-query.tracing.using "#limitless-query.tracing.using")
- [Log examples](#limitless-query.tracing.examples "#limitless-query.tracing.examples")

## Tracing ID

Central to this feature is a unique identifier known as the _tracing ID_. The tracing ID is a 31-digit string appended to
the STATEMENT log lines of PostgreSQL logs, acting as a precise identifier for correlating logs related to a specific query execution. Examples
are `1126253375719408504000000000011` and `1126253375719408495000000000090`.

The tracing ID is composed of the following:

- Transaction identifier – The first 20 digits, uniquely identifying the transaction.
- Command identifier – The first 30 digits, indicating an individual query within a transaction.

If more than 4,294,967,294 queries are run inside an explicit transaction block, the command Identifier wraps around to
`1`. When this happens, you're notified by the following `LOG` message in the PostgreSQL log:

```
wrapping around the tracing ID back to 1 after running 4294967294 (4.2 billion or 2^32-2) queries inside of an explicit transaction block
```

- Node type identifier – The last digit, indicating whether the node is functioning as a coordinator router (`1`) or a
  participant node (`0`).

The following examples illustrate the components of the tracing ID:

- `1126253375719408504000000000011`:
  - Transaction identifier – `1126253375719408504`
  - Command identifier – `112625337571940850400000000001` indicates the first command in the transaction
    block
  - Node type identifier – `1` indicates a coordinator router

- `1126253375719408495000000000090`:
  - Transaction identifier – `1126253375719408495`
  - Command identifier – `112625337571940849500000000009` indicates the ninth command in the transaction
    block
  - Node type identifier – `0` indicates a participant node

## Using query tracing

Perform the following tasks to use query tracing:

1. Make sure that tracing is enabled.

You can check using the following command:

```
SHOW rds_aurora.limitless_log_distributed_trace_id;
```

It's enabled by default (`on`). If it's not enabled, set it using the following command:

```
SET rds_aurora.limitless_log_distributed_trace_id = on;
```

2. Control the volume of logs printed by configuring the log severity level.

The log volume is controlled by the `log_min_messages` parameter. The `log_min_error_statement` parameter is
used to print the `STATEMENT` line with the tracing ID. Both are set to `ERROR` by default. You can check using
the following commands:

```
SHOW log_min_messages;
SHOW log_min_error_statement;
```

To update the severity level and print the `STATEMENT` line for the current session, use the following commands with one of
these severity levels:

```
SET log_min_messages = '`DEBUG5` | `DEBUG4` | `DEBUG3` | `DEBUG2` | `DEBUG1` | `INFO` | `NOTICE` | `WARNING` | `ERROR` | `LOG` | `FATAL` | `PANIC`';
SET log_min_error_statement = '`DEBUG5` | `DEBUG4` | `DEBUG3` | `DEBUG2` | `DEBUG1` | `INFO` | `NOTICE` | `WARNING` | `ERROR` | `LOG` | `FATAL` | `PANIC`';
```

For example:

```
SET log_min_messages = 'WARNING';
SET log_min_error_statement = 'WARNING';
```

3. Enable printing the tracing ID in the logs above a specific run time.

The `log_min_duration_statement` parameter can be changed to the minimum query run time above which the query prints a log
line with the run duration, along with the tracing IDs across the DB cluster. This parameter is set to `-1` by default, which
means it's disabled. You can check using the following command:

```
SHOW log_min_duration_statement;
```

Changing it to `0` prints the duration and tracing ID in the logs for every query across the DB cluster. You can set it to
`0` for the current session by using the following command:

```
SET log_min_duration_statement = 0;
```

4. Obtain the tracing ID.

After running a query (even inside an explicit transaction block), call the `rds_aurora.limitless_get_last_trace_id`
function to obtain the tracing ID of the last query run:

```
SELECT * FROM rds_aurora.limitless_get_last_trace_id();
```

This function returns the transaction identifier and the command identifier. It doesn't return the node type identifier.

```
=> SELECT * FROM customers;
 customer_id | fname | lname
-------------+-------+-------
(0 rows)

=> SELECT * FROM rds_aurora.limitless_get_last_trace_id();
 transaction_identifier |       command_identifier
------------------------+--------------------------------
 10104661421959001813   | 101046614219590018130000000001
(1 row)
```

The function returns a blank line for nondistributed queries, as they don't have a tracing ID.

```
=> SET search_path = public;
SET

=> SELECT * FROM rds_aurora.limitless_get_last_trace_id();
 transaction_identifier | command_identifier
------------------------+--------------------
                        |
(1 row)
```

###### Note

For VACUUM and ANALYZE queries, the duration statement isn't logged with the tracing ID. Therefore,
`limitless_get_last_trace_id()` doesn't return the tracing ID. If VACUUM or ANALYZE is a long-running operation, you
can use the following query to obtain the tracing ID for that operation:

```
SELECT * FROM rds_aurora.limitless_stat_activity
WHERE distributed_tracing_id IS NOT NULL;
```

If the server stops before you can find the last tracing ID, you will have to search the PostgreSQL logs manually to find the
tracing IDs in the logs from right before the failure. 5. Search for the tracing ID across the DB cluster logs using CloudWatch.

Use [CloudWatch Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") to query
the DB cluster's log group, as shown in the following examples.

    * Query for a particular transaction identifier and all of the commands run inside it:



    ```
    fields @timestamp, @message
    | filter @message like /10104661421959001813/
    | sort @timestamp desc
    ```
    * Query for a particular command identifier:



    ```
    fields @timestamp, @message
    | filter @message like /101046614219590018130000000001/
    | sort @timestamp desc
    ```

6. Examine all of the logs across the DB cluster produced by the distributed query.

## Log examples

The following examples show the use of query tracing.

### Correlating logs for error-prone queries

In this example the `TRUNCATE` command is run on the `customers` table when that table doesn't exist.

**Without query tracing**

PostgreSQL log file on the coordinator router:

```
2023-09-26 04:03:19 UTC:[local]: postgres@postgres_limitless:[27503]:ERROR: failed to execute remote query
2023-09-26 04:03:19 UTC:[local]: postgres@postgres_limitless:[27503]:DETAIL: relation "public.customers" does not exist
2023-09-26 04:03:19 UTC:[local]: postgres@postgres_limitless:[27503]:CONTEXT: remote SQL command: truncate public.customers;
2023-09-26 04:03:19 UTC:[local]: postgres@postgres_limitless:[27503]:STATEMENT: truncate customers;
```

PostgreSQL log file on a participant shard:

```
2023-09-26 04:03:19 UTC:[local]: postgres@postgres_limitless:[ 27503]:ERROR: failed to execute remote query
2023-09-26 04:03:19 UTC:[local]: postgres@postgres_limitless:[ 27503]:STATEMENT: truncate customers;
```

These logs are typical. They lack the precise identifiers needed to easily correlate queries across the DB cluster.

**With query tracing**

PostgreSQL log file on the coordinator router:

```
2023-09-26 04:03:19 UTC:[local]:postgres@postgres_limitless:[27503]:ERROR: failed to execute remote query
2023-09-26 04:03:19 UTC:[local]:postgres@postgres_limitless:[27503]:DETAIL: relation "public.customers" does not exist
2023-09-26 04:03:19 UTC:[local]:postgres@postgres_limitless:[27503]:CONTEXT: remote SQL command: truncate public.customers;
2023-09-26 04:03:19 UTC:[local]:postgres@postgres_limitless:[27503]:STATEMENT: /* tid = 1126253375719408502700000000011 */ truncate customers;
```

PostgreSQL log file on a participant shard:

```
2023-09-26 04:03:19 UTC:[local]:postgres@postgres_limitless:[27503]:ERROR:  failed to execute remote query
2023-09-26 04:03:19 UTC:[local]:postgres@postgres_limitless:[27503]:STATEMENT:  /* tid = 1126253375719408502700000000010 */ truncate customers;
```

In the presence of query tracing, each log line is appended with a 31-digit unique identifier. Here,
`1126253375719408502700000000011` and `1126253375719408502700000000010` represent the tracing IDs for
the coordinator and participant nodes, respectively.

- Transaction identifier – `11262533757194085027`
- Command identifier: –`112625337571940850270000000001`
- Node type identifier – The last digit, `1` or `0`, indicates a coordinator router and
  participant node, respectively.

### Correlating logs to find the query run time on various nodes

In this example, the `log_min_duration_statement` parameter has been updated to `0` to print the duration for all
queries.

**Without query tracing**

```
2024-01-15 07:28:46 UTC:[local]:postgres@postgres_limitless:[178322]:LOG: duration: 12.779 ms statement: select * from customers;
```

**With query tracing**

PostgreSQL log file on the coordinator router:

```
2024-01-15 07:32:08 UTC:[local]:postgres@postgres_limitless:[183877]:LOG: duration: 12.618 ms statement: /* tid = 0457669566240497088400000000011 */ select * from customers;
```

PostgreSQL log file on a participant shard:

```
2024-01-15 07:32:08 UTC:localhost(46358):postgres@postgres_limitless:[183944]:LOG: duration: 0.279 ms statement: /* tid = 0457669566240497088400000000010 */ START TRANSACTION ISOLATION LEVEL READ COMMITTED
2024-01-15 07:32:08 UTC:localhost(46358):postgres@postgres_limitless:[183944]:LOG: duration: 0.249 ms parse <unnamed>: SELECT customer_id, fname, lname FROM public.customers
2024-01-15 07:32:08 UTC:localhost(46358):postgres@postgres_limitless:[183944]:LOG: duration: 0.398 ms bind <unnamed>/c1: SELECT customer_id, fname, lname FROM public.customers
2024-01-15 07:32:08 UTC:localhost(46358):postgres@postgres_limitless:[183944]:LOG: duration: 0.019 ms execute <unnamed>/c1: SELECT customer_id, fname, lname FROM public.customers
2024-01-15 07:32:08 UTC:localhost(46358):postgres@postgres_limitless:[183944]:LOG: duration: 0.073 ms statement: /* tid = 0457669566240497088400000000010 */ COMMIT TRANSACTION
```
