# AnomalyDetectorConfiguration

The configuration specifies details about how the anomaly detection model is to be
 trained, including time ranges to exclude from use for training the model and the time
 zone to use for the metric.


## Contents





**ExcludedTimeRanges** 


An array of time ranges to exclude from use when the anomaly detection model is
 trained. Use this to make sure that events that could cause unusual values for the
 metric, such as deployments, aren't used when CloudWatch creates the model.


Type: Array of [Range](API_Range.md "API_Range.md") objects


Required: No




**MetricTimezone** 


The time zone to use for the metric. This is useful to enable the model to
 automatically account for daylight savings time changes if the metric is sensitive to
 such time changes.


To specify a time zone, use the name of the time zone as specified in the standard
 tz database. For more information, see [tz database](https://en.wikipedia.org/wiki/Tz_database "https://en.wikipedia.org/wiki/Tz_database").


Type: String


Length Constraints: Maximum length of 50.


Pattern: `.*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AnomalyDetectorConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AnomalyDetectorConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AnomalyDetectorConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AnomalyDetectorConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AnomalyDetectorConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AnomalyDetectorConfiguration")
