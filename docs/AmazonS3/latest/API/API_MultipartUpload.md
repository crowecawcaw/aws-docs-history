# MultipartUpload

Container for the `MultipartUpload` for the Amazon S3 object.


## Contents





**ChecksumAlgorithm** 


The algorithm that was used to create a checksum of the object.


Type: String


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`



Required: No




**ChecksumType** 


The checksum type that is used to calculate the object’s checksum value. For more information, see
 [Checking
 object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Valid Values: `COMPOSITE | FULL_OBJECT`



Required: No




**Initiated** 


Date and time at which the multipart upload was initiated.


Type: Timestamp


Required: No




**Initiator** 


Identifies who initiated the multipart upload.


Type: [Initiator](API_Initiator.md "API_Initiator.md") data type


Required: No




**Key** 


Key of the object for which the multipart upload was initiated.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**Owner** 


Specifies the owner of the object that is part of the multipart upload. 


###### Note


**Directory buckets** - The bucket owner is returned as the
 object owner for all the objects.


Type: [Owner](API_Owner.md "API_Owner.md") data type


Required: No




**StorageClass** 


The class of storage used to store the object.


###### Note


**Directory buckets** -
 Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.


Type: String


Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS`



Required: No




**UploadId** 


Upload ID that identifies the multipart upload.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MultipartUpload "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MultipartUpload")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MultipartUpload")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MultipartUpload "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MultipartUpload")
