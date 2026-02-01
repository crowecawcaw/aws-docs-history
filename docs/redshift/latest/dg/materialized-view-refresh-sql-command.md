Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# REFRESH MATERIALIZED VIEW

Refreshes a materialized view.

When you create a materialized view, its contents reflect the state of the underlying
database table or tables at that time. The data in the materialized view remains unchanged,
even when applications make changes to the data in the underlying tables.

To update the data in a materialized view, you can use the `REFRESH MATERIALIZED
 VIEW` statement at any time. When you use this statement, Amazon Redshift identifies changes
that have taken place in the base table or tables, and then applies those changes to the
materialized view.

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").

## Syntax

```
REFRESH MATERIALIZED VIEW *mv\_name* [ RESTRICT | CASCADE ]
```

## Parameters

_mv_name_

The name of the materialized view to be refreshed.

RESTRICT

Optional keyword. Refreshes the specified materialized view but not its
dependent materialized views. The default if neither RESTRICT nor CASCADE is
specified.

CASCADE

Optional keyword. Refreshes the specified materialized view and all its
dependent materialized views.

## Usage notes

Only the owner of a materialized view can perform a `REFRESH MATERIALIZED
 VIEW` operation on that materialized view. Furthermore, the owner must have
SELECT privilege on the underlying base tables to successfully run `REFRESH
 MATERIALIZED VIEW`.

The `REFRESH MATERIALIZED VIEW` command runs as a transaction of its own.
Amazon Redshift transaction semantics are followed to determine what data from base
tables is visible to the `REFRESH` command, or when the changes made by the
`REFRESH` command are made visible to other transactions running in
Amazon Redshift.

- For incremental materialized views, `REFRESH MATERIALIZED VIEW` uses
  only those base table rows that are already committed. Therefore, if the refresh
  operation runs after a data manipulation language (DML) statement in the same
  transaction, then changes of that DML statement aren't visible to refresh.
- For a full refresh of a materialized view, `REFRESH MATERIALIZED
VIEW` sees all base table rows visible to the refresh transaction,
  according to usual Amazon Redshift transaction semantics.
- Depending on the input argument type, Amazon Redshift still supports
  incremental refresh for materialized views for the following functions with
  specific input argument types: DATE (timestamp), DATE_PART (date, time, interval,
  time-tz), DATE_TRUNC (timestamp, interval).
- Incremental refresh is supported on a materialized view where the base table is
  in a datashare.
- Refresh of shared materialized views from remote datasharing clusters is not supported for
  materialized views that contain references to other materialized views, Spectrum tables, tables defined in a different Redshift cluster or UDFs.
  Such materialized views can be refreshed from the local (producer) cluster.

Some operations in Amazon Redshift interact with materialized views. Some of these operations
might force a `REFRESH MATERIALIZED VIEW` operation to fully recompute the
materialized view even though the query defining the materialized view only uses the SQL
features eligible for incremental refresh. For example:

- Background vacuum operations might be blocked if materialized views aren't
  refreshed. After an internally defined threshold period, a vacuum operation is
  allowed to run. When this vacuum operation happens, any dependent materialized
  views are marked for recomputation upon the next refresh (even if they are
  incremental). For information about VACUUM, see [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md"). For more information about events and state
  changes, see [STL_MV_STATE](r_STL_MV_STATE.md "r_STL_MV_STATE.md").
- Some user-initiated operations on base tables force a materialized view to be
  fully recomputed next time that a REFRESH operation is run. Examples of such
  operations are a manually invoked VACUUM, a classic resize, an ALTER DISTKEY
  operation, an ALTER SORTKEY operation, and a truncate operation. Automatic
  operations in some cases can also result in a materialized view being fully
  recomputed the next time a REFRESH operation is run. For example, an auto-vacuum
  delete operation can cause a full recompute. For more information about events and
  state changes, see [STL_MV_STATE](r_STL_MV_STATE.md "r_STL_MV_STATE.md").

## Cascading refresh

The CASCADE option refreshes the specified materialized view and all its dependent
materialized views, in order of dependence: base MVs are REFRESHed before the MVs on top
(topological ordering). This allows you to update a nested set of materialized views in
a single command.

The RESTRICT option (the default if neither RESTRICT nor CASCADE is specified)
refreshes only the specified materialized view.

When using the CASCADE option, the following rules apply:

- Only the owner of the materialized view or a superuser can execute
  the `REFRESH MATERIALIZED VIEW ... CASCADE`command.
- If any of the materialized views in the cascade cannot be refreshed, the
  entire cascade operation will stop.

The cascading refresh functionality is only supported for MVs nested on top of local
and streaming materialized views. Materialized views with other source types, such as
Spectrum or Data Sharing, are not supported in cascade mode. CASCADE executes refresh in
a single transaction for all nested MVs.

## Incremental refresh for

materialized views in a datashare

Amazon Redshift supports automatic and incremental refresh for materialized views in a consumer
datashare when the base tables are shared. Incremental refresh is an operation where
Amazon Redshift identifies changes in the base table or tables that happened after the previous
refresh and updates only the corresponding records in the materialized view. For more
information about this behavior, see [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md#mv_CREATE_MARTERIALIZED_VIEW_datashare "materialized-view-create-sql-command.md#mv_CREATE_MARTERIALIZED_VIEW_datashare").

## Limitations for incremental

refresh

Amazon Redshift currently doesn't support incremental refresh for materialized views that
are defined with a query using any of the following SQL elements:

- OUTER JOIN (RIGHT, LEFT, or FULL).
- Set operations: UNION, INTERSECT, EXCEPT, MINUS.
- UNION ALL when it occurs in a subquery and an aggregate function, or a GROUP BY
  clause is present in the query, or the target materialized view contains a
  sortkey.
- Aggregate functions: MEDIAN, PERCENTILE_CONT, LISTAGG, STDDEV_SAMP, STDDEV_POP,
  APPROXIMATE COUNT, APPROXIMATE PERCENTILE, and bitwise aggregate functions.

###### Note

The COUNT, SUM, MIN, MAX, and AVG aggregate functions are supported.

- DISTINCT aggregate functions, such as DISTINCT COUNT, DISTINCT SUM, and so
  on.
- Window functions.
- A query that uses temporary tables for query optimization, such as optimizing
  common subexpressions.
- Subqueries
- External tables referencing the following formats in the query that defines the
  materialized view.

      + Delta Lake
      + Hudi

  Incremental refresh is supported for materialized views defined using formats
  other than those listed above. For more information, see [Materialized views on external data
  lake tables in Amazon Redshift Spectrum](materialized-view-external-table.md "materialized-view-external-table.md").

- Mutable functions, such as date-time functions, RANDOM and non-STABLE
  user-defined functions.
- For limitations regarding incremental refresh for zero-ETL integrations, see [Considerations when using
  zero-ETL integrations with Amazon Redshift](../mgmt/zero-etl.md "../mgmt/zero-etl.md").
- Accessing tables from more than one database.

For more information about materialized-view limitations, including the effect of
background operations like VACUUM on materialized-view refresh operations, see [Usage notes](#mv_REFRESH_MARTERIALIZED_VIEW_usage "#mv_REFRESH_MARTERIALIZED_VIEW_usage").

## Examples

The following example refreshes the `tickets_mv` materialized view.

```
REFRESH MATERIALIZED VIEW tickets_mv;
```

The following example refreshes the `products_mv` materialized view and
all its dependent materialized views:

```
REFRESH MATERIALIZED VIEW products_mv CASCADE;
```
