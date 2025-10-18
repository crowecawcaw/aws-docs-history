# ListCloudFrontOriginAccessIdentities

Lists origin access identities.


## Request Syntax



```
GET /2020-05-31/origin-access-identity/cloudfront?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListCloudFrontOriginAccessIdentities_RequestSyntax "#API_ListCloudFrontOriginAccessIdentities_RequestSyntax")**


Use this when paginating results to indicate where to begin in your list of origin
 access identities. The results include identities in the list that occur after the
 marker. To get the next page of results, set the `Marker` to the value of the
 `NextMarker` from the current page's response (which is also the ID of
 the last identity on that page).




**[MaxItems](#API_ListCloudFrontOriginAccessIdentities_RequestSyntax "#API_ListCloudFrontOriginAccessIdentities_RequestSyntax")**


The maximum number of origin access identities you want in the response body.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CloudFrontOriginAccessIdentityList>
   <IsTruncated>***boolean***</IsTruncated>
   <Items>
      <CloudFrontOriginAccessIdentitySummary>
         <Comment>***string***</Comment>
         <Id>***string***</Id>
         <S3CanonicalUserId>***string***</S3CanonicalUserId>
      </CloudFrontOriginAccessIdentitySummary>
   </Items>
   <Marker>***string***</Marker>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</CloudFrontOriginAccessIdentityList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CloudFrontOriginAccessIdentityList](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


Root level tag for the CloudFrontOriginAccessIdentityList parameters.


Required: Yes




**[IsTruncated](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


A flag that indicates whether more origin access identities remain to be listed. If
 your results were truncated, you can make a follow-up pagination request using the
 `Marker` request parameter to retrieve more items in the list.


Type: Boolean




**[Items](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


A complex type that contains one `CloudFrontOriginAccessIdentitySummary`
 element for each origin access identity that was created by the current
 AWS account.


Type: Array of [CloudFrontOriginAccessIdentitySummary](API_CloudFrontOriginAccessIdentitySummary.md "API_CloudFrontOriginAccessIdentitySummary.md") objects




**[Marker](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


Use this when paginating results to indicate where to begin in your list of origin
 access identities. The results include identities in the list that occur after the
 marker. To get the next page of results, set the `Marker` to the value of the
 `NextMarker` from the current page's response (which is also the ID of
 the last identity on that page).


Type: String




**[MaxItems](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


The maximum number of origin access identities you want in the response body.


Type: Integer




**[NextMarker](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


If `IsTruncated` is `true`, this element is present and contains
 the value you can use for the `Marker` request parameter to continue listing
 your origin access identities where they left off.


Type: String




**[Quantity](#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax "#API_ListCloudFrontOriginAccessIdentities_ResponseSyntax")**


The number of CloudFront origin access identities that were created by the current
 AWS account.


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListCloudFrontOriginAccessIdentities")
