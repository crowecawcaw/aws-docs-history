# CreateMultiRegionAccessPoint

###### Note

This operation is not supported by directory buckets.

Creates a Multi-Region Access Point and associates it with the specified buckets. For more information
 about creating Multi-Region Access Points, see [Creating
 Multi-Region Access Points](../userguide/CreatingMultiRegionAccessPoints.md "../userguide/CreatingMultiRegionAccessPoints.md") in the *Amazon S3 User Guide*.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

This request is asynchronous, meaning that you might receive a response before the
 command has completed. When this request provides a response, it provides a token that you
 can use to monitor the status of the request with
 `DescribeMultiRegionAccessPointOperation`.

The following actions are related to `CreateMultiRegionAccessPoint`:


* [DeleteMultiRegionAccessPoint](API_control_DeleteMultiRegionAccessPoint.md "API_control_DeleteMultiRegionAccessPoint.md")
* [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md")
* [GetMultiRegionAccessPoint](API_control_GetMultiRegionAccessPoint.md "API_control_GetMultiRegionAccessPoint.md")
* [ListMultiRegionAccessPoints](API_control_ListMultiRegionAccessPoints.md "API_control_ListMultiRegionAccessPoints.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/async-requests/mrap/create HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateMultiRegionAccessPointRequest](#AmazonS3-control_CreateMultiRegionAccessPoint-request-CreateMultiRegionAccessPointRequest "#AmazonS3-control_CreateMultiRegionAccessPoint-request-CreateMultiRegionAccessPointRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[ClientToken](#AmazonS3-control_CreateMultiRegionAccessPoint-request-ClientToken "#AmazonS3-control_CreateMultiRegionAccessPoint-request-ClientToken")>`string`</[ClientToken](#AmazonS3-control_CreateMultiRegionAccessPoint-request-ClientToken "#AmazonS3-control_CreateMultiRegionAccessPoint-request-ClientToken")>
   <[Details](#AmazonS3-control_CreateMultiRegionAccessPoint-request-Details "#AmazonS3-control_CreateMultiRegionAccessPoint-request-Details")>
      <[Name](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name")>`string`</[Name](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name")>
      <[PublicAccessBlock](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock")>
         <[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>`boolean`</[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>
         <[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>`boolean`</[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>
         <[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>`boolean`</[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>
         <[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>`boolean`</[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>
      </[PublicAccessBlock](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock")>
      <[Regions](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions")>
         <Region>
            <[Bucket](API_control_Region.md#AmazonS3-Type-control_Region-Bucket "API_control_Region.md#AmazonS3-Type-control_Region-Bucket")>`string`</[Bucket](API_control_Region.md#AmazonS3-Type-control_Region-Bucket "API_control_Region.md#AmazonS3-Type-control_Region-Bucket")>
            <[BucketAccountId](API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId "API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId")>`string`</[BucketAccountId](API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId "API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId")>
         </Region>
      </[Regions](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions")>
   </[Details](#AmazonS3-control_CreateMultiRegionAccessPoint-request-Details "#AmazonS3-control_CreateMultiRegionAccessPoint-request-Details")>
</[CreateMultiRegionAccessPointRequest](#AmazonS3-control_CreateMultiRegionAccessPoint-request-CreateMultiRegionAccessPointRequest "#AmazonS3-control_CreateMultiRegionAccessPoint-request-CreateMultiRegionAccessPointRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_CreateMultiRegionAccessPoint_RequestSyntax "#API_control_CreateMultiRegionAccessPoint_RequestSyntax")**


The AWS account ID for the owner of the Multi-Region Access Point. The owner of the Multi-Region Access Point also must own
 the underlying buckets.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateMultiRegionAccessPointRequest](#API_control_CreateMultiRegionAccessPoint_RequestSyntax "#API_control_CreateMultiRegionAccessPoint_RequestSyntax")**


Root level tag for the CreateMultiRegionAccessPointRequest parameters.


Required: Yes




**[ClientToken](#API_control_CreateMultiRegionAccessPoint_RequestSyntax "#API_control_CreateMultiRegionAccessPoint_RequestSyntax")**


An idempotency token used to identify the request and guarantee that requests are
 unique.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `\S+`



Required: Yes




**[Details](#API_control_CreateMultiRegionAccessPoint_RequestSyntax "#API_control_CreateMultiRegionAccessPoint_RequestSyntax")**


A container element containing details about the Multi-Region Access Point.


Type: [CreateMultiRegionAccessPointInput](API_control_CreateMultiRegionAccessPointInput.md "API_control_CreateMultiRegionAccessPointInput.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CreateMultiRegionAccessPointResult](#AmazonS3-control_CreateMultiRegionAccessPoint-response-CreateMultiRegionAccessPointResult "#AmazonS3-control_CreateMultiRegionAccessPoint-response-CreateMultiRegionAccessPointResult")>
   <[RequestTokenARN](#AmazonS3-control_CreateMultiRegionAccessPoint-response-RequestTokenARN "#AmazonS3-control_CreateMultiRegionAccessPoint-response-RequestTokenARN")>***string***</[RequestTokenARN](#AmazonS3-control_CreateMultiRegionAccessPoint-response-RequestTokenARN "#AmazonS3-control_CreateMultiRegionAccessPoint-response-RequestTokenARN")>
</[CreateMultiRegionAccessPointResult](#AmazonS3-control_CreateMultiRegionAccessPoint-response-CreateMultiRegionAccessPointResult "#AmazonS3-control_CreateMultiRegionAccessPoint-response-CreateMultiRegionAccessPointResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CreateMultiRegionAccessPointResult](#API_control_CreateMultiRegionAccessPoint_ResponseSyntax "#API_control_CreateMultiRegionAccessPoint_ResponseSyntax")**


Root level tag for the CreateMultiRegionAccessPointResult parameters.


Required: Yes




**[RequestTokenARN](#API_control_CreateMultiRegionAccessPoint_ResponseSyntax "#API_control_CreateMultiRegionAccessPoint_ResponseSyntax")**


The request token associated with the request. You can use this token with [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md") to determine the status of asynchronous
 requests.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:.+`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateMultiRegionAccessPoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateMultiRegionAccessPoint")
