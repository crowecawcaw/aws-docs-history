Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing performance data

In this section, you can find how to view performance data in the Amazon Redshift console,
which includes information about cluster and query performance. Additionally, you can
create alarms on cluster metrics directly from the Amazon Redshift console.

When you view performance data in the Amazon Redshift console, you view it by cluster. The
performance data graphs for a cluster are designed to give you access to data to answer
your most common performance questions. For some performance data (see [Performance data in Amazon Redshift](metrics-listing.md "metrics-listing.md")), you can also use CloudWatch
to further customize your metrics graphs. For example, you can choose longer times or
combine metrics across clusters. For more information about working with the CloudWatch
console, see [Performance metrics in the CloudWatch
console](using-cloudwatch-console.md "using-cloudwatch-console.md").

To learn how to monitor, isolate, and optimize your queries using the
query monitoring features on the Amazon Redshift console, watch the following video.

###### Topics

- [Viewing cluster performance data](performance-metrics-perf.md "performance-metrics-perf.md")
- [Viewing query history
  data](performance-metrics-query-history.md "performance-metrics-query-history.md")
- [Viewing database
  performance data](performance-metrics-database-performance.md "performance-metrics-database-performance.md")
- [Viewing workload
  concurrency and concurrency scaling data](performance-metrics-concurrency-scaling.md "performance-metrics-concurrency-scaling.md")
- [Viewing automatic optimization data](performance-metrics-autonomics.md "performance-metrics-autonomics.md")
- [Viewing queries and loads](performance-metrics-queries.md "performance-metrics-queries.md")
- [Viewing and analyzing
  query details](performance-metrics-query-execution-details.md "performance-metrics-query-execution-details.md")
- [Viewing cluster performance as
  queries run](performance-metrics-query-cluster.md "performance-metrics-query-cluster.md")
- [Viewing cluster metrics during load
  operations](performance-metrics-loads.md "performance-metrics-loads.md")
- [Viewing the cluster workload
  breakdown chart](analyze-workload-performance.md "analyze-workload-performance.md")
