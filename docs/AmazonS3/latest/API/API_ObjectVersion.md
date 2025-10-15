# ObjectVersion

The version of an object.


## Contents





**ChecksumAlgorithm** 


The algorithm that was used to create a checksum of the object.


Type: Array of strings


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`



Required: No




**ChecksumType** 


The checksum type that is used to calculate the object’s checksum value. For more information, see
 [Checking
 object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Valid Values: `COMPOSITE | FULL_OBJECT`



Required: No




**ETag** 


The entity tag is an MD5 hash of that version of the object.


Type: String


Required: No




**IsLatest** 


Specifies whether the object is (true) or is not (false) the latest version of an object.


Type: Boolean


Required: No




**Key** 


The object key.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**LastModified** 


Date and time when the object was last modified.


Type: Timestamp


Required: No




**Owner** 


Specifies the owner of the object.


Type: [Owner](API_Owner.md "API_Owner.md") data type


Required: No




**RestoreStatus** 


Specifies the restoration status of an object. Objects in certain storage classes must be restored
 before they can be retrieved. For more information about these storage classes and how to work with
 archived objects, see [Working with archived objects](../userguide/archived-objects.md "../userguide/archived-objects.md") in the *Amazon S3 User Guide*.


Type: [RestoreStatus](API_RestoreStatus.md "API_RestoreStatus.md") data type


Required: No




**Size** 


Size in bytes of the object.


Type: Long


Required: No




**StorageClass** 


The class of storage used to store the object.


Type: String


Valid Values: `STANDARD`



Required: No




**VersionId** 


Version ID of an object.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectVersion "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectVersion")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectVersion "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectVersion")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectVersion "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectVersion")
