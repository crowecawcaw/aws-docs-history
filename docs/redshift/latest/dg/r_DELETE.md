Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DELETE

Deletes rows from tables.

###### Note

The maximum size for a single SQL statement is 16 MB.

## Syntax

```
[ WITH [RECURSIVE] *common\_table\_expression* [, *common\_table\_expression* , ...] ]
DELETE [ FROM ] *{ table\_name | materialized\_view\_name }*
    [ { USING } *table\_name, ...* ]
    [ WHERE *condition* ]
```

## Parameters

WITH clause

Optional clause that specifies one or more
_common-table-expressions_. See [WITH clause](r_WITH_clause.md "r_WITH_clause.md").

FROM

The FROM keyword is optional, except when the USING clause is specified. The
statements `delete from event;` and `delete event;` are
equivalent operations that remove all of the rows from the EVENT table.

###### Note

To delete all the rows from a table, [TRUNCATE](r_TRUNCATE.md "r_TRUNCATE.md") the table. TRUNCATE is much more efficient
than DELETE and doesn't require a VACUUM and ANALYZE. However, be aware
that TRUNCATE commits the transaction in which it is run.

_table_name_

A temporary or persistent table. Only the owner of the table or a user with
DELETE privilege on the table may delete rows from the table.

Consider using the TRUNCATE command for fast unqualified delete operations
on large tables; see [TRUNCATE](r_TRUNCATE.md "r_TRUNCATE.md").

###### Note

After deleting a large number of rows from a table:

- Vacuum the table to reclaim storage space and re-sort rows.
- Analyze the table to update statistics for the query
  planner.

_materialized_view_name_

A materialized view. The DELETE statement works on a materialized view used
for [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md"). Only the owner of
the materialized view or a user with DELETE privilege on the materialized view
may delete rows from it.

You can't run DELETE on a materialized view for streaming ingestion with a
row-level security (RLS) policy that doesn't have the IGNORE RLS permission
granted to the user. There is an exception to this: If the user performing the
DELETE has IGNORE RLS granted, it runs successfully. For more information, see
[RLS policy ownership and
management](t_rls_ownership.md "t_rls_ownership.md").

USING _table_name_, ...

The USING keyword is used to introduce a table list when additional tables
are referenced in the WHERE clause condition. For example, the following
statement deletes all of the rows from the EVENT table that satisfy the join
condition over the EVENT and SALES tables. The SALES table must be explicitly
named in the FROM list:

```
delete from event using sales where event.eventid=sales.eventid;
```

If you repeat the target table name in the USING clause, the DELETE
operation runs a self-join. You can use a subquery in the WHERE clause instead
of the USING syntax as an alternative way to write the same query.

WHERE _condition_

Optional clause that limits the deletion of rows to those that match the
condition. For example, the condition can be a restriction on a column, a join
condition, or a condition based on the result of a query. The query can
reference tables other than the target of the DELETE command. For
example:

```
delete from t1
where col1 in(select col2 from t2);
```

If no condition is specified, all of the rows in the table are
deleted.

## Usage notes

- DELETE operations hold exclusive locks when run on Amazon Redshift streaming materialized views
  connected to any of the following:

      + An Amazon Kinesis data stream
      + An Amazon Managed Streaming for Apache Kafka topic
      + A supported external stream, such as a Confluent Cloud Kafka topic

  For more information, see [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

## Examples

Delete all of the rows from the CATEGORY table:

```
delete from category;
```

Delete rows with CATID values between 0 and 9 from the CATEGORY table:

```
delete from category
where catid between 0 and 9;
```

Delete rows from the LISTING table whose SELLERID values don't exist in the
SALES table:

```
delete from listing
where listing.sellerid not in(select sales.sellerid from sales);
```

The following two queries both delete one row from the CATEGORY table, based on a
join to the EVENT table and an additional restriction on the CATID column:

```
delete from category
using event
where event.catid=category.catid and category.catid=9;
```

```
delete from category
where catid in
(select category.catid from category, event
where category.catid=event.catid and category.catid=9);
```

The following query deletes all rows from the `mv_cities` materialized
view. The materialized view name in this example is a sample:

```
delete from mv_cities;

```
