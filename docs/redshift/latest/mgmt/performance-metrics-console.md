

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Viewing performance data
<a name="performance-metrics-console"></a>

In this section, you can find how to view performance data in the Amazon Redshift console, which includes information about cluster and query performance. Additionally, you can create alarms on cluster metrics directly from the Amazon Redshift console.

When you view performance data in the Amazon Redshift console, you view it by cluster. The performance data graphs for a cluster are designed to give you access to data to answer your most common performance questions. For some performance data (see [Performance data in Amazon Redshift](metrics-listing.md)), you can also use CloudWatch to further customize your metrics graphs. For example, you can choose longer times or combine metrics across clusters. For more information about working with the CloudWatch console, see [Performance metrics in the CloudWatch console](using-cloudwatch-console.md). 

To learn how to monitor, isolate, and optimize your queries using the query monitoring features on the Amazon Redshift console, watch the following video. 

[![AWS Videos](http://img.youtube.com/vi/Wdvb5iYVnLg/0.jpg)](http://www.youtube.com/watch?v=Wdvb5iYVnLg)


**Topics**
+ [Viewing cluster performance data](performance-metrics-perf.md)
+ [Viewing query history data](performance-metrics-query-history.md)
+ [Viewing database performance data](performance-metrics-database-performance.md)
+ [Viewing workload concurrency and concurrency scaling data](performance-metrics-concurrency-scaling.md)
+ [Viewing automatic optimization data](performance-metrics-autonomics.md)
+ [Viewing queries and loads](performance-metrics-queries.md)
+ [Viewing and analyzing query details](performance-metrics-query-execution-details.md)
+ [Viewing cluster performance as queries run](performance-metrics-query-cluster.md)
+ [Viewing cluster metrics during load operations](performance-metrics-loads.md)
+ [Viewing the cluster workload breakdown chart](analyze-workload-performance.md)