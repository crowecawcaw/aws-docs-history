# GetBucketPolicy

###### Note

This action gets a bucket policy for an Amazon S3 on Outposts bucket. To get a policy for
 an S3 bucket, see [GetBucketPolicy](API_GetBucketPolicy.md "API_GetBucketPolicy.md") in the
 *Amazon S3 API Reference*. 

Returns the policy of a specified Outposts bucket. For more information, see [Using
 Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.

If you are using an identity other than the root user of the AWS account that owns the
 bucket, the calling identity must have the `GetBucketPolicy` permissions on the
 specified bucket and belong to the bucket owner's account in order to use this
 action.

Only users from Outposts bucket owner account with the right permissions can perform
 actions on an Outposts bucket. If you don't have `s3-outposts:GetBucketPolicy`
 permissions or you're not using an identity that belongs to the bucket owner's account,
 Amazon S3 returns a `403 Access Denied` error.

###### Important

As a security precaution, the root user of the AWS account that owns a bucket can
 always use this action, even if the policy explicitly denies the root user the ability
 to perform this action.

For more information about bucket policies, see [Using Bucket Policies and User
 Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html").

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_GetBucketPolicy.md#API_control_GetBucketPolicy_Examples "API_control_GetBucketPolicy.md#API_control_GetBucketPolicy_Examples") section.

The following actions are related to `GetBucketPolicy`:


* [GetObject](API_GetObject.md "API_GetObject.md")
* [PutBucketPolicy](API_control_PutBucketPolicy.md "API_control_PutBucketPolicy.md")
* [DeleteBucketPolicy](API_control_DeleteBucketPolicy.md "API_control_DeleteBucketPolicy.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/bucket/`name`/policy HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetBucketPolicy_RequestSyntax "#API_control_GetBucketPolicy_RequestSyntax")**


Specifies the bucket.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_GetBucketPolicy_RequestSyntax "#API_control_GetBucketPolicy_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetBucketPolicyResult](#AmazonS3-control_GetBucketPolicy-response-GetBucketPolicyResult "#AmazonS3-control_GetBucketPolicy-response-GetBucketPolicyResult")>
   <[Policy](#AmazonS3-control_GetBucketPolicy-response-Policy "#AmazonS3-control_GetBucketPolicy-response-Policy")>***string***</[Policy](#AmazonS3-control_GetBucketPolicy-response-Policy "#AmazonS3-control_GetBucketPolicy-response-Policy")>
</[GetBucketPolicyResult](#AmazonS3-control_GetBucketPolicy-response-GetBucketPolicyResult "#AmazonS3-control_GetBucketPolicy-response-GetBucketPolicyResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetBucketPolicyResult](#API_control_GetBucketPolicy_ResponseSyntax "#API_control_GetBucketPolicy_ResponseSyntax")**


Root level tag for the GetBucketPolicyResult parameters.


Required: Yes




**[Policy](#API_control_GetBucketPolicy_ResponseSyntax "#API_control_GetBucketPolicy_ResponseSyntax")**


The policy of the Outposts bucket.


Type: String




## Examples


### Sample GetBucketPolicy request for an Amazon S3 on Outposts bucket


The following request gets the policy of the specified Outposts bucket
 `example-outpost-bucket`.



```

           GET /v20180820/bucket/example-outpost-bucket/policy HTTP/1.1
           Host: s3-outposts.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2009 22:32:00 GMT
           Authorization: authorization string
           x-amz-account-id: example-account-id
           x-amz-outpost-id: op-01ac5d28a6a232904
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketPolicy")
