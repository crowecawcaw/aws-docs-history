Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TRUNCATE

Deletes all of the rows from a table without doing a table scan: this operation is a
faster alternative to an unqualified DELETE operation. To run a TRUNCATE command, you must
have the TRUNCATE permission for the table, be the owner of the table, or be a superuser. To grant
permissions to truncate a table, use the [GRANT](r_GRANT.md "r_GRANT.md")
command.

TRUNCATE is much more efficient than DELETE and doesn't require a VACUUM and
ANALYZE. However, be aware that TRUNCATE commits the transaction in which it is run.

## Syntax

```
TRUNCATE [ TABLE ] *table\_name*
```

The command also works on a materialized view.

```
TRUNCATE *materialized\_view\_name*
```

## Parameters

TABLE

Optional keyword.

_table_name_

A temporary or persistent table. Only the owner of the table or a superuser
may truncate it.

You can truncate any table, including tables that are referenced in
foreign-key constraints.

You don't need to vacuum a table after truncating it.

_materialized_view_name_

A materialized view.

You can truncate a materialized view that is used for [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

## Usage notes

- The TRUNCATE command commits the transaction in which it is run; therefore, you
  can't roll back a TRUNCATE operation, and a TRUNCATE command may commit other
  operations when it commits itself.
- TRUNCATE operations hold exclusive locks when run on Amazon Redshift streaming materialized views
  connected to any of the following:

      + An Amazon Kinesis data stream
      + An Amazon Managed Streaming for Apache Kafka topic
      + A supported external stream, such as a Confluent Cloud Kafka topic

  For more information, see [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

## Examples

Use the TRUNCATE command to delete all of the rows from the CATEGORY table:

```
truncate category;
```

Attempt to roll back a TRUNCATE operation:

```
begin;

truncate date;

rollback;

select count(*) from date;
count
-------
0
(1 row)
```

The DATE table remains empty after the ROLLBACK command because the TRUNCATE command
committed automatically.

The following example uses the TRUNCATE command to delete all of the rows from a
materialized view.

```
truncate my_materialized_view;
```

It deletes all records in the materialized view and leaves the materialized view and
its schema intact. In the query, the materialized view name is a sample.
