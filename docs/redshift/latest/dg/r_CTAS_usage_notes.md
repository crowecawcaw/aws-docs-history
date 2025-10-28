Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CTAS usage notes

## Limits

Amazon Redshift enforces a quota of the number of tables per cluster by node type.

The maximum number of characters for a table name is 127.

The maximum number of columns you can define in a single table is 1,600.

## Inheritance of column and table attributes

CREATE TABLE AS (CTAS) tables don't inherit constraints, identity columns,
default column values, or the primary key from the table that they were created from.

You can't specify column compression encodings for CTAS tables. Amazon Redshift
automatically assigns compression encoding as follows:

- Columns that are defined as sort keys are assigned RAW compression.
- Columns that are defined as BOOLEAN, REAL, DOUBLE PRECISION, GEOMETRY, or
  GEOGRAPHY data type are assigned RAW compression.
- Columns that are defined as SMALLINT, INTEGER, BIGINT, DECIMAL, DATE, TIME,
  TIMETZ, TIMESTAMP, or TIMESTAMPTZ are assigned AZ64 compression.
- Columns that are defined as CHAR, VARCHAR, or VARBYTE are assigned LZO
  compression.

For more information, see [Compression encodings](c_Compression_encodings.md "c_Compression_encodings.md") and [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

To explicitly assign column encodings, use [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md").

CTAS determines distribution style and sort key for the new table based on the
query plan for the SELECT clause.

For complex queries, such as queries that include joins, aggregations, an order by
clause, or a limit clause, CTAS makes a best effort to choose the optimal
distribution style and sort key based on the query plan.

###### Note

For best performance with large datasets or complex queries, we recommend
testing using typical datasets.

You can often predict which distribution key and sort key CTAS chooses by
examining the query plan to see which columns, if any, the query optimizer chooses
for sorting and distributing data. If the top node of the query plan is a simple
sequential scan from a single table (XN Seq Scan), then CTAS generally uses the
source table's distribution style and sort key. If the top node of the query
plan is anything other a sequential scan (such as XN Limit, XN Sort, XN
HashAggregate, and so on), CTAS makes a best effort to choose the optimal
distribution style and sort key based on the query plan.

For example, suppose you create five tables using the following types of SELECT
clauses:

- A simple select statement
- A limit clause
- An order by clause using LISTID
- An order by clause using QTYSOLD
- A SUM aggregate function with a group by clause.

The following examples show the query plan for each CTAS statement.

```
explain create table sales1_simple as select listid, dateid, qtysold from sales;
                           QUERY PLAN
----------------------------------------------------------------
 XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=8)
(1 row)


explain create table sales2_limit as select listid, dateid, qtysold from sales limit 100;
                              QUERY PLAN
----------------------------------------------------------------------
 XN Limit  (cost=0.00..1.00 rows=100 width=8)
   ->  XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=8)
(2 rows)


explain create table sales3_orderbylistid as select listid, dateid, qtysold from sales order by listid;
                               QUERY PLAN
------------------------------------------------------------------------
 XN Sort  (cost=1000000016724.67..1000000017155.81 rows=172456 width=8)
   Sort Key: listid
   ->  XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=8)
(3 rows)


explain create table sales4_orderbyqty as select listid, dateid, qtysold from sales order by qtysold;
                               QUERY PLAN
------------------------------------------------------------------------
 XN Sort  (cost=1000000016724.67..1000000017155.81 rows=172456 width=8)
   Sort Key: qtysold
   ->  XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=8)
(3 rows)


explain create table sales5_groupby as select listid, dateid, sum(qtysold) from sales group by listid, dateid;
                              QUERY PLAN
----------------------------------------------------------------------
 XN HashAggregate  (cost=3017.98..3226.75 rows=83509 width=8)
   ->  XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=8)
(2 rows)

```

To view the distribution key and sort key for each table, query the PG_TABLE_DEF
system catalog table, as shown following.

```
select * from pg_table_def where tablename like 'sales%';

      tablename       |   column   | distkey | sortkey
----------------------+------------+---------+---------
 sales                | salesid    | f       |       0
 sales                | listid     | t       |       0
 sales                | sellerid   | f       |       0
 sales                | buyerid    | f       |       0
 sales                | eventid    | f       |       0
 sales                | dateid     | f       |       1
 sales                | qtysold    | f       |       0
 sales                | pricepaid  | f       |       0
 sales                | commission | f       |       0
 sales                | saletime   | f       |       0
 sales1_simple        | listid     | t       |       0
 sales1_simple        | dateid     | f       |       1
 sales1_simple        | qtysold    | f       |       0
 sales2_limit         | listid     | f       |       0
 sales2_limit         | dateid     | f       |       0
 sales2_limit         | qtysold    | f       |       0
 sales3_orderbylistid | listid     | t       |       1
 sales3_orderbylistid | dateid     | f       |       0
 sales3_orderbylistid | qtysold    | f       |       0
 sales4_orderbyqty    | listid     | t       |       0
 sales4_orderbyqty    | dateid     | f       |       0
 sales4_orderbyqty    | qtysold    | f       |       1
 sales5_groupby       | listid     | f       |       0
 sales5_groupby       | dateid     | f       |       0
 sales5_groupby       | sum        | f       |       0

```

The following table summarizes the results. For simplicity, we omit cost, rows,
and width details from the explain plan.

| Table              | CTAS SELECT statement                                                    | Explain plan top node             | Dist key    | Sort key |
| ------------------ | ------------------------------------------------------------------------ | --------------------------------- | ----------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S1_SIMPLE          | `select listid, dateid, qtysold from sales`                              | `XN Seq Scan on sales ...`        | LISTID      | DATEID   |
| S2_LIMIT           | `select listid, dateid, qtysold from sales limit 100`                    | `XN Limit ...`                    | None (EVEN) | None     |
| S3_ORDER_BY_LISTID | `select listid, dateid, qtysold from sales order by listid`              | `XN Sort ...` `Sort Key: listid`  | LISTID      | LISTID   |
| S4_ORDER_BY_QTY    | `select listid, dateid, qtysold from sales order by qtysold`             | `XN Sort ...` `Sort Key: qtysold` | LISTID      | QTYSOLD  |
| S5_GROUP_BY        | `select listid, dateid, sum(qtysold) from sales group by listid, dateid` | `XN HashAggregate ...`            | None (EVEN) | None     | You can explicitly specify distribution style and sort key in the CTAS statement. For example, the following statement creates a table using EVEN distribution and specifies SALESID as the sort key. `create table sales_disteven diststyle even sortkey (salesid) as select eventid, venueid, dateid, eventname from event;` ## Compression encoding ENCODE AUTO is used as the default for tables. Amazon Redshift automatically manages compression encoding for all columns in the table. ## Distribution of incoming data When the hash distribution scheme of the incoming data matches that of the target table, no physical distribution of the data is actually necessary when the data is loaded. For example, if a distribution key is set for the new table and the data is being inserted from another table that is distributed on the same key column, the data is loaded in place, using the same nodes and slices. However, if the source and target tables are both set to EVEN distribution, data is redistributed into the target table. ## Automatic ANALYZE operations Amazon Redshift automatically analyzes tables that you create with CTAS commands. You do not need to run the ANALYZE command on these tables when they are first created. If you modify them, you should analyze them in the same way as other tables. |
