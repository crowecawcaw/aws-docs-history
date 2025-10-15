# SubmitMultiRegionAccessPointRoutes

###### Note

This operation is not supported by directory buckets.

Submits an updated route configuration for a Multi-Region Access Point. This API operation updates the
 routing status for the specified Regions from active to passive, or from passive to active.
 A value of `0` indicates a passive status, which means that traffic won't be
 routed to the specified Region. A value of `100` indicates an active status,
 which means that traffic will be routed to the specified Region. At least one Region must
 be active at all times.

When the routing configuration is changed, any in-progress operations (uploads, copies,
 deletes, and so on) to formerly active Regions will continue to run to their final
 completion state (success or failure). The routing configurations of any Regions that
 aren’t specified remain unchanged.

###### Note

Updated routing configurations might not be immediately applied. It can take up to 2
 minutes for your changes to take effect.

To submit routing control changes and failover requests, use the Amazon S3 failover control
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
PATCH /v20180820/mrap/instances/`mrap+`/routes HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[SubmitMultiRegionAccessPointRoutesRequest](#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-SubmitMultiRegionAccessPointRoutesRequest "#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-SubmitMultiRegionAccessPointRoutesRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[RouteUpdates](#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-RouteUpdates "#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-RouteUpdates")>
      <Route>
         <[Bucket](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket")>`string`</[Bucket](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket")>
         <[Region](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region")>`string`</[Region](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-Region")>
         <[TrafficDialPercentage](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage")>`integer`</[TrafficDialPercentage](API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage "API_control_MultiRegionAccessPointRoute.md#AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage")>
      </Route>
   </[RouteUpdates](#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-RouteUpdates "#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-RouteUpdates")>
</[SubmitMultiRegionAccessPointRoutesRequest](#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-SubmitMultiRegionAccessPointRoutesRequest "#AmazonS3-control_SubmitMultiRegionAccessPointRoutes-request-SubmitMultiRegionAccessPointRoutesRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[mrap](#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax "#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax")**


The Multi-Region Access Point ARN.


Length Constraints: Maximum length of 200.


Pattern: `^[a-zA-Z0-9\:.-]{3,200}$`



Required: Yes




**[x-amz-account-id](#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax "#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax")**


The AWS account ID for the owner of the Multi-Region Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[SubmitMultiRegionAccessPointRoutesRequest](#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax "#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax")**


Root level tag for the SubmitMultiRegionAccessPointRoutesRequest parameters.


Required: Yes




**[RouteUpdates](#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax "#API_control_SubmitMultiRegionAccessPointRoutes_RequestSyntax")**


The different routes that make up the new route configuration. Active routes return a
 value of `100`, and passive routes return a value of `0`.


Type: Array of [MultiRegionAccessPointRoute](API_control_MultiRegionAccessPointRoute.md "API_control_MultiRegionAccessPointRoute.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample request for initiating failover


In the following example, the request to submit these routing changes to initiate
 a failover is sent to the failover control infrastructure in the
 `us-east-1` Region. In this example, the `eu-north-1` Region
 is set to active, and the `ap-northeast-3` Region is set to passive. In
 other words, the `ap-northeast-3` Region is failed over to the
 `eu-north-1` Region.



```

PATCH /v20180820/mrap/instances/<Multi-Region Access Point>/routes HTTP/1.1
Host: example-account-id.s3-control.us-east-1.amazonaws.com
            
<SubmitMultiRegionAccessPointRoutesRequest>
  <RouteUpdates>
     <Route>
      <Region>eu-north-1</Region>
      <Bucket>example-bucket-eu-north-1</Bucket>
      <TrafficDialPercentage>100</TrafficDialPercentage>
     </Route>
     <Route>
      <Region>ap-northeast-3</Region>
      <Bucket>example-bucket-ap-northeast-3</Bucket>
      <TrafficDialPercentage>0</TrafficDialPercentage>
     </Route>
  </RouteUpdates>
</SubmitMultiRegionAccessPointRoutesRequest>
            
```

### Sample request for setting a Region to active status


The following request updates the route configuration of the
 `eu-north-1` Region to active. The request is sent to the failover
 control infrastructure in the `eu-west-1` Region.



```

PATCH /v20180820/mrap/instances/<Multi-Region Access Point>/routes HTTP/1.1
Host: example-account-id.s3-control.eu-west-1.amazonaws.com

<SubmitMultiRegionAccessPointRoutesRequest>
   <RouteUpdates>
    <Route>
      <Region>eu-north-1<Region>
      <Bucket>example-bucket-eu-north-1</Bucket>
      <TrafficDialPercentage>100</TrafficDialPercentage>
    </Route>
   </RouteUpdates>
</SubmitMultiRegionAccessPointRoutesRequest>
   
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SubmitMultiRegionAccessPointRoutes")
