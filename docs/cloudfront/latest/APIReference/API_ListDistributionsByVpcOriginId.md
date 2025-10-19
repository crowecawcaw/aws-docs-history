# ListDistributionsByVpcOriginId

List CloudFront distributions by their VPC origin ID.


## Request Syntax



```
GET /2020-05-31/distributionsByVpcOriginId/`VpcOriginId`?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListDistributionsByVpcOriginId_RequestSyntax "#API_ListDistributionsByVpcOriginId_RequestSyntax")**


The marker associated with the VPC origin distributions list.




**[MaxItems](#API_ListDistributionsByVpcOriginId_RequestSyntax "#API_ListDistributionsByVpcOriginId_RequestSyntax")**


The maximum number of items included in the list.




**[VpcOriginId](#API_ListDistributionsByVpcOriginId_RequestSyntax "#API_ListDistributionsByVpcOriginId_RequestSyntax")**


The VPC origin ID.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionIdList>
   <IsTruncated>***boolean***</IsTruncated>
   <Items>
      <DistributionId>***string***</DistributionId>
   </Items>
   <Marker>***string***</Marker>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</DistributionIdList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[DistributionIdList](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


Root level tag for the DistributionIdList parameters.


Required: Yes




**[IsTruncated](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


A flag that indicates whether more distribution IDs remain to be listed. If your
 results were truncated, you can make a subsequent request using the `Marker`
 request field to retrieve more distribution IDs in the list.


Type: Boolean




**[Items](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


Contains the distribution IDs in the list.


Type: Array of strings




**[Marker](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


The value provided in the `Marker` request field.


Type: String




**[MaxItems](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


The maximum number of distribution IDs requested.


Type: Integer




**[NextMarker](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


Contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing distribution IDs where you left off.


Type: String




**[Quantity](#API_ListDistributionsByVpcOriginId_ResponseSyntax "#API_ListDistributionsByVpcOriginId_ResponseSyntax")**


The total number of distribution IDs returned in the response.


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByVpcOriginId")
