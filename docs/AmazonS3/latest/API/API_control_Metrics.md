# Metrics

A container that specifies replication metrics-related settings.


## Contents





**Status** 


Specifies whether replication metrics are enabled. 


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




**EventThreshold** 


A container that specifies the time threshold for emitting the
 `s3:Replication:OperationMissedThreshold` event. 


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: [ReplicationTimeValue](API_control_ReplicationTimeValue.md "API_control_ReplicationTimeValue.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Metrics "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Metrics")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Metrics "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Metrics")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Metrics "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Metrics")
