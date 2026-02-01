Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Automated materialized views

This topic describes how Amazon Redshift uses automated materialized views to improve performance.
Amazon Redshift creates materialized views automatically based on database activity and performance.
Amazon Redshift uses automated materialized views by default.

Materialized views are a powerful tool for improving query performance in Amazon Redshift.
They do this by storing a precomputed result set. Similar queries don't have to re-run
the same logic each time, because they can retrieve records from the existing result set.
Developers and analysts create materialized views after analyzing their workloads to
determine which queries would benefit, and whether the maintenance cost of each
materialized view is worthwhile. As workloads grow or change, these materialized views
must be reviewed to ensure they continue to provide tangible performance benefits.

The Automated Materialized Views (AutoMV) feature in Redshift enhances query performance by
automatically creating and managing materialized views based on workload monitoring and machine
learning algorithms. The following includes key features of AutoMV:

- _Continuous monitoring_ – Redshift continuously monitors the workload using machine learning techniques
  to identify opportunities for performance improvements through the creation of materialized views.
- _Automatic creation and deletion_ – When the system detects that a materialized view
  would be beneficial, it automatically creates and maintains it. Conversely, if a previously created AutoMV is no longer
  providing performance benefits, the system will automatically drop it.
- _No user activity requirement_ – The AutoMV feature only operates during periods
  of low user activity or workload running on the cluster. This ensures that the AutoMV operations do not interfere with or impact customer workloads.
- _CPU usage spikes_ – During times of no workload activity, the creation or refresh of materialized views
  by AutoMV may lead to spikes in CPU usage. This is a normal behavior as the system utilizes available resources to create and refresh materialized views.
- _User workload priority_ – If you initiate a workload while an AutoMV operation is in progress, the AutoMV task will stop
  to release resources for the user workload. This ensures that your workloads take priority over the AutoMV operations.
  While the AutoMV feature may lead to CPU usage spikes during periods of no user activity,
  it operates transparently and without impacting your workloads. The system manages materialized
  views to improve query performance and simultaneously prioritizes user workloads over AutoMV operations.

AutoMV behavior and capabilities are the same as user-created materialized views. They
are refreshed automatically and incrementally, using the same criteria and restrictions.
Just like materialized views created by users, [Automatic query rewriting to use
materialized views](materialized-view-auto-rewrite.md "materialized-view-auto-rewrite.md") identifies queries that can benefit
from system-created AutoMVs. It automatically rewrites those queries to use the
AutoMVs, improving query performance. Developers don't need to revise queries to take
advantage of AutoMV.

###### Note

Automated materialized views are refreshed intermittently. Queries rewritten to use AutoMV
always return the latest results. When Redshift detects that data
isn't up to date, queries aren't rewritten to read from automated materialized views. Instead, queries
select the latest data from base tables.

Any workload with queries that are used repeatedly can benefit from AutoMV. Common use cases include:

- _Dashboards_ - Dashboards are widely used to provide quick views of key
  business indicators (KPIs), events, trends, and other metrics. They often have a
  common layout with charts and tables, but show different views for filtering, or
  for dimension-selection operations, like drill down. Dashboards often have a
  common set of queries used repeatedly with different parameters. Dashboard
  queries can benefit greatly from automated materialized views.
- _Reports_ - Reporting queries may be scheduled at various
  frequencies, based on business requirements and the type of report.
  Additionally, they can be automated or on-demand. A common characteristic of
  reporting queries is that they can be long running and resource-intensive. With
  AutoMV, these queries don't need to be recomputed each time they run, which
  reduces runtime for each query and resource utilization in Redshift.
  To turn off automated materialized views, you update the `auto_mv` parameter group to `false`. For more
  information, see [Amazon Redshift parameter groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the Amazon Redshift Cluster Management Guide.

## SQL scope and considerations for automated materialized views

- An automated materialized view can be initiated and created by a query or subquery, provided
  it contains a `GROUP BY` clause or one of the following aggregate functions: SUM, COUNT, MIN, MAX or AVG. But it cannot contain any of the following:

      + Left, right, or full outer joins
      + Aggregate functions other than SUM, COUNT, MIN, MAX, and AVG. (These particular functions work with automatic query rewriting.)
      + Any aggregate function that includes DISTINCT
      + Any window functions
      + SELECT DISTINCT or HAVING clauses
      + Other materialized views

  It isn't guaranteed that a query that meets the criteria will initiate the
  creation of an automated materialized view. The system determines from which
  candidates to create a view, based on its expected benefit to the workload
  and cost in resources to maintain, which includes the cost to the system to
  refresh. Each resulting materialized view is usable by automatic query
  rewriting.

- Even though AutoMV might be initiated by a subquery or individual legs of set operators, the
  resulting materialized view won't contain subqueries or set
  operators.
- To determine if AutoMV was used for queries, view the EXPLAIN plan and look for `%_auto_mv_%` in the output. For more information,
  see [EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md").
- Automated materialized views aren't supported on external tables, such as datashares and federated tables.

## Automated materialized views limitations

Following are limitations for working with automated materialized views:

- _Maximum number of AutoMVs_ - The limit of automated materialized views is 200 per database in the cluster.
- _Storage space and capacity_ - An important characteristic of AutoMV is
  that it is performed using spare background cycles to help achieve that user
  workloads are not impacted. If the cluster is busy or running out of storage
  space, AutoMV ceases its activity. Specifically, at 80% of total cluster
  capacity, no new automated materialized views are created. At 90% of total
  capacity, they may be dropped to facilitate that user workloads continue
  without performance degradation. For more information about determining
  cluster capacity, see [STV_NODE_STORAGE_CAPACITY](r_STV_NODE_STORAGE_CAPACITY.md "r_STV_NODE_STORAGE_CAPACITY.md").

## Billing for automated materialized views

Amazon Redshift's automatic optimization capability creates and refreshes automated materialized views. There
is no charge for compute resources for this process. Storage of automated materialized views is charged at the regular rate for storage. For more information,
see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

## Additional resources

The following blog post provides further explanation regarding automated
materialized views. It details how they’re created, maintained, and dropped. It also explains the
underlying algorithms that drive these decisions: [Optimize your Amazon Redshift query performance with automated materialized views](https://aws.amazon.com/blogs//big-data/optimize-your-amazon-redshift-query-performance-with-automated-materialized-views/ "https://aws.amazon.com/blogs//big-data/optimize-your-amazon-redshift-query-performance-with-automated-materialized-views/").

This video begins with an explanation of materialized views and shows how they improve performance and conserve resources. It then provides an
in-depth explanation of automated materialized views with a process-flow animation and a live demonstration.
