# AbortIncompleteMultipartUpload

Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before
 permanently removing all parts of the upload. For more information, see  [Aborting
 Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config") in the
 *Amazon S3 User Guide*.


## Contents





**DaysAfterInitiation** 


Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AbortIncompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AbortIncompleteMultipartUpload")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AbortIncompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AbortIncompleteMultipartUpload")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AbortIncompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AbortIncompleteMultipartUpload")
