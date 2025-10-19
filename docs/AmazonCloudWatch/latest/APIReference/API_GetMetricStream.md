# GetMetricStream

Returns information about the metric stream that you specify.


## Request Parameters





**Name** 


The name of the metric stream to retrieve information about.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




## Response Elements


The following elements are returned by the service.





**Arn** 


The ARN of the metric stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**CreationDate** 


The date that the metric stream was created.


Type: Timestamp




**ExcludeFilters** 


If this array of metric namespaces is present, then these namespaces are the only
 metric namespaces that are not streamed by this metric stream. In this case, all other
 metric namespaces in the account are streamed by this metric stream.


Type: Array of [MetricStreamFilter](API_MetricStreamFilter.md "API_MetricStreamFilter.md") objects




**FirehoseArn** 


The ARN of the Amazon Kinesis Data Firehose delivery stream that is used by this
 metric stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**IncludeFilters** 


If this array of metric namespaces is present, then these namespaces are the only
 metric namespaces that are streamed by this metric stream.


Type: Array of [MetricStreamFilter](API_MetricStreamFilter.md "API_MetricStreamFilter.md") objects




**IncludeLinkedAccountsMetrics** 


If this is `true` and this metric stream is in a monitoring account, then
 the stream includes metrics from source accounts that the monitoring account is linked
 to.


Type: Boolean




**LastUpdateDate** 


The date of the most recent update to the metric stream's configuration.


Type: Timestamp




**Name** 


The name of the metric stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.




**OutputFormat** 


The output format for the stream. Valid values are `json`,
 `opentelemetry1.0`, and `opentelemetry0.7`. For more
 information about metric stream output formats, see [Metric streams output formats](../monitoring/CloudWatch-metric-streams-formats.md "../monitoring/CloudWatch-metric-streams-formats.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Valid Values: `json | opentelemetry0.7 | opentelemetry1.0`





**RoleArn** 


The ARN of the IAM role that is used by this metric stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**State** 


The state of the metric stream. The possible values are `running` and
 `stopped`.


Type: String




**StatisticsConfigurations** 


Each entry in this array displays information about one or more metrics that include
 additional statistics in the metric stream. For more information about the additional
 statistics, see [CloudWatch statistics definitions](../monitoring/Statistics-definitions.md "../monitoring/Statistics-definitions.md"). 


Type: Array of [MetricStreamStatisticsConfiguration](API_MetricStreamStatisticsConfiguration.md "API_MetricStreamStatisticsConfiguration.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterCombination** 


Parameters were used together that cannot be used together.





**message** 





HTTP Status Code: 400




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




**ResourceNotFoundException** 


The named resource does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricStream")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricStream "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricStream")
