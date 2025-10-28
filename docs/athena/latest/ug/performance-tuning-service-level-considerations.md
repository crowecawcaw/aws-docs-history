# Optimize service

use

Service level considerations include the number of workloads you run per account,
service quotas not only for Athena, but across services, and thinking about how to reduce
'out of resource' errors.

###### Topics

- [Operate multiple workloads
  within the same account](#performance-tuning-service-quotas "#performance-tuning-service-quotas")
- [Reduce 'out of resource'
  errors](#performance-tuning-resource-limits "#performance-tuning-resource-limits")

## Operate multiple workloads

within the same account

Athena uses quotas to limit query concurrency and API request rates at the account
level. Exceeding these quotas can cause queries to fail during execution or at
submission time. For more information about these quotas, see [Service Quotas](service-limits.md "service-limits.md").

If you operate multiple workloads within the same AWS account, your workloads
compete for the same account-level quota. For example, if one workload experiences
an unexpected burst of queries, another workload running in the same account may see
elevated queue time, or in the worst case query submission failures due to
throttling.

We recommend that you use CloudWatch to monitor your service usage through graphs and
dashboards. You can also configure CloudWatch alarms that alert you when your usage
approaches the service quota for concurrent queries, allowing you to take action
before reaching quota limits. For more information, see [Monitor Athena usage metrics with
CloudWatch](monitoring-athena-usage-metrics.md "monitoring-athena-usage-metrics.md").

To control query concurrency and isolate workloads within your account, use
capacity reservations. Capacity reservations provide dedicated query processing
capacity within a single account. Capacity is measured in Data Processing Units
(DPUs) and can be added or removed to increase or decrease query concurrency,
respectively. Capacity reservations allow you to isolate workloads within your
account from one another by assigning capacity to one or more workgroups. For more
information, see [Manage query processing capacity](capacity-management.md "capacity-management.md").

While you should isolate unrelated workloads in different AWS accounts (such as
isolating development from production environments), this approach does not provide
a scalable way to increase query concurrency. Instead, use capacity reservations to
manage and scale your query processing needs within a single account.

### Consider quotas in

other services

When Athena runs a query, it can call other services that enforce quotas.
During query execution, Athena can make API calls to the AWS Glue Data Catalog, Amazon S3, and
other AWS services like IAM and AWS KMS. If you use [federated queries](federated-queries.md "federated-queries.md"), Athena also calls AWS Lambda. All of these services
have their own limits and quotas that can be exceeded. When a query execution
encounters errors from these services, it fails and includes the error from the
source service. Recoverable errors are retried, but queries can still fail if
the issue does not resolve itself in time. Make sure to read error messages
thoroughly to determine if they come from Athena or from another service. Some of
the relevant errors are covered in this performance tuning section.

For more information about working around errors caused by Amazon S3 service
quotas, see [Avoid having too
many files](performance-tuning-data-optimization-techniques.md#performance-tuning-avoid-having-too-many-files "performance-tuning-data-optimization-techniques.md#performance-tuning-avoid-having-too-many-files") later in
this document. For more information about Amazon S3 performance optimization, see
[Best practices
design patterns: optimizing Amazon S3 performance](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md") in the
_Amazon S3 User Guide_.

## Reduce 'out of resource'

errors

Athena runs queries in a distributed query engine. When you submit a query, the
Athena engine query planner estimates the compute capacity required to run the query
and prepares a cluster of compute nodes accordingly. Some queries like DDL queries
run on only one node. Complex queries over large data sets run on much bigger
clusters. The nodes are uniform, with the same memory, CPU, and disk configurations.
Athena scales out, not up, to process more demanding queries.

Sometimes the demands of a query exceed the resources available to the cluster
running the query. When this happens, the query fails with the error
**`Query exhausted resources at this scale factor`**.

The resource most commonly exhausted is memory, but in rare cases it can also be
disk space. Memory errors commonly occur when the engine performs a join or a window
function, but they can also occur in distinct counts and aggregations.

Even if a query fails with an 'out of resource' error once, it might succeed when
you run it again. Query execution is not deterministic. Factors such as how long it
takes to load data and how intermediate datasets are distributed over the nodes can
result in different resource usage. For example, imagine a query that joins two
tables and has a heavy skew in the distribution of the values for the join
condition. Such a query can succeed most of the time but occasionally fail when the
most common values end up being processed by the same node.

To prevent your queries from exceeding available resources, use the performance
tuning tips mentioned in this document. In particular, for tips on how to optimize
queries that exhaust the resources available, see [Optimize joins](performance-tuning-query-optimization-techniques.md#performance-tuning-optimizing-joins "performance-tuning-query-optimization-techniques.md#performance-tuning-optimizing-joins"), [Reduce the scope of
window functions, or remove them](performance-tuning-query-optimization-techniques.md#performance-tuning-optimizing-window-functions "performance-tuning-query-optimization-techniques.md#performance-tuning-optimizing-window-functions"), and [Optimize queries by using approximations](performance-tuning-query-optimization-techniques.md#performance-tuning-optimizing-queries-by-using-approximations "performance-tuning-query-optimization-techniques.md#performance-tuning-optimizing-queries-by-using-approximations").
