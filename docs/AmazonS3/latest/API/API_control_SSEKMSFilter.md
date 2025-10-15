# SSEKMSFilter

A filter that returns objects that are encrypted by server-side encryption with AWS KMS (SSE-KMS).


## Contents





**BucketKeyEnabled** 


Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption 
 using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If specified, will filter SSE-KMS encrypted objects by S3 Bucket Key status. 
 For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](../userguide/bucket-key.md "../userguide/bucket-key.md")
 in the *Amazon S3 User Guide*.


Type: Boolean


Required: No




**KmsKeyArn** 


The Amazon Resource Name (ARN) of the customer managed KMS key to use for the filter 
 to return objects that are encrypted by the specified key. For best performance, 
 we recommend using the `KMSKeyArn` filter in conjunction with other object metadata filters, like `MatchAnyPrefix`, `CreatedAfter`, or 
 `MatchAnyStorageClass`.


###### Note

You must provide the full KMS Key ARN. You can't use an alias name or alias ARN. 
 For more information, see [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN") in the *AWS Key Management Service Developer Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `arn:aws[a-zA-Z0-9-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-zA-Z0-9-]+`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SSEKMSFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SSEKMSFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SSEKMSFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SSEKMSFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SSEKMSFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SSEKMSFilter")
