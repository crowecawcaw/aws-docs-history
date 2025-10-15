# DeleteBucketPolicy

###### Note

This action deletes an Amazon S3 on Outposts bucket policy. To delete an S3 bucket policy,
 see [DeleteBucketPolicy](API_DeleteBucketPolicy.md "API_DeleteBucketPolicy.md") in the *Amazon S3 API Reference*. 

This implementation of the DELETE action uses the policy subresource to delete the
 policy of a specified Amazon S3 on Outposts bucket. If you are using an identity other than the
 root user of the AWS account that owns the bucket, the calling identity must have the
 `s3-outposts:DeleteBucketPolicy` permissions on the specified Outposts bucket
 and belong to the bucket owner's account to use this action. For more information, see
 [Using
 Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in *Amazon S3 User Guide*.

If you don't have `DeleteBucketPolicy` permissions, Amazon S3 returns a `403
 Access Denied` error. If you have the correct permissions, but you're not using an
 identity that belongs to the bucket owner's account, Amazon S3 returns a `405 Method Not
 Allowed` error. 

###### Important

As a security precaution, the root user of the AWS account that owns a bucket can
 always use this action, even if the policy explicitly denies the root user the ability
 to perform this action.

For more information about bucket policies, see [Using Bucket Policies and User
 Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html"). 

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_DeleteBucketPolicy.md#API_control_DeleteBucketPolicy_Examples "API_control_DeleteBucketPolicy.md#API_control_DeleteBucketPolicy_Examples") section.

The following actions are related to `DeleteBucketPolicy`:


* [GetBucketPolicy](API_control_GetBucketPolicy.md "API_control_GetBucketPolicy.md")
* [PutBucketPolicy](API_control_PutBucketPolicy.md "API_control_PutBucketPolicy.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/bucket/`name`/policy HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_DeleteBucketPolicy_RequestSyntax "#API_control_DeleteBucketPolicy_RequestSyntax")**


Specifies the bucket.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_DeleteBucketPolicy_RequestSyntax "#API_control_DeleteBucketPolicy_RequestSyntax")**


The account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample request for deleting a bucket policy for an Amazon S3 on Outposts
 bucket


This example illustrates one usage of DeleteBucketPolicy.



```

            DELETE v20180820/bucket/example-outpost-bucket/policy  HTTP/1.1
            Host: s3-outposts.<Region>.amazonaws.com  
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteBucketPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteBucketPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteBucketPolicy")
