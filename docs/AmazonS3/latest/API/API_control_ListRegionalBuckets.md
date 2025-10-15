# ListRegionalBuckets

###### Note

This operation is not supported by directory buckets.

Returns a list of all Outposts buckets in an Outpost that are owned by the authenticated
 sender of the request. For more information, see [Using Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the
 *Amazon S3 User Guide*.

For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts
 endpoint hostname prefix and `x-amz-outpost-id` in your request, see the [Examples](API_control_ListRegionalBuckets.md#API_control_ListRegionalBuckets_Examples "API_control_ListRegionalBuckets.md#API_control_ListRegionalBuckets_Examples") section.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/bucket?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
x-amz-outpost-id: `OutpostId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[maxResults](#API_control_ListRegionalBuckets_RequestSyntax "#API_control_ListRegionalBuckets_RequestSyntax")**



Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListRegionalBuckets_RequestSyntax "#API_control_ListRegionalBuckets_RequestSyntax")**



Length Constraints: Minimum length of 1. Maximum length of 1024.




**[x-amz-account-id](#API_control_ListRegionalBuckets_RequestSyntax "#API_control_ListRegionalBuckets_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




**[x-amz-outpost-id](#API_control_ListRegionalBuckets_RequestSyntax "#API_control_ListRegionalBuckets_RequestSyntax")**


The ID of the AWS Outposts resource.


###### Note

This ID is required by Amazon S3 on Outposts buckets.


Length Constraints: Minimum length of 1. Maximum length of 64.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListRegionalBucketsResult](#AmazonS3-control_ListRegionalBuckets-response-ListRegionalBucketsResult "#AmazonS3-control_ListRegionalBuckets-response-ListRegionalBucketsResult")>
   <[RegionalBucketList](#AmazonS3-control_ListRegionalBuckets-response-RegionalBucketList "#AmazonS3-control_ListRegionalBuckets-response-RegionalBucketList")>
      <RegionalBucket>
         <[Bucket](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-Bucket "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-Bucket")>***string***</[Bucket](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-Bucket "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-Bucket")>
         <[BucketArn](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-BucketArn "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-BucketArn")>***string***</[BucketArn](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-BucketArn "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-BucketArn")>
         <[CreationDate](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-CreationDate "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-CreationDate")>***timestamp***</[CreationDate](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-CreationDate "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-CreationDate")>
         <[OutpostId](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-OutpostId "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-OutpostId")>***string***</[OutpostId](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-OutpostId "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-OutpostId")>
         <[PublicAccessBlockEnabled](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-PublicAccessBlockEnabled "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-PublicAccessBlockEnabled")>***boolean***</[PublicAccessBlockEnabled](API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-PublicAccessBlockEnabled "API_control_RegionalBucket.md#AmazonS3-Type-control_RegionalBucket-PublicAccessBlockEnabled")>
      </RegionalBucket>
   </[RegionalBucketList](#AmazonS3-control_ListRegionalBuckets-response-RegionalBucketList "#AmazonS3-control_ListRegionalBuckets-response-RegionalBucketList")>
   <[NextToken](#AmazonS3-control_ListRegionalBuckets-response-NextToken "#AmazonS3-control_ListRegionalBuckets-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListRegionalBuckets-response-NextToken "#AmazonS3-control_ListRegionalBuckets-response-NextToken")>
</[ListRegionalBucketsResult](#AmazonS3-control_ListRegionalBuckets-response-ListRegionalBucketsResult "#AmazonS3-control_ListRegionalBuckets-response-ListRegionalBucketsResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListRegionalBucketsResult](#API_control_ListRegionalBuckets_ResponseSyntax "#API_control_ListRegionalBuckets_ResponseSyntax")**


Root level tag for the ListRegionalBucketsResult parameters.


Required: Yes




**[NextToken](#API_control_ListRegionalBuckets_ResponseSyntax "#API_control_ListRegionalBuckets_ResponseSyntax")**



`NextToken` is sent when `isTruncated` is true, which means there
 are more buckets that can be listed. The next list requests to Amazon S3 can be continued with
 this `NextToken`. `NextToken` is obfuscated and is not a real
 key.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**[RegionalBucketList](#API_control_ListRegionalBuckets_ResponseSyntax "#API_control_ListRegionalBuckets_ResponseSyntax")**



Type: Array of [RegionalBucket](API_control_RegionalBucket.md "API_control_RegionalBucket.md") data types




## Examples


### Sample request to list an account's Outposts buckets


This request lists regional buckets.



```

            GET /v20180820/bucket HTTP /1.1            
            Host:s3-outposts.us-west-2.amazonaws.com
            Content-Length: 0
            x-amz-outpost-id: op-01ac5d28a6a232904
            x-amz-account-id: example-account-id
            Date: Wed, 01 Mar  2006 12:00:00 GMT
            Authorization: authorization string
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListRegionalBuckets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListRegionalBuckets "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListRegionalBuckets")
