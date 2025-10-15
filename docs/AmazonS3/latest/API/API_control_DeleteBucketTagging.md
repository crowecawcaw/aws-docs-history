# DeleteBucketTagging

###### Note

This action deletes an Amazon S3 on Outposts bucket's tags. To delete an S3 bucket tags,
 see [DeleteBucketTagging](API_DeleteBucketTagging.md "API_DeleteBucketTagging.md") in the *Amazon S3 API Reference*. 

Deletes the tags from the Outposts bucket. For more information, see [Using
 Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in *Amazon S3 User Guide*.

To use this action, you must have permission to perform the
 `PutBucketTagging` action. By default, the bucket owner has this permission
 and can grant this permission to others. 

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_DeleteBucketTagging.md#API_control_DeleteBucketTagging_Examples "API_control_DeleteBucketTagging.md#API_control_DeleteBucketTagging_Examples") section.

The following actions are related to `DeleteBucketTagging`:


* [GetBucketTagging](API_control_GetBucketTagging.md "API_control_GetBucketTagging.md")
* [PutBucketTagging](API_control_PutBucketTagging.md "API_control_PutBucketTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/bucket/`name`/tagging HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_DeleteBucketTagging_RequestSyntax "#API_control_DeleteBucketTagging_RequestSyntax")**


The bucket ARN that has the tag set to be removed.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_DeleteBucketTagging_RequestSyntax "#API_control_DeleteBucketTagging_RequestSyntax")**


The AWS account ID of the Outposts bucket tag set to be removed.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Examples


### Sample request to delete tags for Amazon S3 on Outposts bucket


The following DELETE request deletes the tag set from the Outposts bucket
 `example-outpost-bucket`. 



```

            DELETE v20180820/bucket/example-outpost-bucket/tagging HTTP/1.1
            Host: s3-outposts.<Region>.amazonaws.com 
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            Date: Wed, 14 Dec 2020 05:37:16 GMT
            Authorization: signatureValue 
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteBucketTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteBucketTagging")
