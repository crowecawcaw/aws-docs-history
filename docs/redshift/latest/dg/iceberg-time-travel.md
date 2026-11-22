

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Time travel queries on Iceberg tables in Amazon Redshift

With time travel queries, you can query an Apache Iceberg table as it was at an earlier point in time. Amazon Redshift reads the table snapshot that was current at that time. You can use time travel queries to compare a table with an earlier version, to undo changes, or to get the same results each time you rerun a report. Time travel queries only read data, and they don't change the table or its history. How far back you can query depends on the table's snapshot retention. For more information, see [Best practices for time travel queries](#iceberg-time-travel-best-practices).

## Syntax
<a name="iceberg-time-travel-syntax"></a>

To read an Apache Iceberg table as it was at an earlier point in time, add an `AS OF TIMESTAMP` clause after the table name where the query reads the table, such as in a `FROM` clause, a `JOIN`, or a `USING` clause.

```
SELECT ...
FROM {{iceberg_table}}
     AS OF TIMESTAMP { '{{timestamp_literal}}' | ( {{timestamp_expression}} ) }
     [ [ AS ] {{alias}} ]
[ ... ]
```

The `AS OF TIMESTAMP` clause applies only to the table reference that it follows. Other tables in the query are read as they are now, unless they have their own `AS OF TIMESTAMP` clause. Amazon Redshift determines the point in time once, before it runs the query.

## Parameters
<a name="iceberg-time-travel-parameters"></a>

{{iceberg\_table}}  
The name of an Apache Iceberg table. You can reference the table the same way as in other queries. For more information, see [Referencing Iceberg tables in Amazon Redshift](referencing-iceberg-tables.md).

'{{timestamp\_literal}}'  
A quoted date or timestamp, such as `'2026-11-01 09:00:00 UTC'` or `'now'`.  
+ It can use the date and timestamp formats and the special datetime values described in [Date, time, and timestamp literals](r_Date_and_time_literals.md).
+ It must include a date. A time alone, such as `'09:00:00'`, isn't supported. A date without a time means midnight on that date.
+ If the value has no time zone, Amazon Redshift reads it in the session time zone.

( {{timestamp\_expression}} )  
An expression in parentheses that evaluates to a single point in time, such as `(CURRENT_TIMESTAMP - INTERVAL '1 day')`.  
+ It can contain only literals, casts, operators, and built-in functions. For details, see [Limitations](#iceberg-time-travel-limitations).
+ Current-time functions, such as `CURRENT_TIMESTAMP` and `SYSDATE`, return the start of the current transaction. `GETDATE` doesn't, so it isn't supported.
+ Its result must be a value that can be cast to `TIMESTAMPTZ`, such as a date, a timestamp, or a string that contains one. If the result has no time zone, Amazon Redshift reads it in the session time zone.

{{alias}}  
An optional table alias. The alias goes after the `AS OF TIMESTAMP` clause.

### Syntax examples
<a name="iceberg-time-travel-syntax-examples"></a>

The following examples use a timestamp literal and two expressions:

```
-- A timestamp literal with a time zone, and a table alias
SELECT o.order_id, o.amount
FROM iceberg_schema.orders AS OF TIMESTAMP '2026-11-01 09:00:00 UTC' AS o;

-- Expressions, in parentheses
SELECT * FROM iceberg_schema.orders
     AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '1 day');

SELECT * FROM iceberg_schema.orders
     AS OF TIMESTAMP (DATEADD(hour, -6, SYSDATE));
```

## Limitations
<a name="iceberg-time-travel-limitations"></a>

Time travel queries have limitations on the inputs that you can use, the tables that you can query, and the SQL statements that you can use them in.

### Time travel inputs
<a name="iceberg-time-travel-limitations-inputs"></a>
+ **Snapshot IDs** – You can specify a point in time only as a timestamp. Querying by snapshot ID, such as with an `AS OF VERSION` clause, isn't supported.
+ **Future points in time** – The point in time can't be later than the start of the current transaction. For example, `'tomorrow'` and `(CURRENT_TIMESTAMP + INTERVAL '1 hour')` aren't supported.
+ **Expressions** – A timestamp expression can contain only literals, casts, operators, and built-in `IMMUTABLE` or `STABLE` functions, such as `DATEADD`, `DATE_TRUNC`, and `CONVERT_TIMEZONE`. Other kinds of expressions aren't supported. These include column references, subqueries, conditional expressions such as `CASE` and `COALESCE`, and aggregate and window functions. User-defined functions and volatile functions, such as `RANDOM`, also aren't supported. You also can't use bind parameters, such as `$1`, or stored procedure arguments and variables.
+ **Prepared statements** – Amazon Redshift sets the point in time when you prepare a statement, such as with `PREPARE` or a JDBC `PreparedStatement`. If you run the statement again, such as with `EXECUTE`, and the point in time would be different, the statement returns an error. For example, `CURRENT_TIMESTAMP` causes this error in a later transaction. Use a fixed point in time that includes a time zone instead.

### Tables
<a name="iceberg-time-travel-limitations-tables"></a>
+ **Table types** – You can use time travel queries only on [Apache Iceberg tables](querying-iceberg.md) in the AWS Glue Data Catalog. These include [Iceberg materialized views](materialized-view-iceberg.md) (materialized views stored as Apache Iceberg tables). For example, you can't use time travel queries on Amazon Redshift tables or views.
+ **Nested data** – You can use a time travel query only when the schema of the snapshot that it reads has no columns of [complex data types](tutorial-query-nested-data.md), such as `struct`, `array`, or `map`. This applies even if the query doesn't select those columns.
+ **AWS Lake Formation** – You can't use time travel queries on Iceberg tables [governed by AWS Lake Formation](spectrum-lake-formation.md), including tables with data filters or column-level permissions. This includes tables in the Amazon S3 Tables catalog ([`s3tablescatalog`](referencing-iceberg-tables.md#referencing-iceberg-three-part-notation)).
+ **Data sharing** – You can't use time travel queries on tables that you access through [data sharing](datashare-overview.md).

### SQL statements
<a name="iceberg-time-travel-limitations-statements"></a>
+ **Read-only** – Time travel queries only read data. You can't use an `AS OF TIMESTAMP` clause on the target table of a data manipulation language (DML) statement, such as `INSERT`, `UPDATE`, `DELETE`, or `MERGE`. The same applies to data definition language (DDL) statements, such as `ALTER TABLE` and `DROP TABLE`, and to other commands that act on a table, such as `COPY`, `VACUUM`, and `GRANT`.
+ **Table references only** – You can use an `AS OF TIMESTAMP` clause only after a table name. For example, you can't use it after a subquery or the name of a [common table expression (CTE)](r_WITH_clause.md). To read a table at an earlier point in time in a CTE, use the `AS OF TIMESTAMP` clause on the table inside the CTE's query.
+ **Views and materialized views** – You can't use an `AS OF TIMESTAMP` clause in the definition of a [view](r_CREATE_VIEW.md), a [late-binding view](r_CREATE_VIEW.md#r_CREATE_VIEW_late-binding-views), or a [materialized view](materialized-view-overview.md), including an Iceberg materialized view.

## How time travel queries work
<a name="iceberg-time-travel-how-it-works"></a>

An Apache Iceberg table's metadata records the table's snapshots and when each one became current. Every change to the table's data adds a new snapshot. For more information, see [Table metadata](https://iceberg.apache.org/spec/#table-metadata) in the *Apache Iceberg table specification*.

Amazon Redshift uses the following metadata fields to find the snapshot for a time travel query:


| Field | Purpose | 
| --- | --- | 
| snapshot-log | Records when each snapshot became current | 
| snapshots | Lists the snapshots that the table still keeps, each with a manifest list of its data files and a schema-id | 
| schemas | Lists the table's schemas | 

For a time travel query, Amazon Redshift does the following:

1. Looks up the table in the AWS Glue Data Catalog to find its current metadata file. Reading a table at an earlier point in time requires the same permissions as reading its current data. Amazon Redshift checks these permissions as they are now, not as they were at the requested point in time. You don't need additional AWS Glue or Amazon S3 permissions.

1. Reads the `snapshot-log` in that file, and finds the latest entry that became current at or before the requested point in time.

1. Finds that snapshot in `snapshots`. The snapshot's `schema-id` identifies the schema in `schemas` that the snapshot was written with, and Amazon Redshift uses that schema for the snapshot's columns. If the snapshot has no `schema-id`, or the metadata has no `schemas`, Amazon Redshift uses the table's current schema.

A time travel query returns an error in the following cases:
+ The table's current metadata file can't be read.
+ The metadata has no `snapshot-log`.
+ The requested point in time is earlier than the first entry in `snapshot-log`.
+ The snapshot that was current at that time is no longer in `snapshots`, for example because it expired.
+ The snapshot has no manifest list.
+ The snapshot's `schema-id` doesn't match any schema in `schemas`.

Because you can query only the snapshots that a table still keeps, the table's snapshot retention determines how far back you can query. For more information, see [Best practices for time travel queries](#iceberg-time-travel-best-practices).

## Best practices for time travel queries
<a name="iceberg-time-travel-best-practices"></a>

Use the following practices to keep time travel queries fast and to keep the history that you need:
+ **Keep only the history that you need** – Each snapshot that a table keeps can make time travel queries take longer to plan, and it keeps the data files that only it references in storage. Set the table's snapshot retention to cover how far back you need to query, and expire older snapshots regularly. You can't query a snapshot after it expires. For more information, see [Snapshot retention optimization](https://docs.aws.amazon.com/glue/latest/dg/snapshot-retention-management.html) in the *AWS Glue Developer Guide* and [Snapshot management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html#s3-tables-maintenance-snapshot) in the *Amazon S3 User Guide*.
+ **Group related writes** – Run related write statements in one multi-statement transaction, so that they commit as one snapshot. For more information, see [Transaction semantics](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-transaction-semantics.html).
+ **Keep long-term history in the data** – For history that you need for months or years, store it in the table itself, for example with timestamp and operation columns, instead of keeping years of snapshots.
+ **Compact data files** – A snapshot keeps the files that it was written with. A snapshot from before compaction can have many small files, and it can take longer to read than the current table. Compact data files regularly with the [AWS Glue Data Catalog compaction optimizer](https://docs.aws.amazon.com/glue/latest/dg/compaction-management.html) or [Amazon S3 Tables compaction](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html#s3-tables-maintenance-compaction).
+ **Use a fixed point in time for repeatable results** – A value such as `CURRENT_TIMESTAMP` resolves to a different point each time, and a timestamp without a time zone depends on the session time zone. To get the same results each time, use a fixed timestamp that includes a time zone.

## Examples
<a name="iceberg-time-travel-examples"></a>

The following examples show common uses of time travel queries. Most examples use an `orders` Iceberg table in the external schema `iceberg_schema`.

### Query and compare earlier versions of a table
<a name="iceberg-time-travel-examples-compare"></a>

The following example counts the rows in the table now, one day ago, and seven days ago:

```
SELECT 'current' AS period, COUNT(*) AS order_count
FROM iceberg_schema.orders
UNION ALL
SELECT '1 day ago', COUNT(*)
FROM iceberg_schema.orders AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '1 day')
UNION ALL
SELECT '7 days ago', COUNT(*)
FROM iceberg_schema.orders AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '7 days');
```

An Iceberg materialized view is stored as a standard Iceberg table, so you can also query it as it was at an earlier point in time, such as before its last refresh. The following example returns the rows of the `daily_revenue_mv` Iceberg materialized view that are new or changed since a refresh at 02:00 UTC:

```
SELECT order_date, revenue, order_count
FROM iceberg_schema.daily_revenue_mv
EXCEPT
SELECT order_date, revenue, order_count
FROM iceberg_schema.daily_revenue_mv
     AS OF TIMESTAMP '2026-11-01 01:59:00 UTC';
```

To find rows that were removed or changed, swap the two sides of `EXCEPT`.

To run the same comparison many times, for example from an application, prepare it with a parameter. The following example returns a customer's orders that are new or changed since the month-end close, and then runs it for different customers:

```
PREPARE changes_since_close (int) AS
SELECT order_id, status, amount
FROM iceberg_schema.orders
WHERE customer_id = $1
EXCEPT
SELECT order_id, status, amount
FROM iceberg_schema.orders AS OF TIMESTAMP '2026-11-01 00:00:00 UTC'
WHERE customer_id = $1;

EXECUTE changes_since_close (42);
EXECUTE changes_since_close (43);
```

### Save a snapshot as a new table
<a name="iceberg-time-travel-examples-save"></a>

The following example saves the table as it was at a point in time to a new Amazon Redshift table:

```
CREATE TABLE orders_2026_11_01 AS
SELECT * FROM iceberg_schema.orders
     AS OF TIMESTAMP '2026-11-01 00:00:00 UTC';
```

The new table has the columns of the snapshot's schema, and it keeps the data after the snapshot expires.

### Undo changes to a table
<a name="iceberg-time-travel-examples-undo"></a>

To restore deleted rows, insert them from the table as it was before the delete. The following example puts back pending orders that a `DELETE` removed by mistake in the last hour:

```
INSERT INTO iceberg_schema.orders
SELECT * FROM iceberg_schema.orders
     AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '1 hour')
WHERE status = 'pending';
```

To restore overwritten values, update the rows from the table as it was before the change. The following example sets each order's status and amount back to their values from one hour ago:

```
UPDATE iceberg_schema.orders
SET status = prev.status, amount = prev.amount
FROM iceberg_schema.orders
     AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '1 hour') AS prev
WHERE orders.order_id = prev.order_id
  AND (orders.status <> prev.status OR orders.amount <> prev.amount);
```

To remove rows that were added, delete the rows that weren't in the table at the earlier point in time. The following example deletes the orders that were added in the last hour:

```
DELETE FROM iceberg_schema.orders
WHERE order_id NOT IN (
  SELECT order_id FROM iceberg_schema.orders
       AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '1 hour'));
```

To restore a set of rows exactly as they were, delete them and insert them again from the earlier point in time, in one transaction. The following example restores the orders of customer 42 to how they were one hour ago:

```
BEGIN;

DELETE FROM iceberg_schema.orders WHERE customer_id = 42;

INSERT INTO iceberg_schema.orders
SELECT * FROM iceberg_schema.orders
     AS OF TIMESTAMP (CURRENT_TIMESTAMP - INTERVAL '1 hour')
WHERE customer_id = 42;

COMMIT;
```

Rows that were added are removed, deleted rows come back, and changed values are reverted. If either statement fails, neither change is committed. Inside a transaction, `CURRENT_TIMESTAMP` returns the start of the transaction. The transaction's writes aren't committed until the transaction commits, so a time travel query in the transaction doesn't see them.

These statements also undo changes that other writers made after that time. Choose a time shortly before the bad write.

### Recompute a summary as of a cutoff time
<a name="iceberg-time-travel-examples-recompute"></a>

The following example recomputes the revenue for October 31 from the `orders` table as it was at the 02:00 UTC reporting cutoff, and updates or inserts the result in the `daily_revenue` table:

```
MERGE INTO public.daily_revenue
USING (
  SELECT order_date, SUM(amount) AS revenue, COUNT(*) AS order_count
  FROM iceberg_schema.orders AS OF TIMESTAMP '2026-11-01 02:00:00 UTC'
  WHERE order_date = '2026-10-31'
  GROUP BY order_date
) AS src
ON daily_revenue.order_date = src.order_date
WHEN MATCHED THEN UPDATE SET revenue = src.revenue, order_count = src.order_count
WHEN NOT MATCHED THEN INSERT (order_date, revenue, order_count)
     VALUES (src.order_date, src.revenue, src.order_count);
```

Orders that arrive after the cutoff don't change the result, so the statement returns the same totals each time it runs.