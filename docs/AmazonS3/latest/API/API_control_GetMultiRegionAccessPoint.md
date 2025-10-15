# GetMultiRegionAccessPoint

###### Note

This operation is not supported by directory buckets.

Returns configuration information about the specified Multi-Region Access Point.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

The following actions are related to `GetMultiRegionAccessPoint`:


* [CreateMultiRegionAccessPoint](API_control_CreateMultiRegionAccessPoint.md "API_control_CreateMultiRegionAccessPoint.md")
* [DeleteMultiRegionAccessPoint](API_control_DeleteMultiRegionAccessPoint.md "API_control_DeleteMultiRegionAccessPoint.md")
* [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md")
* [ListMultiRegionAccessPoints](API_control_ListMultiRegionAccessPoints.md "API_control_ListMultiRegionAccessPoints.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/mrap/instances/`name+` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetMultiRegionAccessPoint_RequestSyntax "#API_control_GetMultiRegionAccessPoint_RequestSyntax")**


The name of the Multi-Region Access Point whose configuration information you want to receive. The name of
 the Multi-Region Access Point is different from the alias. For more information about the distinction between
 the name and the alias of an Multi-Region Access Point, see [Rules for naming Amazon S3 Multi-Region Access Points](../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming "../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming") in the
 *Amazon S3 User Guide*.


Length Constraints: Maximum length of 50.


Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`



Required: Yes




**[x-amz-account-id](#API_control_GetMultiRegionAccessPoint_RequestSyntax "#API_control_GetMultiRegionAccessPoint_RequestSyntax")**


The AWS account ID for the owner of the Multi-Region Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetMultiRegionAccessPointResult](#AmazonS3-control_GetMultiRegionAccessPoint-response-GetMultiRegionAccessPointResult "#AmazonS3-control_GetMultiRegionAccessPoint-response-GetMultiRegionAccessPointResult")>
   <[AccessPoint](#AmazonS3-control_GetMultiRegionAccessPoint-response-AccessPoint "#AmazonS3-control_GetMultiRegionAccessPoint-response-AccessPoint")>
      <[Alias](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Alias "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Alias")>***string***</[Alias](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Alias "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Alias")>
      <[CreatedAt](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-CreatedAt "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-CreatedAt")>***timestamp***</[CreatedAt](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-CreatedAt "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-CreatedAt")>
      <[Name](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Name "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Name")>***string***</[Name](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Name "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Name")>
      <[PublicAccessBlock](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-PublicAccessBlock "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-PublicAccessBlock")>
         <[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>***boolean***</[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>
         <[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>***boolean***</[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>
         <[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>***boolean***</[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>
         <[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>***boolean***</[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>
      </[PublicAccessBlock](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-PublicAccessBlock "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-PublicAccessBlock")>
      <[Regions](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Regions "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Regions")>
         <Region>
            <[Bucket](API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Bucket "API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Bucket")>***string***</[Bucket](API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Bucket "API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Bucket")>
            <[BucketAccountId](API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-BucketAccountId "API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-BucketAccountId")>***string***</[BucketAccountId](API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-BucketAccountId "API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-BucketAccountId")>
            <[Region](API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Region "API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Region")>***string***</[Region](API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Region "API_control_RegionReport.md#AmazonS3-Type-control_RegionReport-Region")>
         </Region>
      </[Regions](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Regions "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Regions")>
      <[Status](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Status "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Status")>***string***</[Status](API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Status "API_control_MultiRegionAccessPointReport.md#AmazonS3-Type-control_MultiRegionAccessPointReport-Status")>
   </[AccessPoint](#AmazonS3-control_GetMultiRegionAccessPoint-response-AccessPoint "#AmazonS3-control_GetMultiRegionAccessPoint-response-AccessPoint")>
</[GetMultiRegionAccessPointResult](#AmazonS3-control_GetMultiRegionAccessPoint-response-GetMultiRegionAccessPointResult "#AmazonS3-control_GetMultiRegionAccessPoint-response-GetMultiRegionAccessPointResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetMultiRegionAccessPointResult](#API_control_GetMultiRegionAccessPoint_ResponseSyntax "#API_control_GetMultiRegionAccessPoint_ResponseSyntax")**


Root level tag for the GetMultiRegionAccessPointResult parameters.


Required: Yes




**[AccessPoint](#API_control_GetMultiRegionAccessPoint_ResponseSyntax "#API_control_GetMultiRegionAccessPoint_ResponseSyntax")**


A container element containing the details of the requested Multi-Region Access Point.


Type: [MultiRegionAccessPointReport](API_control_MultiRegionAccessPointReport.md "API_control_MultiRegionAccessPointReport.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPoint")
