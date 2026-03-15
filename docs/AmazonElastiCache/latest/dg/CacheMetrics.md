# Monitoring use with CloudWatch Metrics

ElastiCache provides metrics that enable you to monitor your clusters. You can access
these metrics through CloudWatch. For more information on CloudWatch, see the [CloudWatch documentation.](https://aws.amazon.com/documentation/cloudwatch/ "https://aws.amazon.com/documentation/cloudwatch/")

ElastiCache provides both host-level metrics (for example, CPU usage) and metrics that are
specific to the cache engine software (for example, cache gets and cache misses). These
metrics are measured and published for each Cache node in 60-second intervals.

###### Important

You should consider setting CloudWatch alarms on certain key metrics, so that you will be notified if your cluster's performance starts to degrade.
For more information, see [Which Metrics Should I Monitor?](CacheMetrics.md "CacheMetrics.md") in this guide.

###### Topics

- [Host-Level Metrics](CacheMetrics.md "CacheMetrics.md")
- [Metrics for Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md")
- [Metrics for Memcached](CacheMetrics.md "CacheMetrics.md")
- [Which Metrics Should I Monitor?](CacheMetrics.md "CacheMetrics.md")
- [Choosing Metric Statistics and Periods](CacheMetrics.md "CacheMetrics.md")
- [Monitoring CloudWatch Cluster and Node Metrics](CloudWatchMetrics.md "CloudWatchMetrics.md")
