

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Refreshing a materialized view
<a name="materialized-view-refresh"></a>

This topic describes how to refresh the data in a material view from the underlying tables.

When you create a materialized view, its contents reflect the state of the underlying database relations (tables or other materialized views) at that time. The data in the materialized view remains unchanged, even when applications change the data in the underlying tables. To update the data in the materialized view, you can use the `REFRESH MATERIALIZED VIEW` statement at any time to manually refresh materialized views. When you use this statement, Amazon Redshift identifies changes that have taken place in the base relations and applies those changes to the materialized view.

Amazon Redshift has two strategies for refreshing a materialized view: 
+ In many cases, Amazon Redshift can perform an incremental refresh. In an *incremental refresh*, Amazon Redshift quickly identifies the changes to the data in the base relations since the last refresh and updates the data in the materialized view. Incremental refresh is supported on the following SQL constructs used in the query when defining the materialized view:
  + Constructs that contain the clauses SELECT, FROM, [INNER] JOIN, WHERE, GROUP BY, or HAVING.
  + Constructs that contain aggregations, such as SUM, MIN, MAX, AVG, and COUNT.
  + Most built-in SQL functions, specifically the ones that are immutable, given that these have the same input arguments and always produce the same output. 

  Incremental refresh is also supported for a materialized view that's based on a datashare table or another materialized view (a nested materialized view).
