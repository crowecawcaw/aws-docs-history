# Understanding redacted logs

AWS Clean Rooms redacts Spark logs before exporting them so that the exported logs don't reveal
the contents of a member's data, or identify the table and storage locations of the source
data. AWS Clean Rooms reconstructs the log records and emits only the fields that are known to be
safe to share. Some information is preserved deliberately, including the names of columns
that a query read.

Redaction doesn't distinguish between members. Expect your own table names and query
values to be redacted from the logs that you export for your own queries, on the same
terms as another member's information. Empty and placeholder fields are normal and don't
indicate a problem with the export.

## What the exported logs contain

The exported logs preserve the information needed to diagnose failures and
performance problems:

- **Timings** – Task and stage
  durations, run time, CPU time, garbage collection time, deserialization and
  result serialization time, shuffle wait time, and shuffle write time are all
  preserved exactly. Timings are the main signal for performance
  analysis.
- **Spark execution identifiers and counts**
  – Job, stage, task, and attempt IDs, partition counts, task counts,
  executor IDs, host names, and ports.
- **Query plan structure** – The
  physical plan tree, including operator names such as
  `HashAggregate`, `SortMergeJoin`, and
  `Exchange`, so you can see the shape of the plan and how the
  engine chose to execute your query. An operator name that isn't one of
  Spark's own appears as `[REDACTED]`.
