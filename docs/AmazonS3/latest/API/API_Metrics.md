# Metrics

 A container specifying replication metrics-related settings enabling replication metrics and
 events.


## Contents





**Status** 


 Specifies whether the replication metrics are enabled. 


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




**EventThreshold** 


 A container specifying the time threshold for emitting the
 `s3:Replication:OperationMissedThreshold` event. 


Type: [ReplicationTimeValue](API_ReplicationTimeValue.md "API_ReplicationTimeValue.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Metrics "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Metrics")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Metrics "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Metrics")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Metrics "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Metrics")
