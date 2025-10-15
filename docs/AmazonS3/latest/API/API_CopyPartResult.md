# CopyPartResult

Container for all response elements.


## Contents





**ChecksumCRC32** 


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 32-bit `CRC32` checksum
 of the part. For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumCRC32C** 


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 32-bit `CRC32C` checksum
 of the part. For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumCRC64NVME** 


The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if
 the multipart upload request was created with the `CRC64NVME` checksum algorithm to the
 uploaded object). For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumSHA1** 


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 160-bit `SHA1` checksum
 of the part. For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String


Required: No




**ChecksumSHA256** 


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 256-bit `SHA256` checksum
 of the part. For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String


Required: No




**ETag** 


Entity tag of the object.


Type: String


Required: No




**LastModified** 


Date and time at which the object was uploaded.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CopyPartResult "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CopyPartResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CopyPartResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CopyPartResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CopyPartResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CopyPartResult")
