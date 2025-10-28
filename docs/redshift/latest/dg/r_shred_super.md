Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Shredding semi-structured data into SUPER columns with materialized views

With Amazon Redshift, you can improve query performance by shredding
data into SUPER columns using materialized views. Shredding refers to the process of breaking
down complex data types like semi-structured JSON or XML into smaller, flatter columns. SUPER
columns are a specialized form of columnar storage optimized for rapidly scanning shredded data.

The following sections describe the steps and considerations for shredding data into SUPER
columns using materialized views in Amazon Redshift.

The following example shows a materialized view definition that shreds the nested data with the resulting columns still being the SUPER data type.

```
SELECT c.c_name, o.o_orderstatus
FROM customer_orders_lineitem c, c.c_orders o;
```

The following example shows a materialized view definition that creates conventional Amazon Redshift scalar columns from the shredded data.

```
SELECT c.c_name, c.c_orders[0].o_totalprice
FROM customer_orders_lineitem c;
```

You can create a single materialized view super_mv to accelerate both queries.

To answer the first query, you must materialize the attribute o_orderstatus. You can
omit the attribute c_name because it doesn't involve nested navigation nor
unnesting. You must also include in the materialized view the attribute c_custkey of
customer_orders_lineitem to be able to join the base table with the materialized
view.

To answer the second query, you must also materialize the attribute o_totalprice and
the array index o_idx of c_orders. Hence, you can access the index 0 of
c_orders.

```
CREATE MATERIALIZED VIEW super_mv distkey(c_custkey) sortkey(c_custkey) AS (
  SELECT c_custkey, o.o_orderstatus, o.o_totalprice, o_idx
  FROM customer_orders_lineitem c, c.c_orders o AT o_idx
);
```

The attributes o_orderstatus and o_totalprice of the materialized view super_mv are SUPER.

The materialized view super_mv will be refreshed incrementally upon changes to the
base table customer_orders_lineitem.

```
REFRESH MATERIALIZED VIEW super_mv;
INFO: Materialized view super_mv was incrementally updated successfully.
```

To rewrite the first PartiQL query as a regular SQL query, join
customer_orders_lineitem with super_mv as follows.

```
SELECT c.c_name, v.o_orderstatus
FROM customer_orders_lineitem c
JOIN super_mv v ON c.c_custkey = v.c_custkey;
```

Similarly, you can rewrite the second PartiQL query. The following example uses a filter on o_idx = 0.

```
SELECT c.c_name, v.o_totalprice
FROM customer_orders_lineitem c
JOIN super_mv v ON c.c_custkey = v.c_custkey
WHERE v.o_idx = 0;
```

In the CREATE MATERIALIZED VIEW command, specify c_custkey as distribution key and
sort key for super_mv. Amazon Redshift performs an efficient merge join, assuming that
c_custkey is also the distribution key and sort key of customer_orders_lineitem. If
that isn’t the case, you can specify c_custkey as the sort key and distribution key
of customer_orders_lineitem as follows.

```
ALTER TABLE customer_orders_lineitem
ALTER DISTKEY c_custkey, ALTER SORTKEY (c_custkey);
```

Use the EXPLAIN statement to verify that Amazon Redshift performs a merge join on the
rewritten queries.

```
EXPLAIN
      SELECT c.c_name, v.o_orderstatus
      FROM customer_orders_lineitem c JOIN super_mv v ON c.c_custkey = v.c_custkey;

      QUERY PLAN
      ------------------------------------------------------------------------------------------------------
      XN Merge Join DS_DIST_NONE  (cost=0.00..34701.82 rows=1470776 width=27)
      Merge Cond: ("outer".c_custkey = "inner".c_custkey)
      ->  XN Seq Scan on mv_tbl__super_mv__0 derived_table2  (cost=0.00..14999.86 rows=1499986 width=13)
      ->  XN Seq Scan on customer_orders_lineitem c  (cost=0.00..999.96 rows=99996 width=30)
      (4 rows)
```
