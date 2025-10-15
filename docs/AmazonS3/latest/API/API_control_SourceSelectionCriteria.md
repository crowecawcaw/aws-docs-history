# SourceSelectionCriteria

A container that describes additional filters for identifying the source objects that
 you want to replicate. You can choose to enable or disable the replication of these
 objects.


## Contents





**ReplicaModifications** 


A filter that you can use to specify whether replica modification sync is enabled.
 S3 on Outposts replica modification sync can help you keep object metadata synchronized
 between replicas and source objects. By default, S3 on Outposts replicates metadata from the
 source objects to the replicas only. When replica modification sync is enabled,
 S3 on Outposts replicates metadata changes made to the replica copies back to the source
 object, making the replication bidirectional.


To replicate object metadata modifications on replicas, you can specify this element and
 set the `Status` of this element to `Enabled`.


###### Note

You must enable replica modification sync on the source and destination buckets to
 replicate replica metadata changes between the source and the replicas.


Type: [ReplicaModifications](API_control_ReplicaModifications.md "API_control_ReplicaModifications.md") data type


Required: No




**SseKmsEncryptedObjects** 


A filter that you can use to select Amazon S3 objects that are encrypted with server-side
 encryption by using AWS Key Management Service (AWS KMS) keys. If you include
 `SourceSelectionCriteria` in the replication configuration, this element is
 required. 


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: [SseKmsEncryptedObjects](API_control_SseKmsEncryptedObjects.md "API_control_SseKmsEncryptedObjects.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SourceSelectionCriteria "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SourceSelectionCriteria")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SourceSelectionCriteria "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SourceSelectionCriteria")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SourceSelectionCriteria "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SourceSelectionCriteria")
