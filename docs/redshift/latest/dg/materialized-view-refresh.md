Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Refreshing a materialized view

This topic describes how to refresh the data in a material view from the underlying tables.

When you create a materialized view, its contents reflect the state of the underlying
database relations (tables or other materialized views) at that time. The data in the
materialized view remains unchanged, even when applications change the data in the
underlying tables. To update the data in the materialized view, you can use the
`REFRESH MATERIALIZED VIEW` statement at any time to manually refresh
materialized views. When you use this statement, Amazon Redshift identifies changes that have taken
place in the base relations and applies those changes to the materialized view.

Amazon Redshift has two strategies for
refreshing a materialized view:

- In many cases, Amazon Redshift can perform an incremental refresh. In an _incremental refresh_, Amazon Redshift quickly identifies the
  changes to the data in the base relations since the last refresh and updates the
  data in the materialized view. Incremental refresh is supported on the following
  SQL constructs used in the query when defining the materialized view:

      + Constructs that contain the clauses SELECT, FROM, [INNER] JOIN, WHERE,
       GROUP BY, or HAVING.
      + Constructs that contain aggregations, such as SUM, MIN, MAX, AVG, and COUNT.
      + Most built-in SQL functions, specifically the ones that are immutable,
       given that these have the same input arguments and always produce the
       same output.

  Incremental refresh is also supported for a materialized view that's based on a datashare table or materialized view.

- If an incremental refresh isn't possible, then Amazon Redshift performs a full
  refresh. A _full refresh_ reruns the underlying
  SQL statement, replacing all of the data in the materialized view.
- Amazon Redshift automatically chooses the refresh method for a materialized view depending
  on the SELECT query used to define the materialized view.

## Nested materialized views

A materialized view can be defined on top of other materialized view(s). To
refresh such a materialized view, you must explicitly use the `CASCADE`
keyword at the top-most materialized view refresh. For example, assume the following
nested materialized view structure:

```
CREATE TABLE t(a INT);
CREATE MATERIALIZED VIEW u AS SELECT * FROM t;
CREATE MATERIALIZED VIEW v AS SELECT * FROM u;
CREATE MATERIALIZED VIEW w AS SELECT * FROM v;

-- w -> v -> u -> t

INSERT INTO t VALUES (1);
```

To bring w fully up to date you have two choices:

- (Recommended) Refresh w using `REFRESH MATERIALIZED VIEW w CASCADE` command. This command executes refresh of all materialized views in a single
  transaction.
- Refresh u, v, and w as separate commands, in dependency order (first u, then v, then w).

If the `CASCADE` keyword is not explicitly used, the materialized view
will be refreshed in `RESTRICT` mode, refreshing only the current
materialized view. The following examples show an informational message when you run
`REFRESH MATERIALIZED VIEW` on a materialized view that depends on an
out-of-date materialized view.

```
REFRESH MATERIALIZED VIEW w;
INFO:  Materialized view w is already up to date.  However, it depends on another materialized view that is not up to date.

REFRESH MATERIALIZED VIEW w CASCADE;
INFO:  Materialized view w was incrementally updated successfully.
```

```
REFRESH MATERIALIZED VIEW v;
INFO: Materialized view v is already up to date. However, it depends on another materialized view that is not up to date.

REFRESH MATERIALIZED VIEW v CASCADE;
INFO: Materialized view v was incrementally updated successfully.
```

In the examples above with the cascade refresh option, materialized view u is
refreshed first, materialized view v is refreshed next, and materialized view w is
not refreshed.

The following example shows how you can create a full refresh plan for a materialized
view programmatically. To refresh the materialized view v, first refresh materialized
view u. To refresh materialized view w, first refresh materialized view u and then
materialized view v.

```
WITH RECURSIVE recursive_deps (mv_tgt, lvl, mv_dep) AS
( SELECT trim(name) as mv_tgt, 0 as lvl, trim(ref_name) as mv_dep
  FROM stv_mv_deps
  UNION ALL
  SELECT R.mv_tgt, R.lvl+1 as lvl, trim(S.ref_name) as mv_dep
  FROM stv_mv_deps S, recursive_deps R
  WHERE R.mv_dep = S.name
)

SELECT mv_tgt, mv_dep from recursive_deps
ORDER BY mv_tgt, lvl DESC;

 mv_tgt | mv_dep
--------+--------
 v      | u
 w      | u
 w      | v
(3 rows)
```

## Limitations

Amazon Redshift doesn't support cascading refresh for materialized views based on sources
other than:

- Local tables
- Local MVs
- Streaming MVs

Amazon Redshift doesn't support incremental refresh for materialized views that are defined with
a query using the following SQL elements:

- OUTER JOIN (RIGHT, LEFT, or FULL).
- The set operations UNION, INTERSECT, EXCEPT, and MINUS.
- The aggregate functions MEDIAN, PERCENTILE_CONT, LISTAGG,
  STDDEV_SAMP, STDDEV_POP, APPROXIMATE COUNT, APPROXIMATE PERCENTILE, and bitwise
  aggregate functions.

###### Note

The COUNT, SUM, and AVG aggregate functions are supported.

- DISTINCT aggregate functions, such as DISTINCT COUNT, DISTINCT
  SUM, and so on.
- Window functions.
- A query that uses temporary tables for query optimization, such as optimizing common subexpressions.
- Subqueries.
- External tables referencing the following formats in the query that defines
  the materialized view.

      + Delta Lake
      + Hudi

  Incremental refresh is supported for materialized views defined using formats
  other than those listed above. For more information, see [Materialized views on external data
  lake tables in Amazon Redshift Spectrum](materialized-view-external-table.md "materialized-view-external-table.md").

## Autorefreshing a materialized

view

Amazon Redshift can automatically refresh materialized views with up-to-date data from its
base tables when materialized views are created with or altered to have the
autorefresh option. Amazon Redshift autorefreshes materialized views as soon as possible
after base tables changes.

To complete refresh of the most important materialized views with minimal impact
to active workloads in your cluster, Amazon Redshift considers multiple factors. These
factors include current system load, the resources needed for refresh, available
cluster resources, and how often the materialized views are used.

Amazon Redshift prioritizes your workloads over autorefresh and might stop autorefresh to
preserve the performance of user workload. This approach might delay refresh of some
materialized views. In some cases, you might need more deterministic refresh
behavior for your materialized views. If so, consider using manual refresh as
described in [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md "materialized-view-refresh-sql-command.md") or scheduled refresh
using the Amazon Redshift scheduler API operations or the console.

You can set autorefresh for materialized views using CREATE MATERIALIZED VIEW. You can
also use the AUTO REFRESH clause to refresh materialized views automatically. For
more information about creating materialized views, see [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md"). You can turn on
autorefresh for a current materialized view by using [ALTER MATERIALIZED VIEW](r_ALTER_MATERIALIZED_VIEW.md "r_ALTER_MATERIALIZED_VIEW.md").

Consider the following when you refresh materialized views:

- You can still refresh a materialized view explicitly using REFRESH MATERIALIZED VIEW command
  even if you haven't enabled autorefresh for the materialized
  view.
- Auto refresh is supported on materialized views defined on datasharing tables or Iceberg tables but not on the combination of the two.
- For refresh status, you can check SVL_MV_REFRESH_STATUS, which records queries that were
  user-initiated or autorefreshed.
- To run REFRESH on recompute-only materialized views, make sure that you have the CREATE
  permission on schemas. For more information, see [GRANT](r_GRANT.md "r_GRANT.md").
