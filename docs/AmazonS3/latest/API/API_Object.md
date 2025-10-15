# Object

An object consists of data and its descriptive metadata.


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


The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object,
 not its metadata. The ETag may or may not be an MD5 digest of the object data. Whether or not it is
 depends on how the object was created and how it is encrypted as described below:



* Objects created by the PUT Object, POST Object, or Copy operation, or through the AWS
 Management Console, and are encrypted by SSE-S3 or plaintext, have ETags that are an MD5 digest of
 their object data.
* Objects created by the PUT Object, POST Object, or Copy operation, or through the AWS
 Management Console, and are encrypted by SSE-C or SSE-KMS, have ETags that are not an MD5 digest of
 their object data.
* If an object is created by either the Multipart Upload or Part Copy operation, the ETag is not
 an MD5 digest, regardless of the method of encryption. If an object is larger than 16 MB, the AWS
 Management Console will upload or copy that object as a Multipart Upload, and therefore the ETag
 will not be an MD5 digest.

###### Note


**Directory buckets** - MD5 is not supported by directory buckets.


Type: String


Required: No




**Key** 


The name that you assign to an object. You use the object key to retrieve the object.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**LastModified** 


Creation date of the object.


Type: Timestamp


Required: No




**Owner** 


The owner of the object


###### Note


**Directory buckets** - The bucket owner is returned as the
 object owner.


Type: [Owner](API_Owner.md "API_Owner.md") data type


Required: No




**RestoreStatus** 


Specifies the restoration status of an object. Objects in certain storage classes must be restored
 before they can be retrieved. For more information about these storage classes and how to work with
 archived objects, see [Working with archived objects](../userguide/archived-objects.md "../userguide/archived-objects.md") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets. Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.


Type: [RestoreStatus](API_RestoreStatus.md "API_RestoreStatus.md") data type


Required: No




**Size** 


Size in bytes of the object


Type: Long


Required: No




**StorageClass** 


The class of storage used to store the object.


###### Note


**Directory buckets** -
 Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.


Type: String


Valid Values: `STANDARD | REDUCED_REDUNDANCY | GLACIER | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Object "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Object")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Object "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Object")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Object "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Object")
