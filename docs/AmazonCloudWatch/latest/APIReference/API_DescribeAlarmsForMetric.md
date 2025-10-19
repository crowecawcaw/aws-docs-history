# DescribeAlarmsForMetric

Retrieves the alarms for the specified metric. To filter the results, specify a
 statistic, period, or unit.

This operation retrieves only standard alarms that are based on the specified
 metric. It does not return alarms based on math expressions that use the specified
 metric, or composite alarms that use the specified metric.


## Request Parameters





**Dimensions** 


The dimensions associated with the metric. If the metric has any associated
 dimensions, you must specify them in order for the call to succeed.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**ExtendedStatistic** 


The percentile statistic for the metric. Specify a value between p0.0 and
 p100.


Type: String


Required: No




**MetricName** 


The name of the metric.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




**Namespace** 


The namespace of the metric.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: Yes




**Period** 


The period, in seconds, over which the statistic is applied.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**Statistic** 


The statistic for the metric, other than percentiles. For percentile statistics,
 use `ExtendedStatistics`.


Type: String


Valid Values: `SampleCount | Average | Sum | Minimum | Maximum`



Required: No




**Unit** 


The unit for the metric.


Type: String


Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`



Required: No




## Response Elements


The following element is returned by the service.





**MetricAlarms** 


The information for each alarm with the specified metric.


Type: Array of [MetricAlarm](API_MetricAlarm.md "API_MetricAlarm.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmsForMetric")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmsForMetric "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmsForMetric")
