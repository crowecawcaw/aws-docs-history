# MetricDatum

Encapsulates the information sent to either create a metric or add new values to be
 aggregated into an existing metric.


## Contents





**MetricName** 


The name of the metric.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




**Counts** 


Array of numbers that is used along with the `Values` array. Each number in
 the `Count` array is the number of times the corresponding value in the
 `Values` array occurred during the period. 


If you omit the `Counts` array, the default of 1 is used as the value for
 each count. If you include a `Counts` array, it must include the same amount
 of values as the `Values` array.


Type: Array of doubles


Required: No




**Dimensions** 


The dimensions associated with the metric. 


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**StatisticValues** 


The statistical values for the metric.


Type: [StatisticSet](API_StatisticSet.md "API_StatisticSet.md") object


Required: No




**StorageResolution** 


Valid values are 1 and 60. Setting this to 1 specifies this metric as a
 high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution
 down to one second. Setting this to 60 specifies this metric as a regular-resolution
 metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is
 available only for custom metrics. For more information about high-resolution metrics,
 see [High-Resolution Metrics](../monitoring/publishingMetrics.md#high-resolution-metrics "../monitoring/publishingMetrics.md#high-resolution-metrics") in the *Amazon CloudWatch User
 Guide*. 


This field is optional, if you do not specify it the default of 60 is
 used.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**Timestamp** 


The time the metric data was received, expressed as the number of milliseconds
 since Jan 1, 1970 00:00:00 UTC.


Type: Timestamp


Required: No




**Unit** 


When you are using a `Put` operation, this defines what unit you want to
 use when storing the metric.


In a `Get` operation, this displays the unit that is used for the
 metric.


Type: String


Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`



Required: No




**Value** 


The value for the metric.


Although the parameter accepts numbers of type Double, CloudWatch rejects values
 that are either too small or too large. Values must be in the range of -2^360 to 2^360.
 In addition, special values (for example, NaN, +Infinity, -Infinity) are not
 supported.


Type: Double


Required: No




**Values** 


Array of numbers representing the values for the metric during the period. Each unique
 value is listed just once in this array, and the corresponding number in the
 `Counts` array specifies the number of times that value occurred during
 the period. You can include up to 150 unique values in each `PutMetricData`
 action that specifies a `Values` array.


Although the `Values` array accepts numbers of type `Double`,
 CloudWatch rejects values that are either too small or too large. Values must be in the
 range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity,
 -Infinity) are not supported.


Type: Array of doubles


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricDatum "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricDatum")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricDatum "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricDatum")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricDatum "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricDatum")
