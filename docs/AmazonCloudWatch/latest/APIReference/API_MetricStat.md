# MetricStat

This structure defines the metric to be returned, along with the statistics, period,
 and units.


## Contents





**Metric** 


The metric to return, including the metric name, namespace, and dimensions.


Type: [Metric](API_Metric.md "API_Metric.md") object


Required: Yes




**Period** 


The granularity, in seconds, of the returned data points. For metrics with regular
 resolution, a period can be as short as one minute (60 seconds) and must be a multiple
 of 60. For high-resolution metrics that are collected at intervals of less than one
 minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution
 metrics are those metrics stored by a `PutMetricData` call that includes a
 `StorageResolution` of 1 second.


If the `StartTime` parameter specifies a time stamp that is greater than
 3 hours ago, you must specify the period as follows or no data points in that time range
 is returned:



* Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds
 (1 minute).
* Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5
 minutes).
* Start time greater than 63 days ago - Use a multiple of 3600 seconds (1
 hour).

Type: Integer


Valid Range: Minimum value of 1.


Required: Yes




**Stat** 


The statistic to return. It can include any CloudWatch statistic or extended
 statistic.


Type: String


Required: Yes




**Unit** 


When you are using a `Put` operation, this defines what unit you want to
 use when storing the metric.


In a `Get` operation, if you omit `Unit` then all data that
 was collected with any unit is returned, along with the corresponding units that were
 specified when the data was reported to CloudWatch. If you specify a unit, the operation
 returns only data that was collected with that unit specified. If you specify a unit
 that does not match the data collected, the results of the operation are null.
 CloudWatch does not perform unit conversions.


Type: String


Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStat "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStat")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStat "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStat")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStat "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStat")
