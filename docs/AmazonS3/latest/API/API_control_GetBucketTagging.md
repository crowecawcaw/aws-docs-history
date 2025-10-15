# GetBucketTagging

###### Note

This action gets an Amazon S3 on Outposts bucket's tags. To get an S3 bucket tags, see
 [GetBucketTagging](API_GetBucketTagging.md "API_GetBucketTagging.md") in the *Amazon S3 API Reference*. 

Returns the tag set associated with the Outposts bucket. For more information, see
 [Using
 Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.

To use this action, you must have permission to perform the
 `GetBucketTagging` action. By default, the bucket owner has this permission
 and can grant this permission to others.


`GetBucketTagging` has the following special error:


* Error code: `NoSuchTagSetError`





	+ Description: There is no tag set associated with the bucket.
All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_GetBucketTagging.md#API_control_GetBucketTagging_Examples "API_control_GetBucketTagging.md#API_control_GetBucketTagging_Examples") section.

The following actions are related to `GetBucketTagging`:


* [PutBucketTagging](API_control_PutBucketTagging.md "API_control_PutBucketTagging.md")
* [DeleteBucketTagging](API_control_DeleteBucketTagging.md "API_control_DeleteBucketTagging.md")

## Request Syntax



```
GET /v20180820/bucket/`name`/tagging HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetBucketTagging_RequestSyntax "#API_control_GetBucketTagging_RequestSyntax")**


Specifies the bucket.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_GetBucketTagging_RequestSyntax "#API_control_GetBucketTagging_RequestSyntax")**


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
<[GetBucketTaggingResult](#AmazonS3-control_GetBucketTagging-response-GetBucketTaggingResult "#AmazonS3-control_GetBucketTagging-response-GetBucketTaggingResult")>
   <[TagSet](#AmazonS3-control_GetBucketTagging-response-TagSet "#AmazonS3-control_GetBucketTagging-response-TagSet")>
      <S3Tag>
         <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
         <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
      </S3Tag>
   </[TagSet](#AmazonS3-control_GetBucketTagging-response-TagSet "#AmazonS3-control_GetBucketTagging-response-TagSet")>
</[GetBucketTaggingResult](#AmazonS3-control_GetBucketTagging-response-GetBucketTaggingResult "#AmazonS3-control_GetBucketTagging-response-GetBucketTaggingResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetBucketTaggingResult](#API_control_GetBucketTagging_ResponseSyntax "#API_control_GetBucketTagging_ResponseSyntax")**


Root level tag for the GetBucketTaggingResult parameters.


Required: Yes




**[TagSet](#API_control_GetBucketTagging_ResponseSyntax "#API_control_GetBucketTagging_ResponseSyntax")**


The tags set of the Outposts bucket.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types




## Examples


### Amazon S3 on Outposts request example for getting a tag set for an Outposts
 bucket


The following request gets the tag set of the specified Outposts bucket
 `example-outpost-bucket`.



```

            GET /v20180820/bucket/example-outpost-bucket/tagging HTTP/1.1
            Host: s3-outposts.<Region>.amazonaws.com
            x-amz-date: Wed, 28 Oct 2020 22:32:00 GMT
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            Authorization: authorization string
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketTagging")
