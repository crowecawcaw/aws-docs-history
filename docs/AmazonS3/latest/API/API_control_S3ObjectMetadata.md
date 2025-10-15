# S3ObjectMetadata


## Contents





**CacheControl** 



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ContentDisposition** 



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ContentEncoding** 



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ContentLanguage** 



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ContentLength** 



*This member has been deprecated.*




Type: Long


Valid Range: Minimum value of 0.


Required: No




**ContentMD5** 



*This member has been deprecated.*




Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ContentType** 



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**HttpExpiresDate** 



Type: Timestamp


Required: No




**RequesterCharged** 



*This member has been deprecated.*




Type: Boolean


Required: No




**SSEAlgorithm** 


The server-side encryption algorithm used when storing objects in Amazon S3.



**Directory buckets**  -
 For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`KMS`). For more
 information, see [Protecting data with server-side encryption](../userguide/s3-express-serv-side-encryption.md "../userguide/s3-express-serv-side-encryption.md") in the *Amazon S3 User Guide*.
 For [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops"), see [S3CopyObjectOperation](API_control_S3CopyObjectOperation.md "API_control_S3CopyObjectOperation.md").


Type: String


Valid Values: `AES256 | KMS`



Required: No




**UserMetadata** 



Type: String to string map


Map Entries: Maximum number of 8192 items.


Key Length Constraints: Minimum length of 1. Maximum length of 1024.


Value Length Constraints: Maximum length of 1024.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ObjectMetadata "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ObjectMetadata")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ObjectMetadata "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ObjectMetadata")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ObjectMetadata "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ObjectMetadata")
