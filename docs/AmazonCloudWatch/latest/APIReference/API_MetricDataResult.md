# MetricDataResult

A `GetMetricData` call returns an array of `MetricDataResult`
 structures. Each of these structures includes the data points for that metric, along
 with the timestamps of those data points and other identifying information.


## Contents





**Id** 


The short name you specified to represent this metric.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Label** 


The human-readable label associated with the data.


Type: String


Required: No




**Messages** 


A list of messages with additional information about the data returned.


Type: Array of [MessageData](API_MessageData.md "API_MessageData.md") objects


Required: No




**StatusCode** 


The status of the returned data. `Complete` indicates that all data points
 in the requested time range were returned. `PartialData` means that an
 incomplete set of data points were returned. You can use the `NextToken`
 value that was returned and repeat your request to get more data points.
 `NextToken` is not returned if you are performing a math expression.
 `InternalError` indicates that an error occurred. Retry your request
 using `NextToken`, if present.


Type: String


Valid Values: `Complete | InternalError | PartialData | Forbidden`



Required: No




**Timestamps** 


The timestamps for the data points, formatted in Unix timestamp format. The number of
 timestamps always matches the number of values and the value for Timestamps[x] is
 Values[x].


Type: Array of timestamps


Required: No




**Values** 


The data points for the metric corresponding to `Timestamps`. The number of
 values always matches the number of timestamps and the timestamp for Values[x] is
 Timestamps[x].


Type: Array of doubles


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricDataResult "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricDataResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricDataResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricDataResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricDataResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricDataResult")
