# ListMultiRegionAccessPoints

###### Note

This operation is not supported by directory buckets.

Returns a list of the Multi-Region Access Points currently associated with the specified AWS account.
 Each call can return up to 100 Multi-Region Access Points, the maximum number of Multi-Region Access Points that can be
 associated with a single account.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

The following actions are related to `ListMultiRegionAccessPoint`:


* [CreateMultiRegionAccessPoint](API_control_CreateMultiRegionAccessPoint.md "API_control_CreateMultiRegionAccessPoint.md")
* [DeleteMultiRegionAccessPoint](API_control_DeleteMultiRegionAccessPoint.md "API_control_DeleteMultiRegionAccessPoint.md")
* [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md")
* [GetMultiRegionAccessPoint](API_control_GetMultiRegionAccessPoint.md "API_control_GetMultiRegionAccessPoint.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/mrap/instances?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[maxResults](#API_control_ListMultiRegionAccessPoints_RequestSyntax "#API_control_ListMultiRegionAccessPoints_RequestSyntax")**


Not currently used. Do not use this parameter.


Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListMultiRegionAccessPoints_RequestSyntax "#API_control_ListMultiRegionAccessPoints_RequestSyntax")**


Not currently used. Do not use this parameter.


Length Constraints: Minimum length of 1. Maximum length of 1024.




**[x-amz-account-id](#API_control_ListMultiRegionAccessPoints_RequestSyntax "#API_control_ListMultiRegionAccessPoints_RequestSyntax")**


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
<[ListMultiRegionAccessPointsResult](#AmazonS3-control_ListMultiRegionAccessPoints-response-ListMultiRegionAccessPointsResult "#AmazonS3-control_ListMultiRegionAccessPoints-response-ListMultiRegionAccessPointsResult")>
   <[AccessPoints](#AmazonS3-control_ListMultiRegionAccessPoints-response-AccessPoints "#AmazonS3-control_ListMultiRegionAccessPoints-response-AccessPoints")>
      <AccessPoint>
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
      </AccessPoint>
   </[AccessPoints](#AmazonS3-control_ListMultiRegionAccessPoints-response-AccessPoints "#AmazonS3-control_ListMultiRegionAccessPoints-response-AccessPoints")>
   <[NextToken](#AmazonS3-control_ListMultiRegionAccessPoints-response-NextToken "#AmazonS3-control_ListMultiRegionAccessPoints-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListMultiRegionAccessPoints-response-NextToken "#AmazonS3-control_ListMultiRegionAccessPoints-response-NextToken")>
</[ListMultiRegionAccessPointsResult](#AmazonS3-control_ListMultiRegionAccessPoints-response-ListMultiRegionAccessPointsResult "#AmazonS3-control_ListMultiRegionAccessPoints-response-ListMultiRegionAccessPointsResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListMultiRegionAccessPointsResult](#API_control_ListMultiRegionAccessPoints_ResponseSyntax "#API_control_ListMultiRegionAccessPoints_ResponseSyntax")**


Root level tag for the ListMultiRegionAccessPointsResult parameters.


Required: Yes




**[AccessPoints](#API_control_ListMultiRegionAccessPoints_ResponseSyntax "#API_control_ListMultiRegionAccessPoints_ResponseSyntax")**


The list of Multi-Region Access Points associated with the user.


Type: Array of [MultiRegionAccessPointReport](API_control_MultiRegionAccessPointReport.md "API_control_MultiRegionAccessPointReport.md") data types




**[NextToken](#API_control_ListMultiRegionAccessPoints_ResponseSyntax "#API_control_ListMultiRegionAccessPoints_ResponseSyntax")**


If the specified bucket has more Multi-Region Access Points than can be returned in one call to this
 action, this field contains a continuation token. You can use this token tin subsequent
 calls to this action to retrieve additional Multi-Region Access Points.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListMultiRegionAccessPoints")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListMultiRegionAccessPoints "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListMultiRegionAccessPoints")
