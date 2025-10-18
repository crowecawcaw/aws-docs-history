# MetricAlarm

The details about a metric alarm.


## Contents





**ActionsEnabled** 


Indicates whether actions should be executed during any changes to the alarm
 state.


Type: Boolean


Required: No




**AlarmActions** 


The actions to execute when this alarm transitions to the `ALARM` state
 from any other state. Each action is specified as an Amazon Resource Name
 (ARN).


Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmArn** 


The Amazon Resource Name (ARN) of the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1600.


Required: No




**AlarmConfigurationUpdatedTimestamp** 


The time stamp of the last update to the alarm configuration.


Type: Timestamp


Required: No




**AlarmDescription** 


The description of the alarm.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




**AlarmName** 


The name of the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**ComparisonOperator** 


The arithmetic operation to use when comparing the specified statistic and
 threshold. The specified statistic value is used as the first operand.


Type: String


Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold | LessThanLowerOrGreaterThanUpperThreshold | LessThanLowerThreshold | GreaterThanUpperThreshold`



Required: No




**DatapointsToAlarm** 


The number of data points that must be breaching to trigger the alarm.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**Dimensions** 


The dimensions for the metric associated with the alarm.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**EvaluateLowSampleCountPercentile** 


Used only for alarms based on percentiles. If `ignore`, the alarm state
 does not change during periods with too few data points to be statistically significant.
 If `evaluate` or this parameter is not used, the alarm is always evaluated
 and possibly changes state no matter how many data points are available.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**EvaluationPeriods** 


The number of periods over which data is compared to the specified
 threshold.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**EvaluationState** 


If the value of this field is `PARTIAL_DATA`, the alarm is being evaluated
 based on only partial data. This happens if the query used for the alarm returns more
 than 10,000 metrics. For more information, see [Create
 alarms on Metrics Insights queries](../monitoring/Create_Metrics_Insights_Alarm.md "../monitoring/Create_Metrics_Insights_Alarm.md").


Type: String


Valid Values: `PARTIAL_DATA`



Required: No




**ExtendedStatistic** 


The percentile statistic for the metric associated with the alarm. Specify a value
 between p0.0 and p100.


Type: String


Required: No




**InsufficientDataActions** 


The actions to execute when this alarm transitions to the
 `INSUFFICIENT_DATA` state from any other state. Each action is specified
 as an Amazon Resource Name (ARN).


Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**MetricName** 


The name of the metric associated with the alarm, if this is an alarm based on a
 single metric.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Metrics** 


An array of MetricDataQuery structures, used in an alarm based on a metric math
 expression. Each structure either retrieves a metric or performs a math expression. One
 item in the Metrics array is the math expression that the alarm watches. This expression
 by designated by having `ReturnData` set to true.


Type: Array of [MetricDataQuery](API_MetricDataQuery.md "API_MetricDataQuery.md") objects


Required: No




**Namespace** 


The namespace of the metric associated with the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: No




**OKActions** 


The actions to execute when this alarm transitions to the `OK` state
 from any other state. Each action is specified as an Amazon Resource Name
 (ARN).


Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**Period** 


The period, in seconds, over which the statistic is applied.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**StateReason** 


An explanation for the alarm state, in text format.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1023.


Required: No




**StateReasonData** 


An explanation for the alarm state, in JSON format.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 4000.


Required: No




**StateTransitionedTimestamp** 


The date and time that the alarm's `StateValue` most recently
 changed.


Type: Timestamp


Required: No




**StateUpdatedTimestamp** 


The time stamp of the last update to the value of either the
 `StateValue` or `EvaluationState` parameters.


Type: Timestamp


Required: No




**StateValue** 


The state value for the alarm.


Type: String


Valid Values: `OK | ALARM | INSUFFICIENT_DATA`



Required: No




**Statistic** 


The statistic for the metric associated with the alarm, other than percentile. For
 percentile statistics, use `ExtendedStatistic`.


Type: String


Valid Values: `SampleCount | Average | Sum | Minimum | Maximum`



Required: No




**Threshold** 


The value to compare with the specified statistic.


Type: Double


Required: No




**ThresholdMetricId** 


In an alarm based on an anomaly detection model, this is the ID of the
 `ANOMALY_DETECTION_BAND` function used as the threshold for the
 alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**TreatMissingData** 


Sets how this alarm is to handle missing data points. The valid values are
 `breaching`, `notBreaching`, `ignore`, and
 `missing`. For more information, see [Configuring how CloudWatch alarms treat missing data](../monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data").


If this parameter is omitted, the default behavior of `missing` is
 used.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Unit** 


The unit of the metric associated with the alarm.


Type: String


Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricAlarm "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricAlarm")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricAlarm "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricAlarm")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricAlarm "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricAlarm")
