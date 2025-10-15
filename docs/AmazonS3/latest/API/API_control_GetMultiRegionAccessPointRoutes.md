# GetMultiRegionAccessPointRoutes

###### Note

This operation is not supported by directory buckets.

Returns the routing configuration for a Multi-Region Access Point, indicating which Regions are active or
 passive.

To obtain routing control changes and failover requests, use the Amazon S3 failover control
 infrastructure endpoints in these five AWS Regions:


* `us-east-1`
* `us-west-2`
* `ap-southeast-2`
* `ap-northeast-1`
* `eu-west-1`
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/mrap/instances/`mrap+`/routes HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[mrap](#API_control_GetMultiRegionAccessPointRoutes_RequestSyntax "#API_control_GetMultiRegionAccessPointRoutes_RequestSyntax")**


The Multi-Region Access Point ARN.


Length Constraints: Maximum length of 200.


Pattern: `^[a-zA-Z0-9\:.-]{3,200}$`



Required: Yes




**[x-amz-account-id](#API_control_GetMultiRegionAccessPointRoutes_RequestSyntax "#API_control_GetMultiRegionAccessPointRoutes_RequestSyntax")**


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
<[GetMultiRegionAccessPointRoutesResult](#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-GetMultiRegionAccessPointRoutesResult "#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-GetMultiRegionAccessPointRoutesResult")>
   <[Mrap](#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Mrap "#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Mrap")>***string***</[Mrap](#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Mrap "#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Mrap")>
   <[Routes](#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Routes "#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Routes")>
      <Route>
         <[Bucket](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket")>***string***</[Bucket](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket")>
         <[Region](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region")>***string***</[Region](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region")>
         <[TrafficDialPercentage](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage")>***integer***</[TrafficDialPercentage](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage")>
      </Route>
   </[Routes](#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Routes "#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Routes")>
</[GetMultiRegionAccessPointRoutesResult](#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-GetMultiRegionAccessPointRoutesResult "#AmazonS3-control_GetMultiRegionAccessPointRoutes-response-GetMultiRegionAccessPointRoutesResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetMultiRegionAccessPointRoutesResult](#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax "#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax")**


Root level tag for the GetMultiRegionAccessPointRoutesResult parameters.


Required: Yes




**[Mrap](#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax "#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax")**


The Multi-Region Access Point ARN.


Type: String


Length Constraints: Maximum length of 200.


Pattern: `^[a-zA-Z0-9\:.-]{3,200}$`





**[Routes](#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax "#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax")**


The different routes that make up the route configuration. Active routes return a value
 of `100`, and passive routes return a value of `0`.


Type: Array of [MultiRegionAccessPointRoute](API_control_MultiRegionAccessPointRoute.md "API_control_MultiRegionAccessPointRoute.md") data types




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes")
