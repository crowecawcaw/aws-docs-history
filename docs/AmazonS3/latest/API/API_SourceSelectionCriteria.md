# SourceSelectionCriteria

A container that describes additional filters for identifying the source objects that you want to
 replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3
 supports only the filter that you can specify for objects created with server-side encryption using a
 customer managed key stored in AWS Key Management Service (SSE-KMS).


## Contents





**ReplicaModifications** 


A filter that you can specify for selections for modifications on replicas. Amazon S3 doesn't replicate
 replica modifications by default. In the latest version of replication configuration (when
 `Filter` is specified), you can specify this element and set the status to
 `Enabled` to replicate modifications on replicas. 


###### Note

 If you don't specify the `Filter` element, Amazon S3 assumes that the replication
 configuration is the earlier version, V1. In the earlier version, this element is not allowed


Type: [ReplicaModifications](API_ReplicaModifications.md "API_ReplicaModifications.md") data type


Required: No




**SseKmsEncryptedObjects** 


 A container for filter information for the selection of Amazon S3 objects encrypted with AWS KMS. If
 you include `SourceSelectionCriteria` in the replication configuration, this element is
 required. 


Type: [SseKmsEncryptedObjects](API_SseKmsEncryptedObjects.md "API_SseKmsEncryptedObjects.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SourceSelectionCriteria "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SourceSelectionCriteria")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SourceSelectionCriteria "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SourceSelectionCriteria")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SourceSelectionCriteria "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SourceSelectionCriteria")
