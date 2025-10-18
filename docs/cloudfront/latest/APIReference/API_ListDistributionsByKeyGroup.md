# ListDistributionsByKeyGroup

Gets a list of distribution IDs for distributions that have a cache behavior that
 references the specified key group.

You can optionally specify the maximum number of items to receive in the response. If
 the total number of items in the list exceeds the maximum that you specify, or the
 default maximum, the response is paginated. To get the next page of items, send a
 subsequent request that specifies the `NextMarker` value from the current
 response as the `Marker` value in the subsequent request.


## Request Syntax



```
GET /2020-05-31/distributionsByKeyGroupId/`KeyGroupId`?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[KeyGroupId](#API_ListDistributionsByKeyGroup_RequestSyntax "#API_ListDistributionsByKeyGroup_RequestSyntax")**


The ID of the key group whose associated distribution IDs you are listing.


Required: Yes




**[Marker](#API_ListDistributionsByKeyGroup_RequestSyntax "#API_ListDistributionsByKeyGroup_RequestSyntax")**


Use this field when paginating results to indicate where to begin in your list of
 distribution IDs. The response includes distribution IDs in the list that occur after
 the marker. To get the next page of the list, set this field's value to the value of
 `NextMarker` from the current page's response.




**[MaxItems](#API_ListDistributionsByKeyGroup_RequestSyntax "#API_ListDistributionsByKeyGroup_RequestSyntax")**


The maximum number of distribution IDs that you want in the response.




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





**[DistributionIdList](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


Root level tag for the DistributionIdList parameters.


Required: Yes




**[IsTruncated](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


A flag that indicates whether more distribution IDs remain to be listed. If your
 results were truncated, you can make a subsequent request using the `Marker`
 request field to retrieve more distribution IDs in the list.


Type: Boolean




**[Items](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


Contains the distribution IDs in the list.


Type: Array of strings




**[Marker](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


The value provided in the `Marker` request field.


Type: String




**[MaxItems](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


The maximum number of distribution IDs requested.


Type: Integer




**[NextMarker](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


Contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing distribution IDs where you left off.


Type: String




**[Quantity](#API_ListDistributionsByKeyGroup_ResponseSyntax "#API_ListDistributionsByKeyGroup_ResponseSyntax")**


The total number of distribution IDs returned in the response.


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**NoSuchResource** 


A resource that was specified is not valid.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByKeyGroup")
