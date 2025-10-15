# Bucket

 In terms of implementation, a Bucket is a resource. 


## Contents





**BucketArn** 


The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify AWS resources across all
 of AWS.


###### Note

This parameter is only supported for S3 directory buckets. For more information, see [Using tags with
 directory buckets](../userguide/directory-buckets-tagging.md "../userguide/directory-buckets-tagging.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:(s3|s3express):.*`



Required: No




**BucketRegion** 



`BucketRegion` indicates the AWS region where the bucket is located. If the request
 contains at least one valid parameter, it is included in the response.


Type: String


Required: No




**CreationDate** 


Date the bucket was created. This date can change when making changes to your bucket, such as
 editing its bucket policy.


Type: Timestamp


Required: No




**Name** 


The name of the bucket.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Bucket "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Bucket")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Bucket "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Bucket")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Bucket "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Bucket")
