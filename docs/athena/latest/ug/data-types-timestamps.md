# Work with timestamp data

This section describes some considerations for working with timestamp data in
Athena.

###### Note

The treatment of timestamps has changed somewhat between previous engine versions and Athena engine version 3. For
information about timestamp-related errors that can occur in Athena engine version 3 and suggested
solutions, see [Timestamp
changes](engine-versions-reference-0003.md#engine-versions-reference-0003-timestamp-changes "engine-versions-reference-0003.md#engine-versions-reference-0003-timestamp-changes") in the [Athena engine version 3](engine-versions-reference-0003.md "engine-versions-reference-0003.md") reference.

## Format for writing

timestamp data to Amazon S3 objects

The format in which timestamp data should be written into Amazon S3 objects depends on both
the column data type and the [SerDe
library](supported-serdes.md "supported-serdes.md") that you use.

- If you have a table column of type `DATE`, Athena expects the
  corresponding column or property of the data to be a string in the ISO format
  `YYYY-MM-DD`, or a built-in date type like those for Parquet or
  ORC.
- If you have a table column of type `TIME`, Athena expects the
  corresponding column or property of the data to be a string in the ISO format
  `HH:MM:SS`, or a built-in time type like those for Parquet or
  ORC.
- If you have a table column of type `TIMESTAMP`, Athena expects the
  corresponding column or property of the data to be a string in the format
  `YYYY-MM-DD HH:MM:SS.SSS` (note the space between the date and
  time), or a built-in time type like those for Parquet, ORC, or Ion. Note that
  Athena does not guarantee the behavior for timestamps that are invalid (for
  example, `0000-00-00 08:00:00.000`).

###### Note

OpenCSVSerDe timestamps are an exception and must be encoded as
millisecond resolution UNIX epochs.

## Ensuring that time-partitioned data matches the timestamp field in a record

The producer of the data must make sure partition values align with the data within
the partition. For example, if your data has a `timestamp` property and you
use Firehose to load the data into Amazon S3, you must use [dynamic partitioning](../../../firehose/latest/dev/dynamic-partitioning.md "../../../firehose/latest/dev/dynamic-partitioning.md")
because the default partitioning of Firehose is wall-clock-based.

## Use string as the data type

for partition keys

For performance reasons, it is preferable to use `STRING` as the data type
for partition keys. Even though Athena recognizes partition values in the format
`YYYY-MM-DD` as dates when you use the `DATE` type, this can
lead to poor performance. For this reason, we recommend that you use the
`STRING` data type for partition keys instead.

## How to write queries for timestamp fields that are also time-partitioned

How you write queries for timestamp fields that are time-partitioned depends on the
type of table that you want to query.

### Hive tables

With the Hive tables most commonly used in Athena, the query engine has no
knowledge of relationships between columns and partition keys. For this reason, you
must always add predicates in your queries for both the column and the partition
key.

For example, suppose you have an `event_time` column and an
`event_date` partition key and want to query events between 23:00 and
03:00. In this case, you must include predicates in your query for both the column
and the partition key, as in the following example.

```
WHERE event_time BETWEEN `start_time` AND `end_time`
  AND event_date BETWEEN `start_time_date` AND `end_time_date`
```

### Iceberg tables

With Iceberg tables, you can use computed partition values, which simplifies your
queries. For example, suppose your Iceberg table was created with a
`PARTITIONED BY` clause like the following:

```
PARTITIONED BY (event_date month(event_time))
```

In this case, the query engine automatically prunes partitions based on the values
of the `event_time` predicates. Because of this, your query only needs to
specify a predicate for `event_time`, as in the following example.

```
WHERE event_time BETWEEN `start_time` AND `end_time`
```

For more information, see [Create Iceberg tables](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md").

When using Iceberg's hidden partitioning for a timestamp column, Iceberg might
create a partition on a constructed table column derived from a timestamp column and
transformed into a date for more effective partitioning. For example, it might
create `event_date` from the timestamp column `event_time` and
automatically partition on `event_date`. In this case, the partition
**type** is a **date**.

For optimal query performance when you use the partition, filter on full day
ranges to enable predicate pushdown. For example, the following query wouldn't be
pushed down because the range can't be converted to a single date partition, even
though it falls within a single day:

```
WHERE event_time >= TIMESTAMP '2024-04-18 00:00:00' AND event_time < TIMESTAMP '2024-04-18 12:00:00'
```

Instead, use a full day range to allow predicate pushdown and improve query
performance as in following example.

```
WHERE event_time >= TIMESTAMP '2024-04-18 00:00:00' AND event_time < TIMESTAMP '2024-04-19 00:00:00'
```

You can also use the `BETWEEN start_time AND end_time` syntax or use
the multi-day ranges as long as the timestamps portions are
`00:00:00`.

For more information, see the [Trino blog
post](https://trino.io/blog/2023/04/11/date-predicates.html "https://trino.io/blog/2023/04/11/date-predicates.html").
