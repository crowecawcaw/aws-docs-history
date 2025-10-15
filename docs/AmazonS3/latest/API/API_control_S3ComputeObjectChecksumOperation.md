# S3ComputeObjectChecksumOperation

Directs the specified job to invoke the `ComputeObjectChecksum` operation on every object listed in the job's manifest.


## Contents





**ChecksumAlgorithm** 


Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more
 information, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Valid Values: `CRC32 | CRC32C | CRC64NVME | MD5 | SHA1 | SHA256`



Required: No




**ChecksumType** 


Indicates the checksum type that you want Amazon S3 to use to calculate the object’s checksum
 value. For more information, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Valid Values: `FULL_OBJECT | COMPOSITE`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ComputeObjectChecksumOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ComputeObjectChecksumOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ComputeObjectChecksumOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ComputeObjectChecksumOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ComputeObjectChecksumOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ComputeObjectChecksumOperation")
