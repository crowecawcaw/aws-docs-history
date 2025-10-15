# Part

Container for elements related to a part.


## Contents





**ChecksumCRC32** 


The Base64 encoded, 32-bit `CRC32` checksum of the part. This checksum is present if the
 object was uploaded with the `CRC32` checksum algorithm. For more information, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumCRC32C** 


The Base64 encoded, 32-bit `CRC32C` checksum of the part. This checksum is present if the
 object was uploaded with the `CRC32C` checksum algorithm. For more information, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumCRC64NVME** 


The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if
 the multipart upload request was created with the `CRC64NVME` checksum algorithm, or if the
 object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME`, to
 the uploaded object). For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumSHA1** 


The Base64 encoded, 160-bit `SHA1` checksum of the part. This checksum is present if the
 object was uploaded with the `SHA1` checksum algorithm. For more information, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumSHA256** 


The Base64 encoded, 256-bit `SHA256` checksum of the part. This checksum is present if
 the object was uploaded with the `SHA256` checksum algorithm. For more information, see
 [Checking
 object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Required: No




**ETag** 


Entity tag returned when the part was uploaded.


Type: String


Required: No




**LastModified** 


Date and time at which the part was uploaded.


Type: Timestamp


Required: No




**PartNumber** 


Part number identifying the part. This is a positive integer between 1 and 10,000.


Type: Integer


Required: No




**Size** 


Size in bytes of the uploaded part data.


Type: Long


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Part "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Part")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Part "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Part")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Part "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Part")
