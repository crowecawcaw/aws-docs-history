# DeletePublicAccessBlock

###### Note

This operation is not supported for directory buckets.

Removes the `PublicAccessBlock` configuration for an Amazon S3 bucket. To use this operation,
 you must have the `s3:PutBucketPublicAccessBlock` permission. For more information about
 permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

The following operations are related to `DeletePublicAccessBlock`:


* [Using
 Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html")
* [GetPublicAccessBlock](API_GetPublicAccessBlock.md "API_GetPublicAccessBlock.md")
* [PutPublicAccessBlock](API_PutPublicAccessBlock.md "API_PutPublicAccessBlock.md")
* [GetBucketPolicyStatus](API_GetBucketPolicyStatus.md "API_GetBucketPolicyStatus.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?publicAccessBlock HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeletePublicAccessBlock_RequestSyntax "#API_DeletePublicAccessBlock_RequestSyntax")**


The Amazon S3 bucket whose `PublicAccessBlock` configuration you want to delete. 


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeletePublicAccessBlock_RequestSyntax "#API_DeletePublicAccessBlock_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeletePublicAccessBlock")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeletePublicAccessBlock")
