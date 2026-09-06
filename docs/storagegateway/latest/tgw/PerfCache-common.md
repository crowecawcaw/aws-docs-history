

# Monitoring cache storage
<a name="PerfCache-common"></a>

You can find information following about how to monitor a gateway's cache storage and how to create an alarm so that you get a notification when parameters of the cache pass specified thresholds. Using this alarm, you know when to add cache storage to a gateway.

You only monitor cache storage in the cached volumes architecture. For more information, see [How Tape Gateway works](StorageGatewayConcepts.md).


| Item of Interest | How to Measure | 
| --- | --- | 
| Total usage of cache | Use the `CachePercentUsed` and `TotalCacheSize` metrics with the `Average` statistic. For example, use the `CachePercentUsed` with the `Average` statistic to analyze the cache usage over a period of time.<br />The `TotalCacheSize` metric changes only when you add cache to the gateway. | 
| Percent of read requests that are served from the cache | Use the `CacheHitPercent` metric with the `Average` statistic.<br />Typically, you want `CacheHitPercent` to remain high. | 
| Percent of the cache that is dirty—that is, it contains content that has not been uploaded to AWS | Use the `CachePercentDirty` metrics with the `Average` statistic.<br />Typically, you want `CachePercentDirty` to remain low. | <a name="PerfCacheDirtyMeasuring-common1"></a>

**To measure the percent of a cache that is dirty for a gateway and all its volumes**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose the **StorageGateway: Gateway Metrics** dimension, and find the gateway that you want to work with.

1. Choose the `CachePercentDirty` metric.

1. For **Time Range**, choose a value.

1. Choose the `Average` statistic.

1. For **Period**, choose a value of 5 minutes to match the default reporting time.

The resulting time-ordered set of data points contains the percentage of the cache that is dirty over the 5 minutes.<a name="PerfCacheDirtyMeasuring-common"></a>

**To measure the percent of the cache that is dirty for a volume**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose the **StorageGateway: Volume Metrics** dimension, and find the volume that you want to work with.

1. Choose the `CachePercentDirty` metric.

1. For **Time Range**, choose a value.

1. Choose the `Average` statistic.

1. For **Period**, choose a value of 5 minutes to match the default reporting time.

The resulting time-ordered set of data points contains the percentage of the cache that is dirty over the 5 minutes.