- **Source column names** – Column names
  that come from a table being scanned, so you can see which columns are used
  in filters, joins, and aggregations. Names that a query creates, such as an
  alias, are not preserved. For more information, see [How column and table names are treated](#export-analysis-logs-names "#export-analysis-logs-names").
- **Scan type and file format** – A scan
  operator ordinarily includes the name of the table being read. The name is
  replaced with a form that identifies only the scan type and file format, such
  as `Scan parquet`, so you can still tell how data is being read. If
  the file format isn't one that AWS Clean Rooms recognizes, the operator appears as
  `Scan` with no format.
- **Error classes** – When a query fails,
  the logs identify the kind of error but not the data that caused it. They
  report Spark's error class, its SQLSTATE code, and the standard message that
  Spark defines for that class, with the message's
  `<placeholder>` tokens left unfilled, because the values
  that would fill them come from the data. A failed cast, for example, reports
  `[CAST_INVALID_INPUT]` and a message describing that a value of one
  type can't be cast to another, without showing the value. When one failure
  caused another, the error classes in the chain are reported together, up to a
  few levels deep. A failure that didn't originate in Spark is reported only as
  a non-Spark error, with no class.

Individual task failures report only the kind of failure, such as
`ExceptionFailure`. They don't carry an error class of their
own.

- **Spark configuration** –
  Settings whose values are always numbers, sizes, or fixed keywords, and that
  are most often needed to diagnose a performance problem: driver and executor
  cores and memory, memory fractions and off-heap settings, dynamic allocation
  settings, adaptive query execution settings, default parallelism and the
  shuffle partition count, the broadcast join threshold, the maximum partition
  size, shuffle compression settings, the scheduler mode, and the serializer.
  Most other configuration is redacted, because settings can contain paths,
  identifiers, and query text. One of these settings is also omitted if its
  value isn't a plain number, size, or keyword.
- **Memory utilization and data volumes**
  – Peak execution memory, memory and disk spill, executor JVM memory,
  cached data sizes, shuffle block counts, and the number of bytes and records
  read and written, including shuffle read and write volumes. These figures are
  rounded down rather than exact. For more
  information, see [How redacted logs differ from standard Spark logs](#export-analysis-logs-caveats "#export-analysis-logs-caveats").
- **Why an executor stopped** – A category
  for each executor that stopped, such as running out of memory, being shut down
  by the driver, being decommissioned, or failing to respond. This is often the
  fastest way to explain why a query failed. The logs also record any executor
  or host that Spark stopped scheduling work on, which is useful when failures
  keep recurring in one place. For more information, see [How redacted logs differ from standard Spark logs](#export-analysis-logs-caveats "#export-analysis-logs-caveats").
- **Shuffle fetch failure detail** – When
  a task can't fetch shuffle output, the shuffle, map, map index, and reduce
  identifiers are preserved, along with the executor and host that the fetch
  was attempted against. This lets you distinguish repeated failures against a
  single source, which usually indicate an unresponsive executor, from failures
  spread across many sources, which usually indicate transient network
  problems.

## What is redacted

- **Data values** – Literal values from
  your query, and data values from any table. A filter predicate shows which
  column was filtered but not the value it was compared against.
- **Table names and storage locations**
  – Table identifiers, database names, and Amazon S3 paths.
- **Query text** – The SQL statement and
  any description associated with the query.
- **Error message text and stack traces**
  – Because an error message can quote the value that caused the error,
  message text and stack traces are removed. The name of the underlying
  exception class is also redacted, because an exception thrown by a
  user-defined function carries a name that the query author chose. The Spark
  error class is preserved instead, for the query and the job. The reason a stage
  failed and the reason a task was killed are redacted as well.
- **Names that Spark records for its own work**
  – The names and call sites of stages and cached datasets, and the
  application name. These are free-text fields that can echo a table name or a
  storage path. In Spark History Server, stages therefore appear without the
  descriptions that would normally identify them, and you locate a stage by its
  ID and its place in the plan instead.
- **Computed and aliased column names** –
  Names that a query creates rather than reads from a table, because the query
  engine generates such a name from the expression and the name can contain a
  value. These appear as a numeric identifier such as `#42`. For more
  information, see [How column and table names are treated](#export-analysis-logs-names "#export-analysis-logs-names").
- **Scan detail** – The read schema, the
  filter predicates applied at each scan (pushed-down filters, partition
  filters, and data filters), and the data location.
- **Links to driver and executor logs** –
  The log URLs that Spark records for each executor and for the driver. In
  Spark History Server, the links that would normally open a driver or executor
  log aren't populated.
- **Resource identifiers and service
  endpoints** – AWS account IDs, ARNs such as those of IAM
  roles and AWS KMS keys, and the endpoint URLs of the services that AWS Clean Rooms calls
  to run your query.
- **AWS service details** –
  AWS Clean Rooms class names, classpath entries, JVM configuration, and Hadoop and
  system properties. Job properties are redacted as well, apart from the
  identifiers that Spark History Server needs in order to associate jobs with
  the query execution they belong to.

## How column and table names are treated

The exported logs keep the names of columns that a query read. Table names and
column aliases created in the query are redacted. A name that a query creates is
generated from
the expression it names, and that generated name can contain a value from the query:
`SELECT 'confidential'` produces a column named
`confidential`. A name therefore appears only when it can be traced back
to a column of a scanned table. Every other name is replaced with a numeric
identifier.

For example, consider the following query.

```
`SELECT user_id, SUM(amount) AS total
FROM sales
WHERE region = 'us-west'
GROUP BY user_id`
```

The exported logs represent it as follows.

| Element of the query                                         | In the exported logs                                                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| The columns `user_id`, `amount`, and<br>`region`             | Present by name, so you can see what the query grouped, summed,<br>and filtered on                            |
| The table `sales`, its database, and its storage<br>location | Not present                                                                                                   |
| The value `'us-west'`                                        | Replaced with `[REDACTED]`                                                                                    |
| The alias `total`                                            | Replaced with a numeric identifier, because the query created the<br>name rather than reading it from a table |

## How redacted logs differ from standard Spark logs

###### Row counts and data volumes are approximate

Record counts, byte volumes, spill sizes, and peak memory measurements are
rounded down to an order of magnitude, because an exact count can reveal the
size of another member's data. A task that read 1,342 records reports 1,000.
Measurements below 100 report as 0.

Because every figure is rounded down, a task that reports 100 and a task that
reports 1,000 might have read nearly the same number of records. Treat figures that
differ by only one order of magnitude with caution; larger differences, such as 1,000
against 10,000,000, still reliably indicate skew.

###### Redacted values take more than one form

In the query plan, a redacted value appears as the literal text
`[REDACTED]`. Elsewhere in the logs, a redacted field is usually empty
instead. It might be a blank string, an empty list, or a value that is absent
altogether, so that Spark History Server can still read the
record. Both forms mean the same thing.

###### Query plans don't use familiar operator syntax

Expressions in the plan are written as function calls rather than in
mathematical notation. A comparison appears as
`EqualTo(#12, [REDACTED])` rather than `(a = 5)`. Function
names appear in this form too, and user-defined function names don't appear at
all.

###### Only the physical plan is included

The exported logs contain the physical plan. They don't contain the parsed,
analyzed, or optimized logical plans that ordinarily accompany it.

###### Per-task metrics are redacted

The plan graph lists the metrics that each operator reports, such as the number
of output rows. Metrics that individual tasks report show no value at all,
because the per-task figures behind them are removed. For task-level numbers, use
the per-task metrics in the stage view instead.

###### Spark driver metrics are rounded down

Metrics that Spark computes on the driver, including those for broadcasts,
scans, and writes, do report a value, but it is rounded down to an order of
magnitude for the same reason that record counts and data volumes are: an exact
figure can reveal the size of another member's data.

###### Only the event log is exported

The export contains the Spark event log. It doesn't contain the free-form
driver and executor output that Spark writes alongside it, because a single line
of that output can contain a table name, a storage path, or a data value.
Diagnosis has to be done from the event log.

###### Executor failures show generic error messages

Because the free-form reason an executor stopped can contain AWS Clean Rooms service
detail, the logs instead report a general error message, such as an out-of-memory
exit, a shutdown initiated by the driver, a decommissioned executor, or a lost
process. This record is specific to AWS Clean Rooms and isn't a standard Spark event, so
Spark History Server and other tools might not display it. If you don't see it,
you can find it in the exported event log file.

###### Unrecognized records are redacted by default

If a log record isn't one that AWS Clean Rooms recognizes, all of its text is replaced
with `[REDACTED]`, including its field names, and all of its numbers
are replaced with zero. Only the record type is preserved. Such a record carries
no diagnostic information.
