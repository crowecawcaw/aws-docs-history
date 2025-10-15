# Destination

Specifies information about the replication destination bucket and its settings for an
 S3 on Outposts replication configuration.


## Contents





**Bucket** 


The Amazon Resource Name (ARN) of the access point for the destination bucket where you want
 S3 on Outposts to store the replication results.


Type: String


Required: Yes




**AccessControlTranslation** 


Specify this property only in a cross-account scenario (where the source and destination
 bucket owners are not the same), and you want to change replica ownership to the
 AWS account that owns the destination bucket. If this property is not specified in the
 replication configuration, the replicas are owned by same AWS account that owns the
 source object.


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: [AccessControlTranslation](API_control_AccessControlTranslation.md "API_control_AccessControlTranslation.md") data type


Required: No




**Account** 


The destination bucket owner's account ID. 


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




**EncryptionConfiguration** 


A container that provides information about encryption. If
 `SourceSelectionCriteria` is specified, you must specify this element.


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: [EncryptionConfiguration](API_control_EncryptionConfiguration.md "API_control_EncryptionConfiguration.md") data type


Required: No




**Metrics** 


 A container that specifies replication metrics-related settings. 


Type: [Metrics](API_control_Metrics.md "API_control_Metrics.md") data type


Required: No




**ReplicationTime** 


A container that specifies S3 Replication Time Control (S3 RTC) settings, including whether S3 RTC is enabled
 and the time when all objects and operations on objects must be replicated. Must be
 specified together with a `Metrics` block. 


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: [ReplicationTime](API_control_ReplicationTime.md "API_control_ReplicationTime.md") data type


Required: No




**StorageClass** 


 The storage class to use when replicating objects. All objects stored on S3 on Outposts
 are stored in the `OUTPOSTS` storage class. S3 on Outposts uses the
 `OUTPOSTS` storage class to create the object replicas. 


###### Note

Values other than `OUTPOSTS` aren't supported by Amazon S3 on Outposts. 


Type: String


Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Destination "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Destination")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Destination "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Destination")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Destination "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Destination")
