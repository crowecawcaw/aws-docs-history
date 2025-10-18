# MetricStreamEntry

This structure contains the configuration information about one metric stream.


## Contents





**Arn** 


The ARN of the metric stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**CreationDate** 


The date that the metric stream was originally created.


Type: Timestamp


Required: No




**FirehoseArn** 


The ARN of the Kinesis Firehose devlivery stream that is used for this metric
 stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**LastUpdateDate** 


The date that the configuration of this metric stream was most recently
 updated.


Type: Timestamp


Required: No




**Name** 


The name of the metric stream.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**OutputFormat** 


The output format of this metric stream. Valid values are `json`,
 `opentelemetry1.0`, and `opentelemetry0.7`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Valid Values: `json | opentelemetry0.7 | opentelemetry1.0`



Required: No




**State** 


The current state of this stream. Valid values are `running` and
 `stopped`.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStreamEntry "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStreamEntry")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStreamEntry "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStreamEntry")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStreamEntry "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStreamEntry")
