# ListInvalidations

Lists invalidation batches.


## Request Syntax



```
GET /2020-05-31/distribution/`DistributionId`/invalidation?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[DistributionId](#API_ListInvalidations_RequestSyntax "#API_ListInvalidations_RequestSyntax")**


The distribution's ID.


Required: Yes




**[Marker](#API_ListInvalidations_RequestSyntax "#API_ListInvalidations_RequestSyntax")**


Use this parameter when paginating results to indicate where to begin in your list of
 invalidation batches. Because the results are returned in decreasing order from most
 recent to oldest, the most recent results are on the first page, the second page will
 contain earlier results, and so on. To get the next page of results, set
 `Marker` to the value of the `NextMarker` from the current
 page's response. This value is the same as the ID of the last invalidation batch on that
 page.




**[MaxItems](#API_ListInvalidations_RequestSyntax "#API_ListInvalidations_RequestSyntax")**


The maximum number of invalidation batches that you want in the response body.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<InvalidationList>
   <IsTruncated>***boolean***</IsTruncated>
   <Items>
      <InvalidationSummary>
         <CreateTime>***timestamp***</CreateTime>
         <Id>***string***</Id>
         <Status>***string***</Status>
      </InvalidationSummary>
   </Items>
   <Marker>***string***</Marker>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</InvalidationList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[InvalidationList](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


Root level tag for the InvalidationList parameters.


Required: Yes




**[IsTruncated](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


A flag that indicates whether more invalidation batch requests remain to be listed. If
 your results were truncated, you can make a follow-up pagination request using the
 `Marker` request parameter to retrieve more invalidation batches in the
 list.


Type: Boolean




**[Items](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


A complex type that contains one `InvalidationSummary` element for each
 invalidation batch created by the current AWS account.


Type: Array of [InvalidationSummary](API_InvalidationSummary.md "API_InvalidationSummary.md") objects




**[Marker](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


The value that you provided for the `Marker` request parameter.


Type: String




**[MaxItems](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


The value that you provided for the `MaxItems` request parameter.


Type: Integer




**[NextMarker](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


If `IsTruncated` is `true`, this element is present and contains
 the value that you can use for the `Marker` request parameter to continue
 listing your invalidation batches where they left off.


Type: String




**[Quantity](#API_ListInvalidations_ResponseSyntax "#API_ListInvalidations_ResponseSyntax")**


The number of invalidation batches that were created by the current AWS account.
 


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**NoSuchDistribution** 


The specified distribution does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListInvalidations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListInvalidations "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListInvalidations")
