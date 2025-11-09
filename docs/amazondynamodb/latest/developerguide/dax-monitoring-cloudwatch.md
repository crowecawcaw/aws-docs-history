# Monitoring with Amazon CloudWatch

You can monitor DynamoDB Accelerator (DAX) using Amazon CloudWatch, which collects and processes raw data
from DAX into readable, near real-time metrics. These statistics are recorded for a
period of two weeks. You can then access historical information for a better perspective
on how your web application or service is performing. By default, DAX metric data is
sent to CloudWatch automatically. For more information, see [What Is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the
_Amazon CloudWatch User Guide_.

###### Topics

- [How do I use DAX metrics?](#dax-how-to-use-metrics "#dax-how-to-use-metrics")
- [Viewing DAX metrics and
  dimensions](dax-metrics-dimensions-dax.md "dax-metrics-dimensions-dax.md")
- [Creating CloudWatch alarms to monitor DAX](dax-creating-alarms.md "dax-creating-alarms.md")
- [Production monitoring](dax-production-monitoring.md "dax-production-monitoring.md")

## How do I use DAX metrics?

The metrics reported by DAX provide information that you can analyze in different ways. The following list
shows some common uses for the metrics. These are suggestions to get you started, and not a comprehensive list.

| How Can I?                              | Relevant Metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Determine if any system errors occurred | Monitor `FaultRequestCount` to determine if any<br>requests resulted in an HTTP 500 (server error) code. This can<br>indicate a DAX internal service error or an HTTP 500 in the<br>underlying table's [SystemErrors metric](metrics-dimensions.md "metrics-dimensions.md").                                                                                                                                                                                                                                                                            |
| Determine if any user errors occurred   | Monitor `ErrorRequestCount` to determine if any<br>requests resulted in an HTTP 400 (client error) code. If you see<br>the error count growing, you might want to investigate and make<br>sure you are sending correct client requests.                                                                                                                                                                                                                                                                                                                 |
| Determine if any cache misses occurred  | Monitor `ItemCacheMisses` to determine the number<br>of times an item was not found in the cache, and<br>`QueryCacheMisses` and<br>`ScanCacheMisses` to determine the number of<br>times a query or scan result was not found in the cache.                                                                                                                                                                                                                                                                                                             |
| Monitor cache hit rates                 | Use [CloudWatch Metric Math](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md") to define a cache hit rate<br>metric using math expressions.<br>For example, for the item cache, you can use the expression<br>m1/SUM([m1, m2])\*100, where m1 is the `ItemCacheHits`<br>metric and m2 is the `ItemCacheMisses` metric for<br>your cluster. For the query and scan caches, you can follow the<br>same pattern using the corresponding query and scan cache<br>metric. |
