# ReplicaModifications

A filter that you can specify for selection for modifications on replicas. Amazon S3 doesn't replicate
 replica modifications by default. In the latest version of replication configuration (when
 `Filter` is specified), you can specify this element and set the status to
 `Enabled` to replicate modifications on replicas. 

###### Note

 If you don't specify the `Filter` element, Amazon S3 assumes that the replication
 configuration is the earlier version, V1. In the earlier version, this element is not allowed.


## Contents





**Status** 


Specifies whether Amazon S3 replicates modifications on replicas.


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicaModifications "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicaModifications")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicaModifications "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicaModifications")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicaModifications "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicaModifications")