+ If an incremental refresh isn't possible, then Amazon Redshift performs a full refresh. A *full refresh* reruns the underlying SQL statement (the materialized view definition), replacing all of the data in the materialized view. For the scenarios where an incremental refresh isn't supported, see [Limitations](#materialized-view-refresh-limitations).
+ Amazon Redshift automatically chooses the refresh method for a materialized view depending on the SELECT query used to define the materialized view. 

Amazon Redshift performs a full recompute instead of an incremental refresh in the following additional cases:
+ A vacuum operation on a base table ran with the FORCE option, or reclaimed rows under low-disk-space conditions, while the materialized view was not up to date. For more information about the FORCE option, see [VACUUM](r_VACUUM_command.md).
+ The materialized view has not been refreshed for an extended period. To keep vacuum operations on base tables effective, Amazon Redshift marks stale materialized views that have not been refreshed recently for full recompute.

## Nested materialized views
<a name="materialized-view-refresh-nested"></a>

A materialized view can be defined on top of other materialized view(s). To refresh such a materialized view, you must explicitly use the `CASCADE` keyword at the top-most materialized view refresh. For example, assume the following nested materialized view structure:

```
CREATE TABLE t(a INT);
CREATE MATERIALIZED VIEW u AS SELECT * FROM t;
CREATE MATERIALIZED VIEW v AS SELECT * FROM u;
CREATE MATERIALIZED VIEW w AS SELECT * FROM v;

-- w -> v -> u -> t

INSERT INTO t VALUES (1);
```

To bring w fully up to date you have two choices:
+ (Recommended) Refresh w using `REFRESH MATERIALIZED VIEW w CASCADE` command. This command executes refresh of all materialized views in a single transaction. 
+ Refresh u, v, and w as separate commands, in dependency order (first u, then v, then w). 

If the `CASCADE` keyword is not explicitly used, the materialized view will be refreshed in `RESTRICT` mode, refreshing only the current materialized view. The following examples show an informational message when you run `REFRESH MATERIALIZED VIEW` on a materialized view that depends on an out-of-date materialized view.

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

In the examples above with the cascade refresh option, materialized view u is refreshed first, materialized view v is refreshed next, and materialized view w is not refreshed.

The following example shows how you can create a full refresh plan for a materialized view programmatically. To refresh the materialized view v, first refresh materialized view u. To refresh materialized view w, first refresh materialized view u and then materialized view v.

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
<a name="materialized-view-refresh-limitations"></a>

Amazon Redshift doesn't support cascading refresh for materialized views based on sources other than:
+ Local tables
+ Shared tables
+ Local MVs
+ Streaming MVs

Cascading refresh does not extend to shared materialized views.

Amazon Redshift doesn't support incremental refresh for materialized views that are defined with a query using the following SQL elements:
+ OUTER JOIN (RIGHT, LEFT, or FULL).
+ The set operations UNION, INTERSECT, EXCEPT, and MINUS.
+ The aggregate functions MEDIAN, PERCENTILE\_CONT, LISTAGG, STDDEV\_SAMP, STDDEV\_POP, APPROXIMATE COUNT, APPROXIMATE PERCENTILE, and bitwise aggregate functions.
**Note**  
The COUNT, SUM, and AVG aggregate functions are supported.
+ DISTINCT aggregate functions, such as DISTINCT COUNT, DISTINCT SUM, and so on.
+ Window functions.
+ A query that uses temporary tables for query optimization, such as optimizing common subexpressions.
+ Subqueries.
+ External tables referencing the following formats in the query that defines the materialized view. 
  +  Delta Lake 
  +  Hudi 

  Incremental refresh is supported for materialized views defined using formats other than those listed above. For more information, see [Materialized views on external data lake tables in Amazon Redshift Spectrum](materialized-view-external-table.md). 

## Using Auto Refresh with a materialized view
<a name="materialized-view-auto-refresh"></a>

Amazon Redshift can automatically refresh materialized views with up-to-date data from its base tables when materialized views are created with or altered to have Auto Refresh enabled.

With Auto Refresh enabled, Amazon Redshift initiates materialized view refreshes once per configured refresh interval. A refresh occurs only if the materialized view is stale. If the materialized view is not stale, Auto Refresh doesn't run and no compute resources are used. You can enable Auto Refresh for materialized views using [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md) and [ALTER MATERIALIZED VIEW](r_ALTER_MATERIALIZED_VIEW.md) with the `AUTO REFRESH YES` option. Optionally, you can specify a custom refresh interval with the `AUTO REFRESH YES INTERVAL {{seconds}}` clause. The interval must be between 60 seconds and 86,400 seconds (24 hours). If you don't specify an interval, Amazon Redshift uses a cluster-wide default refresh interval of 300 seconds (5 minutes). A superuser or administrator can change this default by using ALTER SYSTEM SET default\_mv\_auto\_refresh\_interval = {{seconds}}. For more information, see [ALTER SYSTEM](r_ALTER_SYSTEM.md). A refresh interval set for an individual materialized view takes precedence over the cluster-wide default.

Auto Refresh queries run with the same priority as other user queries and also benefit from concurrency scaling. To prevent load spikes, when multiple materialized views share the same refresh interval, Amazon Redshift spreads out their refresh times so that they don't all run at once.

Changing the refresh interval of an existing materialized view with ALTER MATERIALIZED VIEW doesn't cause a full recompute of the materialized view.

To view the refresh interval currently configured for your auto-refreshable materialized views, query the `autorefresh_interval` and `has_default_autorefresh_interval` columns in [STV\_MV\_INFO](r_STV_MV_INFO.md) or [SVV\_MV\_INFO](r_SVV_MV_INFO.md).

**Note**  
With [patch release 206](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html#cluster-version-206), Amazon Redshift supports user-defined refresh intervals for all user-defined, auto-refreshable materialized views except streaming materialized views.

Consider the following when you refresh materialized views:
+ You can still manually refresh a materialized view using the REFRESH MATERIALIZED VIEW command even if you haven't enabled Auto Refresh for the materialized view.
+ Auto Refresh is supported on materialized views defined on datasharing tables or Iceberg tables but not on the combination of the two.
+ For refresh status, you can check [SYS\_MV\_REFRESH\_HISTORY](SYS_MV_REFRESH_HISTORY.md), which records queries that were user-initiated or run by Auto Refresh. 
+ To run full recompute REFRESH of materialized views, make sure that you have the CREATE permission on schemas. For more information, see [GRANT](r_GRANT.md).

### Recommendations for setting the refresh interval
<a name="materialized-view-auto-refresh-interval-recommendations"></a>

Consider the following recommendations when you configure Auto Refresh intervals for your materialized views:
+ To keep specific time-sensitive materialized views fresher, set a shorter interval on just those materialized views by using `ALTER MATERIALIZED VIEW` with the `AUTO REFRESH YES INTERVAL` clause (down to the 60-second minimum), rather than lowering the cluster-wide default for every materialized view.
+ If your base tables are updated infrequently, consider setting the interval to the maximum of 86,400 seconds (24 hours). You can't specify an interval longer than 24 hours. Amazon Redshift doesn't run Auto Refresh for a materialized view that is already up to date. The only cost is a staleness check, which has negligible overhead.
+ When you choose an interval, consider how long the materialized view takes to refresh and how frequently its base tables change. Only one Auto Refresh can run at a time for a given materialized view. If you set the interval too short for a materialized view that takes a long time to refresh, the materialized view might refresh continuously without ever becoming up to date.
+ To change the refresh cadence for all materialized views on the cluster or workgroup, set the cluster-wide default by using `ALTER SYSTEM SET default_mv_auto_refresh_interval`.
+ If automatically refreshing materialized views at your chosen interval competes with other workloads for resources, consider the following:
  + For a provisioned cluster, resize the cluster. For more information, see [Resizing clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html) in the *Amazon Redshift Management Guide*.
  + For a serverless workgroup, increase the maximum compute capacity (RPUs). For more information, see [Redshift Serverless capacity](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-capacity.html#serverless-auto-optimization) in the *Amazon Redshift Management Guide*.
  + Enable concurrency scaling, or increase the number of scaling clusters by using `max_concurrency_scaling_clusters`. For more information, see [Concurrency scaling](concurrency-scaling.md) and [max\_concurrency\_scaling\_clusters](r_max_concurrency_scaling_clusters.md).