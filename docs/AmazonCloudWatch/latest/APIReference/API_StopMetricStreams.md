# StopMetricStreams

Stops the streaming of metrics for one or more of your metric streams.


## Request Parameters





**Names** 


The array of the names of metric streams to stop streaming.


This is an "all or nothing" operation. If you do not have permission to access all of
 the metric streams that you list here, then none of the streams that you list in the
 operation will stop streaming.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StopMetricStreams")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopMetricStreams "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopMetricStreams")
