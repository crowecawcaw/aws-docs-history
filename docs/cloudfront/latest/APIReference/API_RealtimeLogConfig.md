# RealtimeLogConfig

A real-time log configuration.


## Contents





**ARN** 


The Amazon Resource Name (ARN) of this real-time log configuration.


Type: String


Required: Yes




**EndPoints** 


Contains information about the Amazon Kinesis data stream where you are sending real-time
 log data for this real-time log configuration.


Type: Array of [EndPoint](API_EndPoint.md "API_EndPoint.md") objects


Required: Yes




**Fields** 


A list of fields that are included in each real-time log record. In an API response,
 the fields are provided in the same order in which they are sent to the Amazon Kinesis data
 stream.


For more information about fields, see [Real-time log configuration fields](../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md#understand-real-time-log-config-fields "../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md#understand-real-time-log-config-fields") in the
 *Amazon CloudFront Developer Guide*.


Type: Array of strings


Required: Yes




**Name** 


The unique name of this real-time log configuration.


Type: String


Required: Yes




**SamplingRate** 


The sampling rate for this real-time log configuration. The sampling rate determines
 the percentage of viewer requests that are represented in the real-time log data. The
 sampling rate is an integer between 1 and 100, inclusive.


Type: Long


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/RealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/RealtimeLogConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/RealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/RealtimeLogConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/RealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/RealtimeLogConfig")
