# ListOriginRequestPolicies

Gets a list of origin request policies.

You can optionally apply a filter to return only the managed policies created by
 AWS, or only the custom policies created in your AWS account.

You can optionally specify the maximum number of items to receive in the response. If
 the total number of items in the list exceeds the maximum that you specify, or the
 default maximum, the response is paginated. To get the next page of items, send a
 subsequent request that specifies the `NextMarker` value from the current
 response as the `Marker` value in the subsequent request.


## Request Syntax



```
GET /2020-05-31/origin-request-policy?Marker=`Marker`&MaxItems=`MaxItems`&Type=`Type` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListOriginRequestPolicies_RequestSyntax "#API_ListOriginRequestPolicies_RequestSyntax")**


Use this field when paginating results to indicate where to begin in your list of
 origin request policies. The response includes origin request policies in the list that
 occur after the marker. To get the next page of the list, set this field's value to the
 value of `NextMarker` from the current page's response.




**[MaxItems](#API_ListOriginRequestPolicies_RequestSyntax "#API_ListOriginRequestPolicies_RequestSyntax")**


The maximum number of origin request policies that you want in the response.




**[Type](#API_ListOriginRequestPolicies_RequestSyntax "#API_ListOriginRequestPolicies_RequestSyntax")**


A filter to return only the specified kinds of origin request policies. Valid values
 are:



* `managed` – Returns only the managed policies created by
 AWS.
* `custom` – Returns only the custom policies created in your
 AWS account.

Valid Values: `managed | custom`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<OriginRequestPolicyList>
   <Items>
      <OriginRequestPolicySummary>
         <OriginRequestPolicy>
            <Id>***string***</Id>
            <LastModifiedTime>***timestamp***</LastModifiedTime>
            <OriginRequestPolicyConfig>
               <Comment>***string***</Comment>
               <CookiesConfig>
                  <CookieBehavior>***string***</CookieBehavior>
                  <Cookies>
                     <Items>
                        <Name>***string***</Name>
                     </Items>
                     <Quantity>***integer***</Quantity>
                  </Cookies>
               </CookiesConfig>
               <HeadersConfig>
                  <HeaderBehavior>***string***</HeaderBehavior>
                  <Headers>
                     <Items>
                        <Name>***string***</Name>
                     </Items>
                     <Quantity>***integer***</Quantity>
                  </Headers>
               </HeadersConfig>
               <Name>***string***</Name>
               <QueryStringsConfig>
                  <QueryStringBehavior>***string***</QueryStringBehavior>
                  <QueryStrings>
                     <Items>
                        <Name>***string***</Name>
                     </Items>
                     <Quantity>***integer***</Quantity>
                  </QueryStrings>
               </QueryStringsConfig>
            </OriginRequestPolicyConfig>
         </OriginRequestPolicy>
         <Type>***string***</Type>
      </OriginRequestPolicySummary>
   </Items>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</OriginRequestPolicyList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[OriginRequestPolicyList](#API_ListOriginRequestPolicies_ResponseSyntax "#API_ListOriginRequestPolicies_ResponseSyntax")**


Root level tag for the OriginRequestPolicyList parameters.


Required: Yes




**[Items](#API_ListOriginRequestPolicies_ResponseSyntax "#API_ListOriginRequestPolicies_ResponseSyntax")**


Contains the origin request policies in the list.


Type: Array of [OriginRequestPolicySummary](API_OriginRequestPolicySummary.md "API_OriginRequestPolicySummary.md") objects




**[MaxItems](#API_ListOriginRequestPolicies_ResponseSyntax "#API_ListOriginRequestPolicies_ResponseSyntax")**


The maximum number of origin request policies requested.


Type: Integer




**[NextMarker](#API_ListOriginRequestPolicies_ResponseSyntax "#API_ListOriginRequestPolicies_ResponseSyntax")**


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing origin request policies where you left
 off.


Type: String




**[Quantity](#API_ListOriginRequestPolicies_ResponseSyntax "#API_ListOriginRequestPolicies_ResponseSyntax")**


The total number of origin request policies returned in the response.


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**NoSuchOriginRequestPolicy** 


The origin request policy does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListOriginRequestPolicies")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListOriginRequestPolicies "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListOriginRequestPolicies")
